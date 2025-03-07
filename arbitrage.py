# arbitrage.py

from web3 import Web3
import time
from config import CONFIG
from utils import get_reserves, send_private_transaction

web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

def calculate_profit(reserve_in, reserve_out, amount):
    """Calculate arbitrage profit."""
    if reserve_in == 0 or reserve_out == 0:
        return 0
    return (amount * reserve_out / reserve_in) - amount

def get_best_arbitrage():
    """Find best arbitrage opportunities."""
    best_profit = 0
    best_trade = None

    for dex_in, factory_in in CONFIG["DEX_FACTORIES"].items():
        for dex_out, factory_out in CONFIG["DEX_FACTORIES"].items():
            if dex_in == dex_out:
                continue

            for token_a, token_b in CONFIG["TOKEN_PAIRS"]:
                reserves_in = get_reserves(factory_in, token_a, token_b)
                reserves_out = get_reserves(factory_out, token_a, token_b)

                profit = calculate_profit(reserves_in[0], reserves_out[1], 1_000)  
                if profit > best_profit:
                    best_profit = profit
                    best_trade = (dex_in, dex_out, token_a, token_b)

    return best_trade, best_profit

def execute_arbitrage():
    """Execute arbitrage if profitable."""
    best_trade, best_profit = get_best_arbitrage()

    if best_trade and best_profit > 0:
        dex_in, dex_out, token_a, token_b = best_trade

        nonce = web3.eth.get_transaction_count(CONFIG["WALLET_ADDRESS"])
        chain_id = web3.eth.chain_id  

        tx = {
            "to": dex_in,
            "gas": CONFIG["GAS_LIMIT"],
            "gasPrice": Web3.toWei(CONFIG["GAS_PRICE"], "gwei"),
            "value": 0,
            "nonce": nonce,
            "chainId": chain_id,
            "data": "0x"
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key=CONFIG["PRIVATE_KEY"])
        tx_hash = send_private_transaction(signed_tx)

        if tx_hash:
            print(f"✅ Arbitrage executed! TX Hash: {tx_hash}")
        else:
            print("❌ Arbitrage TX failed.")
    else:
        print("❌ No profitable arbitrage found.")

if __name__ == "__main__":
    execute_arbitrage()