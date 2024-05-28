import "ETH.spec";
//import "ERC20UtilsSummary.spec";

using main as harness;
using mock as mock;

methods {
    /// permit() data encoding
    function harness.encodeForPermit224(address,address,uint256,uint256,uint8,bytes32,bytes32) external returns (bytes memory) envfree;
    function harness.encodeForPermit256(address,address,uint256,uint256,bool,uint8,bytes32,bytes32) external returns (bytes memory) envfree;
    
    /// approve()
    function mock.approveTo() external returns (address) envfree;
    function mock.approveSuccess() external returns (bool) envfree;
    /// permit()
    function mock.permitOwner() external returns (address) envfree;
    function mock.permitSpender() external returns (address) envfree;
    function mock.permitValue() external returns (uint256) envfree;
    function mock.permitDeadline() external returns (uint256) envfree;
    function mock.permitV() external returns (uint8) envfree;
    function mock.permitR() external returns (bytes32) envfree;
    function mock.permitS() external returns (bytes32) envfree;
    function mock.permitDatahash() external returns (bytes32) envfree;
    function mock.permitSuccess() external returns (bool) envfree;
    /// safeTransfer()
    function mock.safeTransferRecipient() external returns (address) envfree;
    function mock.safeTransferAmount() external returns (uint256) envfree;
    function mock.safeTransferSuccess() external returns (bool) envfree;
    /// safeTransferFrom()
    function mock.safeTransferFromSender() external returns (address) envfree;
    function mock.safeTransferFromRecipient() external returns (address) envfree;
    function mock.safeTransferFromAmount() external returns (uint256) envfree;
    function mock.safeTransferFromSuccess() external returns (bool) envfree;
    /// getBalance()
    function mock.getBalanceAccount() external returns (address) envfree;
    function mock.balance() external returns (uint256) envfree;

    /// DISPATCHERS
    function _.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) external => DISPATCHER(true);
    function _.permit(address,address,uint256,uint256,bool,uint8,bytes32,bytes32) external => DISPATCHER(true);
    function _.transfer(address,uint256) external => DISPATCHER(true);
    function _.transferFrom(address,address,uint256) external => DISPATCHER(true);
    function _.balanceOf(address) external => DISPATCHER(true);
    
    function _._ external => DISPATCH [
        mock.approve(address,uint256),
    ] default NONDET;
}

definition permit224_sig() returns uint32 = 0xd505accf;
    //sig:mock.permit(address,address,uint256,uint256,uint8,bytes32,bytes32).selector;

definition permit256_sig() returns uint32 = 0x8fcbaf0c;
    //sig:mock.permit(address,address,uint256,uint256,bool,uint8,bytes32,bytes32).selector;

definition transfer_sig() returns uint32 = 0xa9059cbb;
    //sig:mock.transfer(address,uint256).selector;

definition transferFrom_sig() returns uint32 = 0x23b872dd;
    //sig:mock.transferFrom(uint256,uint256,address,bytes).selector;

definition balanceOf_sig() returns uint32 = 0x70a08231;
    //sig:mock.balanceOf(address).selector;

definition approve_sig() returns uint32 = 0x095ea7b3;
    //sig:mock.approve(address,uint256).selector;

/// ghost boolean for "function was called".
persistent ghost bool called_permit224;
persistent ghost bool called_permit256;
persistent ghost bool called_transfer;
persistent ghost bool called_transferFrom;
persistent ghost bool called_balanceOf;
persistent ghost bool called_approve;

/// ghost address for function callee.
persistent ghost address callee_token_permit224;
persistent ghost address callee_token_permit256;
persistent ghost address callee_token_transfer;
persistent ghost address callee_token_transferFrom;
persistent ghost address callee_token_balanceOf;
persistent ghost address callee_token_approve;

/// ghost boolean for "permit was successful"
persistent ghost bool permit_succees;

function nullify_ghosts() {
    called_permit224 = false;
    called_permit256 = false;
    called_transfer = false;
    called_transferFrom = false;
    called_balanceOf = false;
    called_approve = false;

    callee_token_permit224 = 0;
    callee_token_permit256 = 0;
    callee_token_transfer = 0;
    callee_token_transferFrom = 0;
    callee_token_balanceOf = 0;
    callee_token_approve = 0;

    permit_succees = false;
}

hook STATICCALL(uint g, address addr, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    if (selector == balanceOf_sig()) {
        called_balanceOf = true;
        callee_token_balanceOf = addr;
    }
}

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    if (selector == transfer_sig()) {
        called_transfer = true;
        callee_token_transfer = addr;
    } else if (selector == transferFrom_sig()) {
        called_transferFrom = true;
        callee_token_transferFrom = addr;
    } else if (selector == permit224_sig()) {
        called_permit224 = true;
        callee_token_permit224 = addr;
        permit_succees = rc > 0;
    } else if (selector == permit256_sig()) {
        called_permit256 = true;
        callee_token_permit256 = addr;
        permit_succees = rc > 0;
    } else if (selector == approve_sig()) {
        called_approve = true;
        callee_token_approve = addr;
    }
}

