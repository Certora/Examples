// Libraries with functions with identical signature
library TestLibrary {
    function calleeInternal() internal returns (bool) { 
        return false; 
    }

    function calleeExternal() external returns (bool) { 
        return false; 
    }

    function calleeOverloadedInInterfaceExternal()  external returns (bool) { 
        return false; 
    }
}

contract Test {
    constructor() { }
    IUnresolved public unresolved;

    function calleeOverloadedInContractExternal()   external   returns (bool) { 
        return false; 
    }

    function calleeOverloadedInContractInternal()   internal   returns (bool) {
         return false; 
    }

    function callInternal() external returns (bool) { 
        return TestLibrary.calleeInternal(); 
    }

    function callExternal() external returns (bool) { 
        return TestLibrary.calleeExternal(); 
    }

    function callOverloadedInInterfaceExternal() external returns (bool) { 
        return TestLibrary.calleeOverloadedInInterfaceExternal(); 
    }

    function callIOverloadedInInterfaceExternal() external returns (bool) { 
        return unresolved.calleeOverloadedInInterfaceExternal(); 
    }
    
}

interface IUnresolved {
    function calleeOverloadedInInterfaceExternal()  external returns (bool);
}