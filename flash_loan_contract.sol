// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline
    ) external returns (uint[] memory amounts);
}

interface IDYDXFlashLoan {
    function flashLoan(address token, uint amount) external;
}

contract FlashLoanArbitrage {
    address private owner;
    address private uniswapRouter;
    address private sushiswapRouter;
    address private dydxLendingPool;

    constructor(address _uniswap, address _sushiswap, address _dydx) {
        owner = msg.sender;
        uniswapRouter = _uniswap;
        sushiswapRouter = _sushiswap;
        dydxLendingPool = _dydx;
    }

    function executeArbitrage(address token, uint amount) external {
        require(msg.sender == owner, "Not authorized");
        IDYDXFlashLoan(dydxLendingPool).flashLoan(token, amount);
    }

    function onFlashLoanReceived(address token, uint amount) external {
        // Swap on Uniswap
        address;
        path[0] = token;
        path[1] = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48; // USDC

        IUniswapV2Router(uniswapRouter).swapExactTokensForTokens(
            amount, 1, path, address(this), block.timestamp + 15
        );

        // Swap back on Sushiswap
        IUniswapV2Router(sushiswapRouter).swapExactTokensForTokens(
            amount, 1, path, address(this), block.timestamp + 15
        );

        // Repay flash loan
        payable(dydxLendingPool).transfer(amount);
    }

    receive() external payable {}
}
