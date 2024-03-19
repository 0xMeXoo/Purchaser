from web3 import Web3
import settings


class Network(object):
    def __init__(self, name, rpc, oracle_address):
        self.name = name
        self.web3 = Web3(Web3.HTTPProvider(rpc))
        self.oracle_address = oracle_address
        self.chain_id = self.web3.eth.chain_id


arbitrum_net = Network(
    name='Arbitrum',
    rpc=settings.arbitrum_rpc,
    oracle_address='None'
)
