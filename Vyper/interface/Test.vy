

# @version ^0.3.9


interface TestInterface:
    # get address of owner
    def owner() -> address: view
    # get eth 
    def eth() -> uint256: view
    # set new owner
    def setOwner(owner: address): nonpayable
    # send ETH
    def sendEth(): payable
    # set owner and send ETH
    def setOwnerAndSendEth(owner: address): payable


# store contract having the above interface
testInterface: public(TestInterface)


@external
def __init__(test: address):
    # store contract instance
    self.testInterface = TestInterface(test)
    # if you need to get address from self.test
    addr: address = self.testInterface.address


@external
@view
def getOwner() -> address:
    return self.testInterface.owner()

@external
@view
def getEth() -> uint256:
    return self.testInterface.eth()


@external
@view
def getOwnerFromAddress(test: address) -> address:
    # you can also call functions by passing in the address of the interface
    return TestInterface(test).owner()


@external
def setOwner(owner: address):
    self.testInterface.setOwner(owner)


@external
@payable
def sendEth():
    self.testInterface.sendEth(value=msg.value)


@external
@payable
def setOwnerAndSendEth(owner: address):
    self.testInterface.setOwnerAndSendEth(owner, value=msg.value)