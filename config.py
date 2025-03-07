# config.py

CONFIG = {
    "PRIVATE_KEY": "your_private_key_here",
    "WALLET_ADDRESS": "your_wallet_address_here",
    "RPC_URL": "https://mainnet.infura.io/v3/your_project_id",
    "GAS_LIMIT": 3000000,
    "GAS_PRICE": "50",  # In Gwei

    # DEX Addresses
    "UNISWAP_ROUTER": "0xE592427A0AEce92De3Edee1F18E0157C05861564",
    "SUSHISWAP_ROUTER": "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",

    # Token Addresses (Example: WETH & USDC)
    "TOKEN_A": "0xC02aaa39b223FE8D0A0e5C4F27eAD9083C756Cc2",  # WETH
    "TOKEN_B": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48",  # USDC

    # Flash Loan Provider (dYdX)
    "DYDX_LENDING_POOL": "0x1e0447b19bb6ecfdae1e4ae1694b0c3659614e4e"
}
