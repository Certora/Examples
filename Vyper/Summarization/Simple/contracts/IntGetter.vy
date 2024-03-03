interface IntGetter:
  def get1() -> uint256: view
  def get2() -> uint256: view
  def set1(): nonpayable

implements: IntGetter

@external
@view
def get1() -> uint256:
    return 3

@external
@view
def get2() -> uint256:
    return 2

@external
@nonpayable
def set1():
    pass

