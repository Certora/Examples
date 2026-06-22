methods {
		function getCurrentManager(uint256 fundId) external returns (address) envfree;
		function getPendingManager(uint256 fundId) external returns (address) envfree;
		function isActiveManager(address a) external returns (bool) envfree;
}

invariant ManagerZeroIsNotActive()
        !isActiveManager(0);

rule uniqueManager(uint256 fundId1, uint256 fundId2, method f) {
	require fundId1 != fundId2;
    requireInvariant ManagerZeroIsNotActive();
    require getCurrentManager(fundId1) != 0 => isActiveManager(getCurrentManager(fundId1));
	require getCurrentManager(fundId2) != 0 => isActiveManager(getCurrentManager(fundId2));
	require getCurrentManager(fundId1) != getCurrentManager(fundId2) ;
				
	env e;
	if (f.selector == sig:claimManagement(uint256).selector)
	{
		uint256 id;
        /// Since there is symetry between fundId1 and funcdId2 and they are havoced it is enough to have require id == fundId1
		require id == fundId1 || id == fundId2;
		claimManagement(e, id);  
	}
	else {
		calldataarg args;
		f(e,args);
	}
	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert getCurrentManager(fundId1) != 0 => isActiveManager(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert getCurrentManager(fundId2) != 0 => isActiveManager(getCurrentManager(fundId2)), "manager of fund2 is not active";
}


rule uniqueManagerWeak(uint256 fundId1, uint256 fundId2, method f) {
	require fundId1 != fundId2;
    requireInvariant ManagerZeroIsNotActive();
    require getCurrentManager(fundId1) != 0 && isActiveManager(getCurrentManager(fundId1));
	require getCurrentManager(fundId2) != 0 && isActiveManager(getCurrentManager(fundId2));
	require getCurrentManager(fundId1) != getCurrentManager(fundId2) ;
				
	env e;
	if (f.selector == sig:claimManagement(uint256).selector)
	{
		uint256 id;
		require id == fundId1 || id == fundId2;
		claimManagement(e, id);  
	}
	else {
		calldataarg args;
		f(e,args);
	}
	assert getCurrentManager(fundId1) != getCurrentManager(fundId2), "managers not different";
	assert getCurrentManager(fundId1) != 0 && isActiveManager(getCurrentManager(fundId1)), "manager of fund1 is not active";
	assert getCurrentManager(fundId2) != 0 && isActiveManager(getCurrentManager(fundId2)), "manager of fund2 is not active";
}

/// This is a taughtology because by the require, it is never the case that newManager== other && newManager == manager.
rule tautology(uint256 fundId, method f) { 
	address manager =  getCurrentManager(fundId);
	address other;
	require other != manager;
	env e;
	calldataarg args;
	f(e,args);
	address newManager = getCurrentManager(fundId);
	assert ( newManager!= other || newManager != manager);
}

rule mistake(uint256 fundId, address pending ) {
	address manager;
	env e;
	require manager != pending ;
	require pending != 0;
	claimManagement(e, fundId );
	// the following is wrong, the engineer wanted to reason about the pending before  claimManagement 
	assert getPendingManager(fundId) == pending =>  getCurrentManager(fundId)== pending;
	// check that indeed the hypothesis is always false 
	// assert( getPendingManager(fundId) != pending);
}	
	
