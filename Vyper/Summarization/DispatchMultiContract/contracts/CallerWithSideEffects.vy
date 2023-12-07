import CalleeA.vy as CalleeA
import CalleeB.vy as CalleeB

calleeA: CalleeA
calleeB: CalleeB

@external
def setXA(_x: uint256):
    x: uint256 = self.calleeA.setX(_x)

@external
def getXA() -> uint256:
    return self.calleeA.getX()

@external
def setXB(_x: uint256): 
    x: uint256 = self.calleeB.setX(_x)

@external
def getXB() -> uint256:
    return self.calleeB.getX()

@external
def setValueA(_value: uint256): 
    self.calleeA.setValue(_value)

@external
def getValueA() -> uint256:
    return self.calleeA.getValue()

@external
def setValueB(_value: uint256): 
    self.calleeB.setValue(_value)

@external
def getValueB() -> uint256:
    return self.calleeB.getValue()

@external
def getDummyB() -> uint256: 
    return self.calleeB.dummyB()

@external
def setXAFromAddress( _addr: address, _x: uint256): 
    callee: CalleeA = CalleeA(_addr)
    callee.setX(_x)

@external
def setXBFromAddress(_addr: address, _x: uint256): 
    callee: CalleeB = CalleeB(_addr)
    callee.setX(_x)


# def setXandSendEther(Callee _callee, uint256 _x): payable 
#    (uint256 x, uint256 value) = _callee.setXandSendEthervalue: msg.value(_x)


