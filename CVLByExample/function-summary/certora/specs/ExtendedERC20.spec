methods {
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
}

// timeout rule
// The user is msg.sender so the amount redeemed goes to it.
// Under the assumptions that totalSupply > 0 and totalAssets > 0, 
// amount redeemed by redeem(shares, receiver, user) is between the amount redeemed by redeem(s1) followed by redeem(s2)
// and this amount + 2.
rule userLossIsLimited(address user, address receiver, uint256 s1, uint256 s2) {
    env e;
    require(receiver != currentContract);
    require(user == e.msg.sender);
    require(totalAssets() > 0);
    require(totalSupply() > 0);
    uint256 shares = require_uint256(s1 + s2);
    require(shares <= balanceOf(e, user));
    require(shares <= totalSupply());

    storage init = lastStorage;

    mathint redeemed1a = redeem(e, s1, receiver, user);
    mathint redeemed1b = redeem(e, s2, receiver, user);
    mathint redeemed2 = redeem(e, shares, receiver, user) at init;

    assert(redeemed2 >= redeemed1a + redeemed1b);
    assert(redeemed2 <= redeemed1a + redeemed1b + 2);
}


