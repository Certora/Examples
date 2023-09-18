
methods {
    function bar() external envfree optional;
}


rule checkBar() {
  bar@withrevert();
  assert !lastReverted;
}
