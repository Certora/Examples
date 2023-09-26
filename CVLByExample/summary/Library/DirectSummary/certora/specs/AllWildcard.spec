/**
 * Every function being called (from solidity) is given its a summarization using a wildcard.
 */
methods {
    // functions declared in TestLibrary
    function _.calleeInternal()                            internal => ALWAYS(true);
    function _.calleeExternal()                            external => ALWAYS(true);
    function _.calleeOverloadedInContractInternal()        internal => ALWAYS(true);
    function _.calleeOverloadedInLibraryInternal()         internal => ALWAYS(true);
    function _.calleeOverloadedInContractExternal()        external => ALWAYS(true);
    function _.calleeOverloadedInLibraryExternal()         external => ALWAYS(true);
    function _.calleeOverloadedInInterfaceExternal()       external => ALWAYS(true);
    function _.calleeOverloadedInLibraryWithOnlyInternal() internal => ALWAYS(true);

    // functions from the contract Test to call in rules
    function callInternal() external returns bool;
    function callExternal() external returns bool;
    function callOverloadedInContractInternal() external returns bool;
    function callCOverloadedInContractInternal() external returns bool;
    function callOverloadedInLibraryInternal() external returns bool;
    function callT2OverloadedInLibraryInternal() external returns bool;
    function callOverloadedInContractExternal() external returns bool;
    function callCOverloadedInContractExternal() external returns bool;
    function callOverloadedInLibraryExternal() external returns bool;
    function callT2OverloadedInLibraryExternal() external returns bool;
    function callOverloadedInInterfaceExternal() external returns bool;
    function callIOverloadedInInterfaceExternal() external returns bool;
}

rule callInternal(env e)                                { assert callInternal(e);                               }
rule callExternal(env e)                                { assert callExternal(e);                               }
rule callOverloadedInContractInternal(env e)            { assert callOverloadedInContractInternal(e);           }
rule callCOverloadedInContractInternal(env e)           { assert callCOverloadedInContractInternal(e);          }
rule callOverloadedInLibraryInternal(env e)             { assert callOverloadedInLibraryInternal(e);            }
rule callT2OverloadedInLibraryInternal(env e)           { assert callT2OverloadedInLibraryInternal(e);          }
rule callOverloadedInLibraryWithOnlyInternal(env e)     { assert callOverloadedInLibraryWithOnlyInternal(e);    }
rule callT3OverloadedInLibraryWithOnlyInternal(env e)   { assert callT3OverloadedInLibraryWithOnlyInternal(e);  }
rule callOverloadedInContractExternal(env e)            { assert callOverloadedInContractExternal(e);           }
rule callCOverloadedInContractExternal(env e)           { assert callCOverloadedInContractExternal(e);          }
rule callOverloadedInLibraryExternal(env e)             { assert callOverloadedInLibraryExternal(e);            }
rule callT2OverloadedInLibraryExternal(env e)           { assert callT2OverloadedInLibraryExternal(e);          }
rule callOverloadedInInterfaceExternal(env e)           { assert callOverloadedInInterfaceExternal(e);          }
rule callIOverloadedInInterfaceExternal(env e)          { assert callIOverloadedInInterfaceExternal(e);         }
