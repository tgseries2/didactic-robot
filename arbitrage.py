# arbitrage.py

from web3 import Web3
from config import CONFIG
from utils import is_profitable_trade

web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

def execute_flash_loan(token, amount):
    """Requests a flash loan from dYdX and executes arbitrage."""
    if not is_profitable_trade(CONFIG["TOKEN_A"], CONFIG["TOKEN_B"], amount):
        print("No profitable arbitrage opportunity found.")
        return
    
    flash_loan_contract = web3.eth.contract(address=CONFIG["DYDX_LENDING_POOL"], abi=FLASH_LOAN_ABI)
    
    tx = flash_loan_contract.functions.initiateFlashLoan(
        CONFIG["TOKEN_A"], amount
    ).build_transaction({
        "from": CONFIG["WALLET_ADDRESS"],
        "gas": CONFIG["GAS_LIMIT"],
        "gasPrice": web3.toWei(CONFIG["GAS_PRICE"], "gwei"),
        "nonce": web3.eth.get_transaction_count(CONFIG["WALLET_ADDRESS"]),
    })

    signed_tx = web3.eth.account.sign_transaction(tx, CONFIG["PRIVATE_KEY"])
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"Flash loan executed: {web3.toHex(tx_hash)}")
