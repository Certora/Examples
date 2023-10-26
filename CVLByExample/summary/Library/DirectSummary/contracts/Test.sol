// Libraries with functions with identical signature
library TestLibrary {
    function calleeInternal()               internal returns (bool) { return false; }
    function calleeExternal()               external returns (bool) { return false; }

    function calleeOverloadedInContractInternal()           internal returns (bool) { return false; }
    function calleeOverloadedInLibraryInternal()            internal returns (bool) { return false; }
    function calleeOverloadedInLibraryWithOnlyInternal()    internal returns (bool) { return false; }

    function calleeOverloadedInContractExternal()   external returns (bool) { return false; }
    function calleeOverloadedInLibraryExternal()    external returns (bool) { return false; }
    function calleeOverloadedInInterfaceExternal()  external returns (bool) { return false; }
}

library TestLibrary2 {
    function calleeOverloadedInLibraryExternal()   external   returns (bool) { return false; }
    function calleeOverloadedInLibraryInternal()   internal   returns (bool) { return false; }
}

library TestLibrary3 {
    function calleeOverloadedInLibraryWithOnlyInternal() internal returns (bool) { return false; }
}

contract Test {
    constructor() { }
    IUnresolved public unresolved;

    function calleeOverloadedInContractExternal()   external   returns (bool) { return false; }
    function calleeOverloadedInContractInternal()   internal   returns (bool) { return false; }

    function callInternal()     external returns (bool) { return TestLibrary.calleeInternal(); }
    function callExternal()     external returns (bool) { return TestLibrary.calleeExternal(); }
    function callOverloadedInContractInternal()             external returns (bool) { return TestLibrary.calleeOverloadedInContractInternal();          }
    function callCOverloadedInContractInternal()            external returns (bool) { return calleeOverloadedInContractInternal();                      }
    function callOverloadedInLibraryInternal()              external returns (bool) { return TestLibrary.calleeOverloadedInLibraryInternal();           }
    function callT2OverloadedInLibraryInternal()            external returns (bool) { return TestLibrary2.calleeOverloadedInLibraryInternal();          }
    function callOverloadedInLibraryWithOnlyInternal()      external returns (bool) { return TestLibrary.calleeOverloadedInLibraryWithOnlyInternal();   }
    function callT3OverloadedInLibraryWithOnlyInternal()    external returns (bool) { return TestLibrary3.calleeOverloadedInLibraryWithOnlyInternal();  }

    function callOverloadedInContractExternal()     external returns (bool) { return TestLibrary.calleeOverloadedInContractExternal();  }
    function callCOverloadedInContractExternal()    external returns (bool) { return this.calleeOverloadedInContractExternal();              }
    function callOverloadedInLibraryExternal()      external returns (bool) { return TestLibrary.calleeOverloadedInLibraryExternal();   }
    function callT2OverloadedInLibraryExternal()    external returns (bool) { return TestLibrary2.calleeOverloadedInLibraryExternal();  }

    function callOverloadedInInterfaceExternal()    external returns (bool) { return TestLibrary.calleeOverloadedInInterfaceExternal(); }
    function callIOverloadedInInterfaceExternal()   external returns (bool) { return unresolved.calleeOverloadedInInterfaceExternal(); }
    
}

interface IUnresolved {
    function calleeOverloadedInInterfaceExternal()  external returns (bool);
}