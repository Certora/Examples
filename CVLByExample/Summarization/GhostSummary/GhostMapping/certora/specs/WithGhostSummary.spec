methods {
  // tell the tool to use a ghost function as the summary for the function
    function continuous_interest(uint256 p, uint256 r, uint256 t) internal returns (uint256) =>
          ghost_interest[p][r][t];
    function balance(address account) external returns(uint256) envfree;
    function advanceDays(uint256 n) external envfree;
}

// define the ghost function
ghost mapping(uint256 => mapping(uint256 => mapping(uint256 => uint256))) ghost_interest {
  // add an axiom describing monotonicity of ghost_interest
  axiom forall uint256 p. forall uint256 r. forall uint256 t1. forall uint256 t2.
      t2 >= t1 => ghost_interest[p][r][t2] >= ghost_interest[p][r][t1];
}

rule yield_monotonic(address a, uint256 n) {
  // internally, when this calls continuous_interest, the function will
  // be summarized as ghost_interest
  uint256 y1 = balance(a);
  require n >= 0;
  advanceDays(n);
  // internally, when this calls continuous_interest, the function will
  // be summarized as ghost_interest
  uint256 y2 = balance(a);
  assert (y2 >= y1, "balance is not monotonic with respect to time");
}

