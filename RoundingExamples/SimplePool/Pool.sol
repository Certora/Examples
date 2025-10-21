
import {ERC20} from './ERC20.sol';
import {IERC20} from './IERC20.sol';
pragma solidity >=0.8.0;

interface IFlashLoanReceiver {
  function executeOperation(uint256 amount,uint256 premium,address initiator) external returns (bool);
}


contract Pool is ERC20 {

  IERC20 public asset;   
  uint256 private constant feePrecision = 10000; 
  //feeRate is up to 1%, so less than 100 as it is divided by feePrecision
  uint256 public feeRate; 
  uint256 public depositedAmount = 0;
  address public owner;

  constructor(uint256 feeRate_, IERC20 asset_) public ERC20() {
    feeRate = feeRate_;
    asset = asset_;
    owner = msg.sender;
  }

  function amountToShares(uint256 amount) public view virtual returns (uint256) { 
      return amount * totalSupply() / depositedAmount;   
  }
  function deposit(uint256 amount) public returns(uint256 shares) {
      if (totalSupply()==0 || depositedAmount == 0){
          shares = amount;
      }
      else{
        shares = amountToShares(amount);
        require (shares != 0);
      }
      asset.transferFrom(msg.sender,address(this),amount);
      depositedAmount = depositedAmount + amount;
      _mint(msg.sender,shares);
    }


  function withdraw(uint256 amount) public returns (uint256 shares)  {
    shares = amountToShares(amount);
   	_burn(msg.sender,shares);
		asset.transfer(msg.sender,amount);
    depositedAmount = depositedAmount - amount;
    }

    
    // half the fee to the owner, half to liquidity providers. rounding up fee
  function flashLoan(address receiverAddress, uint256 amount)  public {          
    uint256 totalPremium = calcPremium(amount);
    uint256 splitPremium = calcPremium(amount / 2);
  
    asset.transfer(msg.sender,amount);
    depositedAmount = depositedAmount - amount;
    IFlashLoanReceiver(receiverAddress).executeOperation(amount, totalPremium, msg.sender);
  
    asset.transferFrom(msg.sender,address(this),amount + splitPremium);
    asset.transferFrom(msg.sender,owner, splitPremium);
    depositedAmount = depositedAmount + amount + splitPremium;
  }

  function calcPremium(uint256 amount) public view returns (uint256){
    // round up
    return ((amount*feeRate + feePrecision - 1)/feePrecision);
  }
}