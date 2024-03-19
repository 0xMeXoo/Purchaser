
class Wallet(object):
    def __init__(self, key, address):
        self.key = key
        self.address = address
        self.txn_num = {
            'Tier 1': 0,
            'Tier 2': 0,
            'Tier 3': 0,
            'Tier 4': 0,
            'Tier 5': 0,
            'Tier 6': 0,
            'Tier 7': 0,
            'Tier 8': 0,
            'Tier 9': 0,
            'Tier 10': 0,
        }
