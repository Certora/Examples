import "ETH.spec";

using DummyERC20A as erc20A;
using DummyERC20B as erc20B;
using DummyERC20C as erc20C;

methods {
    function ERC20Utils.getBalance(address token, address account) internal returns (uint256) with (env e) => dispatchBalanceOf(e, token, account);
    function ERC20Utils.safeTransfer(address token, address recipient, uint256 amount) internal returns (bool) with (env e) => dispatchTransfer(e, token, recipient, amount);
    function ERC20Utils.safeTransferFrom(address token, address sender, address recipient, uint256 amount) internal returns (bool) with (env e) => dispatchTransferFrom(e, token, sender, recipient, amount);
    function ERC20Utils.approve(address token, address to) internal with (env e) => dispatchApprove(e, token, to);
    function ERC20Utils.permit(address token, bytes calldata data) internal with (env e) => dispatchPermit(e, token, data);
    function ERC20Utils.isETH(address token, uint256 amount) internal returns (uint256) with (env e) => isETHSummary(token, amount, e.msg.value);
}

function isETHSummary(address token, uint256 amount, uint256 msgvalue) returns uint256 {
    if (token == ETH()) {
        require msgvalue == amount;
        return 1;
    } else {
        require msgvalue == 0;
    }
    return 0;
}

function dispatchBalanceOf(env e, address token, address account) returns uint256 {
    env ed; /// Dispatch environment
    require ed.msg.sender == currentContract;
    require ed.block.timestamp == e.block.timestamp; 
    require ed.msg.value == 0;
    if (token == erc20A) {
        return erc20A.balanceOf(ed, account);
    } else if (token == erc20B) {
        return erc20B.balanceOf(ed, account);
    } else if(token == erc20C) {
        return erc20C.balanceOf(ed, account);
    } else if (token == ETH()) {
        return nativeBalances[account];
    } else {
        require false; // optimistic
    }
    return 0;
}

function dispatchTransfer(env e, address token, address recipient, uint256 amount) returns bool {
    env ed; /// Dispatch environment
    require ed.msg.sender == currentContract;
    require ed.block.timestamp == e.block.timestamp; 
    require ed.msg.value == 0;
    if (token == erc20A) {
        return erc20A.transfer(ed, recipient, amount);
    } else if (token == erc20B) {
        return erc20B.transfer(ed, recipient, amount);
    } else if (token == erc20C) {
        return erc20C.transfer(ed, recipient, amount);
    } else {
        require false; // optimistic
    }
    return true;
}

function dispatchTransferFrom(env e, address token, address sender, address recipient, uint256 amount) returns bool {
    env ed; /// Dispatch environment
    require ed.msg.sender == currentContract;
    require ed.block.timestamp == e.block.timestamp; 
    require ed.msg.value == 0;
    if (token == erc20A) {
        return erc20A.transferFrom(ed, sender, recipient, amount);
    } else if (token == erc20B) {
        return erc20B.transferFrom(ed, sender, recipient, amount);
    } else if (token == erc20C) {
        return erc20C.transferFrom(ed, sender, recipient, amount);
    } else {
        require false; // optimistic
    }
    return true;
}

function dispatchApprove(env e, address token, address to) {
    env ed; /// Dispatch environment
    require ed.msg.sender == currentContract;
    require ed.block.timestamp == e.block.timestamp; 
    require ed.msg.value == 0;
    if (token == erc20A) {
        erc20A.approve(ed, to, max_uint256);
    } else if (token == erc20B) {
        erc20B.approve(ed, to, max_uint256);
    } else if (token == erc20C) {
        erc20C.approve(ed, to, max_uint256);
    } else {
        require false; // optimistic
    }
}

function dispatchPermit(env e, address token, bytes data) {
    env ed; /// Dispatch environment
    require ed.msg.sender == currentContract;
    require ed.block.timestamp == e.block.timestamp; 
    require ed.msg.value == 0;
    require data.length == 224; /// Assume only standard permit selector.
    if (token == erc20A) {
        erc20A.permit(ed, data);
    } else if (token == erc20B) {
        erc20B.permit(ed, data);
    } else if (token == erc20C) {
        erc20C.permit(ed, data);
    } else {
        require false; // optimistic
    }
}
