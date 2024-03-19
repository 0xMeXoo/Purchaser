from src.Helpers.txnHelper import read_wallets
import settings
from src.Operations.approve import approving
from src.Operations.purchasing import purchase_lot
from src.logger import cs_logger


wallets = read_wallets()


def main():
    if settings.approving_switch == 1:
        approving(wallets)

    if settings.purchase_switch == 1:
        purchase_lot(wallets[0])


main()
cs_logger.info(f'')
cs_logger.info(f'Нажмите Enter для выхода...')
input()
cs_logger.info(f'Выход...')
