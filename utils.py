# utils.py

from web3 import Web3
from config import CONFIG

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

def get_token_reserves(dex_router, token_a, token_b):
    """Fetches token reserves from the given DEX router."""
    router_contract = web3.eth.contract(address=dex_router, abi=UNISWAP_ABI)
    reserves = router_contract.functions.getReserves(token_a, token_b).call()
    return reserves

def calculate_profit(reserve_in, reserve_out, amount_in):
    """Calculates potential profit from arbitrage trade."""
    amount_out = (amount_in * reserve_out) / (reserve_in + amount_in)
    return amount_out - amount_in

def is_profitable_trade(token_a, token_b, amount):
    """Checks if an arbitrage opportunity exists between two DEXes."""
    uni_reserves = get_token_reserves(CONFIG["UNISWAP_ROUTER"], token_a, token_b)
    sushi_reserves = get_token_reserves(CONFIG["SUSHISWAP_ROUTER"], token_a, token_b)

    profit = calculate_profit(uni_reserves[0], sushi_reserves[1], amount)
    return profit > 0
