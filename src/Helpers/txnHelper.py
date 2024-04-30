from random import uniform, randint
import settings
from time import sleep
from src.logger import cs_logger
from web3 import Web3
from src.Wallet import Wallet


def get_gas_price(network):
    gas_price_mult = round(uniform(settings.gas_price_mult[0], settings.gas_price_mult[1]), 3)
    gas_price = int(network.web3.eth.gas_price * gas_price_mult)
    return gas_price


def get_priority(network):
    priority_mult = round(uniform(settings.priority_mult[0], settings.priority_mult[1]), 3)
    priority = int(network.web3.eth.max_priority_fee * priority_mult)
    return priority


def get_txn_dict(address, network, value=0, gas=5_000_000):
    nonce = network.web3.eth.get_transaction_count(address)
    dict_transaction = None

    if settings.txn_type == 0:
        gas_price = get_gas_price(network)
        dict_transaction = {
            'chainId': network.chain_id,
            'from': address,
            'value': value,
            'gas': gas,
            'gasPrice': gas_price,
            'nonce': nonce,
        }
    elif settings.txn_type == 2:
        gas_price = get_gas_price(network)
        max_priority = network.web3.to_wei(0.025, 'gWei')
        dict_transaction = {
            'chainId': network.chain_id,
            'from': address,
            'value': value,
            'gas': gas,
            'maxFeePerGas': gas_price,
            'maxPriorityFeePerGas': max_priority,
            'nonce': nonce,
        }
    return dict_transaction


def check_tx_status(txn_hash, net, sec=1):
    status = None
    while status is None:
        txn_done = net.web3.eth.wait_for_transaction_receipt(txn_hash, 60 * 5)
        status = txn_done.get('status')
        sleep(sec)
    return status


def approve_amount(wallet, spender_address, token, net, token_amount, approve_sum=2 ** 256 - 1):
    try:
        allowance = token.contract.functions.allowance(wallet.address, spender_address).call()
        if allowance < token_amount:
            cs_logger.info(f'Даем разрешение смартконтракту использовать токен')

            dict_transaction = get_txn_dict(wallet.address, net)
            txn_approve = token.contract.functions.approve(
                spender_address,
                approve_sum
            ).build_transaction(dict_transaction)

            estimate_gas = check_estimate_gas(txn_approve, net)
            txn_approve['gas'] = estimate_gas

            txn_hash, txn_status = exec_txn(wallet.key, txn_approve, net)
            cs_logger.info(f'Hash аппрува: {txn_hash}')
            return txn_hash
    except Exception as ex:
        cs_logger.info(f'Ошибка в (txnHelper: approve_amount): {ex.args}')


def check_estimate_gas(txn, net, mult_on=True):
    try:
        if mult_on is False:
            estimate_gas = net.web3.eth.estimate_gas(txn)
            return estimate_gas
        gas_mult = round(uniform(settings.gas_mult[0], settings.gas_mult[1]), 3)
        estimate_gas = int(net.web3.eth.estimate_gas(txn) * gas_mult)
        return estimate_gas
    except Exception as ex:
        return f'Ошибка в (txnHelper: check_estimate_gas): {ex.args}'


def exec_txn(private_key, txn, net):
    try:
        if settings.test_mode == 0:
            signed_txn = net.web3.eth.account.sign_transaction(txn, private_key)
            txn_hash = net.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            # check_tx_status(txn_hash, net, 3)
            return txn_hash.hex(), True
        if settings.test_mode == 1:
            txn_hash = 'Test'  # Для тестов
            return txn_hash, True
    except Exception as ex:
        return f'Ошибка в (exec_txn): {ex.args}', False


def delay_sleep(min_delay, max_delay):
    delay = randint(min_delay, max_delay)
    sleep(delay)
    return delay


def read_wallets():
    wallet_list = list()
    wallet_info = settings.wallets.read().splitlines()
    w3 = Web3()
    for wl in wallet_info:
        key = wl
        address = w3.eth.account.from_key(key).address
        wlt = Wallet(key, address)
        wallet_list.append(wlt)
    return wallet_list
