# arbitrage.py

from web3 import Web3
from config import CONFIG
from utils import get_all_pairs, send_private_transaction

web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

def get_best_arbitrage():
    """Find best arbitrage opportunities across all DEXes."""
    best_profit = 0
    best_trade = None

    for dex_factory in CONFIG["DEX_FACTORIES"].values():
        token_pairs = get_all_pairs(dex_factory)

        for token_a, token_b in token_pairs:
            for dex_in in CONFIG["DEX_ROUTERS"].values():
                for dex_out in CONFIG["DEX_ROUTERS"].values():
                    if dex_in == dex_out:
                        continue

                    reserves_in = get_reserves(dex_in, token_a, token_b)
                    reserves_out = get_reserves(dex_out, token_a, token_b)

                    profit = calculate_profit(reserves_in[0], reserves_out[1], 1_000)  # Test with 1000 tokens
                    if profit > best_profit:
                        best_profit = profit
                        best_trade = (dex_in, dex_out, token_a, token_b)

    return best_trade, best_profit

def execute_arbitrage():
    """Execute arbitrage if profitable."""
    best_trade, best_profit = get_best_arbitrage()

    if best_trade and best_profit > 0:
        dex_in, dex_out, token_a, token_b = best_trade

        # Construct arbitrage TX
        tx = {
            "to": dex_in,
            "gas": CONFIG["GAS_LIMIT"],
            "gasPrice": Web3.toWei(CONFIG["GAS_PRICE"], "gwei"),
            "value": 0,
            "data": "0x"  # TODO: Encode swap transaction data
        }
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=CONFIG["PRIVATE_KEY"])
        tx_hash = send_private_transaction(signed_tx)

        print(f"Arbitrage executed! TX Hash: {tx_hash}")
    else:
        print("No profitable arbitrage found.")

if __name__ == "__main__":
    execute_arbitrage()
