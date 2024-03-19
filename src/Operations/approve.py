from src.Helpers.txnHelper import approve_amount
from src.tokens import wETH_token
from src.networks import arbitrum_net
from src.Contracts.tiers import tier_list
from src.logger import cs_logger


def approving(wallets):

    for wallet in wallets:
        cs_logger.info(f'Даем аппрувы для {wallet.address}')
        for tier in tier_list:
            cs_logger.info(f'{tier.title}')
            approve_amount(wallet, tier.contract_address, wETH_token, arbitrum_net, tier.price)
