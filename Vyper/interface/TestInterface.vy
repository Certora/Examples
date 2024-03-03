# @version ^0.3.9
# The imported interface

owner: public(address)
eth: public(uint256)


@external
def setOwner(owner: address):
    self.owner = owner


@external
@payable
def sendEth():
    self.eth = msg.value


@external
@payable
def setOwnerAndSendEth(owner: address):
    self.owner = owner
    self.eth = msg.value

