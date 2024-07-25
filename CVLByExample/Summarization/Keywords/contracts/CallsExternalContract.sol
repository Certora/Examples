import './IntGetter.sol';
import './AnotherIntGetterImpl.sol';
import './IntGetterImpl.sol';

contract CallsExternalContract {
  IntGetterImpl public g1;
  AnotherIntGetterImpl public g2;
  address public a;
  
  function getFromG1() external view returns (uint256) { 
    return g1.get1(); 
  }

  function getFromG2() external view returns (uint256) { 
    return g2.get2(); 
  }

  function setToG1(uint256 val) external { 
    return g1.set1(val); 
  }

  function setToG2(uint256 val) external { 
    return g2.set2(val); 
  }

  function getDummyB() public view returns(uint256) {
    return g2.dummyB();
  }

  function setXA(uint256 _x) public {
    g1.setX(_x);
  }

  function getXA() public returns(uint256){
    return g1.getX();
  }

  function setXB(uint256 _x) public {
      g2.setX(_x);
  }

  function getXB() public returns(uint256){
      return g2.getX();
  }

  function foo() external {
    a.call(abi.encodeWithSignature("noSuchFun()"));
  }

}