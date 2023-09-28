// Vat.spec

methods {
    function debt() external returns (uint256) envfree;
    function vice() external returns (uint256) envfree;
}

// sumOfVaultDebtGhost gives the current sum over all debt assigned to a vault.
ghost sumOfVaultDebtGhost() returns uint256 {
    // Here we state that the sum is 0 before contructor.
    init_state axiom sumOfVaultDebtGhost() == 0;
}

// tracking the rate.
ghost mapping(bytes32 => uint256) rateGhost {
    init_state axiom forall bytes32 ilk. rateGhost[ilk] == 0;
}

// Tracking the sum over “normalized” debt for a given collateral type (“ilk”).
ghost mapping(bytes32 => uint256) ArtGhost {
    init_state axiom forall bytes32 ilk. ArtGhost[ilk] == 0;
}

hook Sload uint256 v currentContract.ilks[KEY bytes32 ilk].(offset 0) STORAGE {
    require ArtGhost[ilk] == v;
}

// Updating ArtGhost in sync with sumOfVaultDebtGhost.
hook Sstore currentContract.ilks[KEY bytes32 ilk].(offset 0) uint256 newArt (uint256 oldArt) STORAGE {
    havoc sumOfVaultDebtGhost assuming to_mathint(sumOfVaultDebtGhost@new()) == to_mathint(sumOfVaultDebtGhost@old()) + 
    to_mathint((newArt * rateGhost[ilk]) - (oldArt * rateGhost[ilk]));
    ArtGhost[ilk] = newArt;
}

hook Sload uint256 v currentContract.ilks[KEY bytes32 ilk].(offset 32) STORAGE {
    require rateGhost[ilk] == v;
}

// Updating RateGhost in sync with sumOfVaultDebtGhost.
hook Sstore currentContract.ilks[KEY bytes32 ilk].(offset 32) uint256 newRate (uint256 oldRate) STORAGE {
    havoc sumOfVaultDebtGhost assuming to_mathint(sumOfVaultDebtGhost@new()) == 
        to_mathint(sumOfVaultDebtGhost@old() + (ArtGhost[ilk] * newRate) - (ArtGhost[ilk] * oldRate));
    rateGhost[ilk] = newRate;
}


// DAI is backed by debt. Debt is either assigned to a Vault, meaning it is associated with a lien against some collateral asset,
// or it is “unbacked” (also: “bad”), meaning it is the protocol’s (i.e., MKR holders’) responsibility. 
// This invariant states that these two sources of debt, when added, should equal the sum of all DAI balances. 
// vice is the total bad debt.
// debt is the sum over all DAI balances.
invariant fundamental_equation_of_dai()
   to_mathint(debt()) == to_mathint(vice() + sumOfVaultDebtGhost())
   filtered { f -> !f.isFallback }
