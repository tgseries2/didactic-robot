# utils.py

from web3 import Web3
import requests
from config import CONFIG

web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

# Factory & Pair ABIs
UNISWAP_FACTORY_ABI = '[{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]'
PAIR_ABI = '[{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]'

def get_all_pairs(dex_factory):
    """Fetch all token pairs from a DEX factory."""
    factory_contract = web3.eth.contract(address=dex_factory, abi=UNISWAP_FACTORY_ABI)
    total_pairs = factory_contract.functions.allPairsLength().call()

    token_pairs = []
    for i in range(total_pairs):
        pair_address = factory_contract.functions.allPairs(i).call()
        pair_contract = web3.eth.contract(address=pair_address, abi=PAIR_ABI)

        token0 = pair_contract.functions.token0().call()
        token1 = pair_contract.functions.token1().call()

        token_pairs.append((token0, token1))
    return token_pairs

def send_private_transaction(signed_tx):
    """Submit a transaction privately via bloXroute/Eden."""
    private_rpc = CONFIG["PRIVATE_RPC_URL"]

    payload = {
        "jsonrpc": "2.0",
        "method": "eth_sendPrivateTransaction",
        "params": [{"tx": signed_tx.rawTransaction.hex()}],
        "id": 1
    }

    response = requests.post(private_rpc, json=payload).json()
    return response.get("result", "TX Failed")
