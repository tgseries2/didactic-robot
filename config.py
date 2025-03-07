# config.py

CONFIG = {
    "PRIVATE_KEY": "your_private_key_here",
    "WALLET_ADDRESS": "your_wallet_address_here",
    "RPC_URL": "https://mainnet.infura.io/v3/your_project_id",

    # Private Transaction Submission
    "PRIVATE_RPC_URL": "https://mev.api.blxrbdn.com",  # bloXroute BDN

    # Gas Settings
    "GAS_LIMIT": 3000000,
    "GAS_PRICE": "50",  # In Gwei

    # Flash Loan Provider
    "DYDX_LENDING_POOL": "0x1e0447b19bb6ecfdae1e4ae1694b0c3659614e4e",

    # DEX Factory Contracts (Used to fetch all token pairs dynamically)
    "DEX_FACTORIES": {
        "UniswapV2": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5Aa6f",
        "Sushiswap": "0xC0AEe478e3658e2610c5F7A4A2E1777ce9e4f2Ac",
        "Balancer": "0xBA12222222228d8Ba445958a75a0704d566BF2C8",
    },

    # DEX Routers (For executing trades)
    "DEX_ROUTERS": {
        "UniswapV2": "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        "Sushiswap": "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",
        "Curve": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5Aa6f",
        "Balancer": "0xBA12222222228d8Ba445958a75a0704d566BF2C8",
    }
}