/// @title Validate data for permit()
rule test_call_through_permit(env e, address token) {
    nullify_ghosts();
    bytes data;
    harness.permit(e, token, data);

    assert permit_succees => called_permit224 || called_permit256;
    assert permit_succees => data.length == 224 || data.length == 256;
    assert permit_succees => token == callee_token_permit224 || token == callee_token_permit256; 
}

/// @title Validate permit() with encoded data (len=224)
rule test_encoded_call_through_permit224(env e, address token) {
    nullify_ghosts();
    address owner;
    address spender;
    uint256 value;
    uint256 deadline;
    uint8 v;
    bytes32 r;
    bytes32 s;
    bytes data = harness.encodeForPermit224(owner, spender, value, deadline, v, r, s);

    harness.permit(e, token, data);
    if(permit_succees) {
        assert mock.permitOwner() == owner;
        assert mock.permitSpender()  == spender;
        assert mock.permitValue() == value;
        assert mock.permitDeadline()  == deadline;
        assert mock.permitV() == v;
        assert mock.permitR() == r;
        assert mock.permitS() == s;
        assert keccak256(data) == mock.permitDatahash();
        assert token == callee_token_permit224;
    }
    else {
        assert !(e.msg.value == 0 && mock.permitSuccess());
    }
}

/// @title Validate permit() with encoded data (len=256)
rule test_encoded_call_through_permit256(env e, address token) {
    nullify_ghosts();
    address owner;
    address spender;
    uint256 value;
    uint256 deadline;
    bool allowed;
    uint8 v;
    bytes32 r;
    bytes32 s;
    bytes data = harness.encodeForPermit256(owner, spender, value, deadline, allowed, v, r, s);

    harness.permit(e, token, data);
    if(permit_succees) {
        assert mock.permitOwner() == owner;
        assert mock.permitSpender()  == spender;
        assert mock.permitValue() == value;
        assert mock.permitDeadline()  == deadline;
        assert mock.permitV() == v;
        assert mock.permitR() == r;
        assert mock.permitS() == s;
        assert keccak256(data) == mock.permitDatahash();
        assert token == callee_token_permit256;
    }
    else {
        assert !(e.msg.value == 0 && mock.permitSuccess());
    }
}

/// @title Validate data for transferFrom()
rule test_call_through_transferFrom(env e, address token) {
    nullify_ghosts();
    address sender;
    address recipient;
    uint256 amount;
    bool result = harness.safeTransferFrom(e, token, sender, recipient, amount);

    assert called_transferFrom;
    assert mock.safeTransferFromSuccess();
    assert token == callee_token_transferFrom;
    assert sender == mock.safeTransferFromSender();
    assert recipient == mock.safeTransferFromRecipient();
    assert amount == mock.safeTransferFromAmount();
    satisfy token != ETH();
}

/// @title Validate data for approve()
rule test_call_through_approve(env e, address token) {
    nullify_ghosts();
    address to;
    harness.approve(e, token, to);

    assert called_approve;
    assert mock == callee_token_approve => mock.approveSuccess();
    assert mock == callee_token_approve => token == callee_token_approve;
    assert mock == callee_token_approve => to == mock.approveTo();
    satisfy token != ETH() && mock == callee_token_approve;
}

/// @title Validate data for transfer()
rule test_call_through_transfer(env e, address token) {
    nullify_ghosts();
    address recipient;
    uint256 amount;
    bool result = harness.safeTransfer(e, token, recipient, amount);

    assert token != ETH() => mock.safeTransferSuccess();
    assert called_transfer <=> (token != ETH());
    assert token == callee_token_transfer || token == ETH();
    assert token != ETH() => recipient == mock.safeTransferRecipient();
    assert token != ETH() => amount == mock.safeTransferAmount();
    satisfy token != ETH();
}

/// @title Validate revert condition for transfer()
rule test_safeTransfer_revert(env e, address token) {
    nullify_ghosts();
    require e.msg.value == 0;
    require token != ETH();
    address recipient;
    uint256 amount;
    harness.safeTransfer@withrevert(e, token, recipient, amount);
    bool reverted = lastReverted;

    assert reverted => !mock.safeTransferSuccess();
    satisfy reverted;
}

/// @title Validate revert condition for transferFrom()
rule test_safeTransferFrom_revert(env e, address token) {
    nullify_ghosts();
    require e.msg.value == 0;
    address sender;
    address recipient;
    uint256 amount;
    harness.safeTransferFrom@withrevert(e, token, sender, recipient, amount);
    bool reverted = lastReverted;

    assert reverted => !mock.safeTransferFromSuccess();
    satisfy reverted;
}

/// @title Validate data for balanceOf()
rule test_call_through_balanceOf(env e, address token) {
    nullify_ghosts();
    address account;
    uint256 result = harness.getBalance(e, token, account);

    assert called_balanceOf <=> token != ETH();
    assert token == callee_token_balanceOf || token == ETH();
    assert token != ETH() => result == mock.balance();
    assert token == ETH() => result == nativeBalances[account];
    assert token != ETH() => account == mock.getBalanceAccount();
    satisfy token != ETH();
}

/// @title Test for isETH()
rule test_isETH(env e, address token) {
    uint256 amount;
    uint256 isETH_ = isETH(e, token, amount);

    assert token == ETH() => isETH_ == 1;
    assert token != ETH() => isETH_ == 0;
}