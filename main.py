# main.py

import time
from arbitrage import execute_flash_loan
from config import CONFIG

AMOUNT_TO_BORROW = Web3.toWei(10, "ether")  # Example: 10 ETH

while True:
    print("Checking for arbitrage opportunities...")
    execute_flash_loan(CONFIG["TOKEN_A"], AMOUNT_TO_BORROW)
    time.sleep(5)  # Wait before checking again
