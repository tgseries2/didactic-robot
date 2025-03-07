# config.py

CONFIG = {
    "PRIVATE_KEY": "0xYOUR_PRIVATE_KEY",
    "WALLET_ADDRESS": "0xYOUR_WALLET_ADDRESS",
    "RPC_URL": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    "PRIVATE_RPC_URL": "https://mev.api.blxrbdn.com",  # bloXroute private transactions

    "GAS_LIMIT": 3000000,
    "GAS_PRICE": "50",  # in Gwei

    "DYDX_LENDING_POOL": "0x1e0447b19bb6ecfdae1e4ae1694b0c3659614e4e",  

    "DEX_FACTORIES": {
        "UniswapV2": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5Aa6f",
        "Sushiswap": "0xC0AEe478e3658e2610c5F7A4A2E1777ce9e4f2Ac",
    },

    "DEX_ROUTERS": {
        "UniswapV2": "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        "Sushiswap": "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",
    },

    "TOKEN_PAIRS": [
        ("0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),  # USDC <> WETH
        ("0x6B175474E89094C44Da98b954EedeAC495271d0F", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),  # DAI <> WETH
    ]
}