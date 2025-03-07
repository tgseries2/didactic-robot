# utils.py

from web3 import Web3
import requests
from config import CONFIG

web3 = Web3(Web3.HTTPProvider(CONFIG["RPC_URL"]))

PAIR_ABI = '''
[
    {"constant":true,"inputs":[],"name":"getReserves","outputs":[{"name":"_reserve0","type":"uint112"},{"name":"_reserve1","type":"uint112"},{"name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"}
]
'''

def get_reserves(factory, token_a, token_b):
    """Fetch token reserves from a DEX pair contract."""
    sorted_tokens = sorted([token_a, token_b])  # Sort for correct order
    salt = Web3.solidityKeccak(["address", "address"], sorted_tokens)
    
    pair_address = Web3.toChecksumAddress(
        Web3.keccak(hexstr=factory + salt.hex())[12:]
    )

    pair_contract = web3.eth.contract(address=pair_address, abi=PAIR_ABI)

    try:
        reserves = pair_contract.functions.getReserves().call()
        return reserves
    except Exception as e:
        print(f"❌ Error fetching reserves: {e}")
        return 0, 0

def send_private_transaction(signed_tx):
    """Submit a transaction privately via bloXroute."""
    private_rpc = CONFIG["PRIVATE_RPC_URL"]
    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_sendRawTransaction",
        "params": [signed_tx.rawTransaction.hex()],
        "id": 1
    }

    response = requests.post(private_rpc, json=payload).json()
    if "result" in response:
        return response["result"]
    else:
        print(f"❌ Private TX failed: {response}")
        return None