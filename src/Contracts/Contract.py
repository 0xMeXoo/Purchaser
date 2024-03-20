import settings
from src.networks import arbitrum_net
from src.ABIs import Sale_ABI
from src.Helpers.txnHelper import get_txn_dict, check_estimate_gas, approve_amount, exec_txn, delay_sleep, get_gas_price
import eth_abi
from src.logger import cs_logger
from src.tokens import wETH_token
from time import time
from math import ceil


class ContractTier(object):
    def __init__(self, tier, title, contract_address, price, allocation, buy_limit, max_total_purchase):
        self.tier = tier
        self.title = title
        self.contract_address = contract_address
        self.contract = arbitrum_net.web3.eth.contract(arbitrum_net.web3.to_checksum_address(contract_address),
                                                       abi=Sale_ABI)
        if settings.smart_contract_source == 1:
            self.price = self.contract.functions.salePrice().call()
            self.allocation = self.contract.functions.publicAllocation().call()
        else:
            self.price = price
            self.allocation = allocation

        self.buy_limit = buy_limit

        if settings.proof_empty == 1:
            self.proof = []
        else:
            self.proof = [eth_abi.encode(['bytes32'], [b''])]

        self.max_total_purchase = max_total_purchase

    def build_txn_purchase(self, wallet):
        try:
            discount_code = settings.discount_code
            dict_transaction = get_txn_dict(wallet.address, arbitrum_net)
            value = self.price * settings.lot_number
            if settings.simple_purchase == 1:
                txn = self.contract.functions.purchase(
                    value
                ).build_transaction(dict_transaction)
                return txn

            if discount_code != '-':
                txn = self.contract.functions.whitelistedPurchaseWithCode(
                    value, self.proof, self.allocation, discount_code
                ).build_transaction(dict_transaction)
                return txn

            else:
                txn = self.contract.functions.whitelistedPurchase(
                    value, self.proof, self.allocation
                ).build_transaction(dict_transaction)
                return txn

        except Exception as ex:
            cs_logger.info(f'Ошибка в (ContractTier: build_txn) {ex.args}')

    def purchase(self, wallet):
        try:
            cs_logger.info(f'Пытаемся купить Tier {self.tier} по таймингу, контракт - {self.contract_address}')
            approve_amount(wallet, self.contract_address, wETH_token, arbitrum_net, self.price)
            curr_time = ceil(time())
            while curr_time < settings.start_time:
                curr_time = ceil(time())
            txn = self.build_txn_purchase(wallet)
            estimate_gas = check_estimate_gas(txn, arbitrum_net)
            if type(estimate_gas) is str:
                cs_logger.info(f'{estimate_gas}')
                delay_sleep(settings.delay[0], settings.delay[1])
                return False
            txn['gas'] = estimate_gas
            txn_hash, txn_status = exec_txn(wallet.key, txn, arbitrum_net)
            cs_logger.info(f'Hash покупки: {txn_hash}')
            wallet.txn_num[self.title] += settings.lot_number
            return True

        except Exception as ex:
            cs_logger.info(f'Ошибка в (ContractTier: purchase) {ex.args}')
            delay_sleep(settings.delay[0], settings.delay[1])

    def purchase_timing(self, wallet):
        try:
            i = 0
            cs_logger.info(f'Пытаемся купить Tier {self.tier} по таймингу, контракт - {self.contract_address}')
            approve_amount(wallet, self.contract_address, wETH_token, arbitrum_net, self.price)
            txn = self.build_txn_purchase(wallet)
            txn['gas'] = 6_000_000
            curr_time = ceil(time())
            while curr_time < settings.start_time:
                curr_time = ceil(time())
                if (settings.start_time - curr_time) < 4 and i == 0:
                    i += 1
                    cs_logger.info(f'Сейл через несколько секунд!')
                    txn['gasPrice'] = get_gas_price(arbitrum_net)
            txn_hash, txn_status = exec_txn(wallet.key, txn, arbitrum_net)
            cs_logger.info(f'Hash покупки: {txn_hash}')
            wallet.txn_num[self.title] += settings.lot_number
            return True

        except Exception as ex:
            cs_logger.info(f'Ошибка в (ContractTier: purchase_timing) {ex.args}')
            delay_sleep(settings.delay[0], settings.delay[1])

    def check_lots(self):
        lots_sum = self.contract.functions.saleTokenPurchased().call()
        if lots_sum == self.max_total_purchase:
            cs_logger.info(f'Ноды этого тира закончились!')
            return False
        return True
