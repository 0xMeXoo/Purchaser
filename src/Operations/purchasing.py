import settings
from src.Contracts.tiers import tier_list
from src.logger import cs_logger


def purchase_lot(wallet):
    tier = tier_list[settings.tier - 1]
    cs_logger.info(f'Кошелек   {wallet.address}  |  Tier {tier.tier}')
    if settings.no_gas_check == 1:
        tier.purchase_timing(wallet)
    while tier.buy_limit > wallet.txn_num[tier.title]:
        tier.purchase(wallet)
        lots_remain = tier.check_lots()
        if lots_remain is False:
            return
