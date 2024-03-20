from src.Contracts.Contract import ContractTier


tier1 = ContractTier(
    tier=1,
    title='Tier 1',
    contract_address='0xc2BF4eBEbBd692176d08faC51ba7ec3410Af18EC',  # Адрес контракта
    price=125900000000000000,           # Стоимость
    allocation=5000000000000000000,     # параметр publicAllocation
    buy_limit=5,                        # Максимальное количество нод, которое покупаем
    max_total_purchase=314750000000000000000
)

tier2 = ContractTier(
    tier=2,
    title='Tier 2',
    contract_address='0xD19EBA0953e995806e76f5505cD6D8A820909C94',
    price=144800000000000000,
    allocation=10000000000000000000,
    buy_limit=10,
    max_total_purchase=362000000000000000000
)

tier3 = ContractTier(
    tier=3,
    title='Tier 3',
    contract_address='0xF85468AaDD71d2dbC969b4A8Cc2147c1DdD4866d',
    price=166500000000000000,
    allocation=15000000000000000000,
    buy_limit=15,
    max_total_purchase=374625000000000000000
)

tier4 = ContractTier(
    tier=4,
    title='Tier 4',
    contract_address='0x754C9D60d5E877bd24c47FaE05eb670875D47442',
    price=191500000000000000,
    allocation=30000000000000000000,
    buy_limit=30,
    max_total_purchase=215437500000000000000
)

tier5 = ContractTier(
    tier=5,
    title='Tier 5',
    contract_address='0x2EbdcEDE80039bb745C3ee2a18C740346dd6560e',
    price=220200000000000000,
    allocation=50000000000000000000,
    buy_limit=50,
    max_total_purchase=220200000000000000000
)

tier6 = ContractTier(
    tier=6,
    title='Tier 6',
    contract_address='0x213404cAB4e3FF587614daBF7bfB23FEb0354227',
    price=253300000000000000,
    allocation=200000000000000000000,
    buy_limit=100,
    max_total_purchase=253300000000000000000
)

tier7 = ContractTier(
    tier=7,
    title='Tier 7',
    contract_address='0xB503f244C02B9472FE0e49d558Df3A3274E1C38c',
    price=291200000000000000,
    allocation=200000000000000000000,
    buy_limit=200,
    max_total_purchase=254800000000000000000
)

tier8 = ContractTier(
    tier=8,
    title='Tier 8',
    contract_address='0x13e8c714F43C806933E0600880600002186BB924',
    price=334900000000000000,
    allocation=200000000000000000000,
    buy_limit=200,
    max_total_purchase=293037500000000000000
)

tier9 = ContractTier(
    tier=9,
    title='Tier 9',
    contract_address='0x2f2735573c137a57F8cE472D55039beb564Fa489',
    price=385200000000000000,
    allocation=200000000000000000000,
    buy_limit=200,
    max_total_purchase=674100000000000000000
)

tier10 = ContractTier(
    tier=10,
    title='Tier 10',
    contract_address='0x20F0E6560d3B2A3DCd3f6dCbF1182e9bB39C49D5',
    price=442900000000000000,
    allocation=200000000000000000000,
    buy_limit=200,
    max_total_purchase=664350000000000000000
)

tier_list = list()
tier_list.extend([tier1, tier2, tier3, tier4, tier5, tier6, tier7, tier8, tier9, tier10])
