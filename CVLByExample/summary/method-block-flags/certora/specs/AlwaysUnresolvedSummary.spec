
methods {
  // `UNRESOLVED` summaries can only be used on wildcard receivers; a call to `Partial.bar` can never be unresolved.
    function _.bar(uint256 _x) external envfree => ALWAYS(5) UNRESOLVED;
}


rule checkBar() {
  uint256 _x;
  bar@withrevert(_x);
  assert !lastReverted;
}
