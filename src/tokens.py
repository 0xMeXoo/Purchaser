from web3 import Web3
from src.ABIs import wETH_ABI
from src.networks import arbitrum_net


class Token(object):
    def __init__(self, token_name, token_address, contract):
        self.name = token_name
        self.address = token_address
        self.contract = contract


wETH_token = Token(
    token_name='wETH',
    token_address='0x82aF49447D8a07e3bd95BD0d56f35241523fBab1',
    contract=arbitrum_net.web3.eth.contract(Web3.to_checksum_address('0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'),
                                            abi=wETH_ABI)
)
