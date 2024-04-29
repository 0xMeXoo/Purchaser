from src.Contracts.Contract import ContractTier


tier1 = ContractTier(
    tier=1,
    title='Tier 1',
    contract_address='0xc9110F53C042a61d1b0f95342e61d62714F8A2E6',  # Адрес контракта
    price=81300000000000000,             # Стоимость
    allocation=10000000000000000000,     # параметр publicAllocation
    buy_limit=10,                        # Максимальное количество нод, которое покупаем
    max_total_purchase=314750000000000000000
)

tier2 = ContractTier(
    tier=2,
    title='Tier 2',
    contract_address='0x11B2669a07A0D17555a7Ab54C0C37f5c8655A739',
    price=91500000000000000,
    allocation=10000000000000000000,
    buy_limit=10,
    max_total_purchase=362000000000000000000
)

tier3 = ContractTier(
    tier=3,
    title='Tier 3',
    contract_address='0x58078e429a99478304a25B2Ab03ABE79199bE618',
    price=103000000000000000,
    allocation=20000000000000000000,
    buy_limit=20,
    max_total_purchase=374625000000000000000
)

tier4 = ContractTier(
    tier=4,
    title='Tier 4',
    contract_address='0x2E89CAE8F6532687b015F4BA320F57c77920B451',
    price=115800000000000000,
    allocation=20000000000000000000,
    buy_limit=20,
    max_total_purchase=215437500000000000000
)

tier5 = ContractTier(
    tier=5,
    title='Tier 5',
    contract_address='0x396Ea0670e3112BC344791Ee7931a5A55E0bDBd1',
    price=130300000000000000,
    allocation=40000000000000000000,
    buy_limit=40,
    max_total_purchase=220200000000000000000
)

tier6 = ContractTier(
    tier=6,
    title='Tier 6',
    contract_address='0xB08772AA562ED5d06B34fb211c51EC92debF7b26',
    price=146600000000000000,
    allocation=60000000000000000000,
    buy_limit=5,
    max_total_purchase=253300000000000000000
)

tier7 = ContractTier(
    tier=7,
    title='Tier 7',
    contract_address='0x772eDA6C5aACC61771F9b5f9423D381D311a7018',
    price=164900000000000000,
    allocation=80000000000000000000,
    buy_limit=5,
    max_total_purchase=254800000000000000000
)

tier8 = ContractTier(
    tier=8,
    title='Tier 8',
    contract_address='0x4842547944832Fe833af677BFDB157dEf391e685',
    price=185500000000000000,
    allocation=100000000000000000000,
    buy_limit=5,
    max_total_purchase=293037500000000000000
)

tier9 = ContractTier(
    tier=9,
    title='Tier 9',
    contract_address='0x3F0d099120Bf804606835DEFa6dA1A5E784328D6',
    price=208700000000000000,
    allocation=250000000000000000000,
    buy_limit=5,
    max_total_purchase=674100000000000000000
)

tier10 = ContractTier(
    tier=10,
    title='Tier 10',
    contract_address='0xe0D06d430b0a44e6444f5f0736dC113afe5b636A',
    price=234800000000000000,
    allocation=500000000000000000000,
    buy_limit=5,
    max_total_purchase=664350000000000000000
)

tier_list = list()
tier_list.extend([tier1, tier2, tier3, tier4, tier5])  # Первые 5 тиров
#tier_list.extend([tier6, tier7, tier8, tier9, tier10])
