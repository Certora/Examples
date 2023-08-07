import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract VulnerableBankOtherFixed {
  
    using SafeMath for uint256;
    mapping(address => uint) public balances;

    function donate(address _to) public payable {
        balances[_to] = balances[_to].add(msg.value);
    }

    function balanceOf(address _who) public view returns (uint balance) {
        return balances[_who];
    }

    function getEthBalance() external view returns(uint){
        return address(this).balance;
    } 

    function withdraw(uint _amount) public {
        if (balances[msg.sender] >= _amount) {
            balances[msg.sender] -= _amount;
            (bool result,) = msg.sender.call{value:_amount}("");
            require (result, "Withdrawal failed");
        }
    }

    receive() external payable {}
}
