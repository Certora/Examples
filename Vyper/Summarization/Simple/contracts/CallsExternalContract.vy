from IntGetter.vy import IntGetter

g1: public(IntGetter)
g2: public(IntGetter)


@external 
def __init__(g1Address: address, g2Address: address):
  self.g1 = IntGetter(g1Address)
  self.g2 = IntGetter(g2Address)

@external
@view
def getFromG1() -> uint256:
  return self.g1.get1() 

@external
@view
def getFromG2() -> uint256:
  return self.g1.get2() 
