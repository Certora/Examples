contract Example {
  uint public x;
  function updateX() external {
    x = 3;
  }

  function foo() external {
    myInternalFoo();
  }

  function myInternalFoo() internal {
    // ...
  }

  function bar() external {
    x = 5;
  }

}
