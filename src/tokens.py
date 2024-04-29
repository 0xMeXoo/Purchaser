from web3 import Web3
from src.ABIs import wETH_ABI
from src.networks import zksync_era as network
import settings


class Token(object):
    def __init__(self, token_name, token_address, contract):
        self.name = token_name
        self.address = token_address
        self.contract = contract


wETH_token = Token(
    token_name='wETH',
    token_address=settings.weth_address,
    contract=network.web3.eth.contract(Web3.to_checksum_address(settings.weth_address), abi=wETH_ABI)
)
