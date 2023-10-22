methods {
    function balance(address account) external returns(uint256) envfree;
    function advanceDays(uint256 n) external envfree;
}

// A rule for verifying that balance calculation is monotonic with respect to time.
// This rule fails because of the overapproximation done by the solver.
rule yield_monotonic(address a, uint256 n) {
  uint256 y1 = balance(a);
  require n >= 0;
  advanceDays(n);
  uint256 y2 = balance(a);
  assert (y2 >= y1, "balance is not monotonic with respect to time");
}
