contract Example{
    address public constant foo = 0xE0f5206BBD039e7b0592d8918820024e2a7437b9;

    //We trust the contract address and the sighash
    function callTrusted() external returns (uint){
        Foo bar = Foo(foo);
        return bar.trusted();
    }

    //We trust the contract address, but not the sighash of the call.
    function callUntrusted() external returns (uint){
        Foo bar = Foo(foo);
        return bar.untrusted();
    }

    //We neither trust the sighash, nor the contract address.
    function callUntrusted(address userTrustedContractAddress) external returns (uint){
        Foo bar = Foo(userTrustedContractAddress);
        return bar.untrusted();
    }

    //We trust the sighash, but the contract address is unknown.
    function callUntrustedDespiteKnownSighash(address userTrustedContractAddress) external returns (uint){
        Foo bar = Foo(userTrustedContractAddress);
        return bar.trusted();
    }
}

contract Foo{
    //Sighash: 0xb23d4266
    function untrusted() external returns (uint){
        return 1;
    }
    //Sighash: 0x7e2a6db8
    function trusted() external returns (uint){
        return 2;
    }
}
