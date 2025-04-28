// sample.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SampleToken {
    string public name = "SampleToken";
    string public symbol = "STK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    address public owner;

    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balanceOf[owner] = totalSupply;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        balanceOf[msg.sender] -= amount;
        balanceOf[recipient] += amount;
        return true;
    }

    function approve(address spender, uint256 amount) public returns (bool) {
        allowance[msg.sender][spender] = amount;
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Invalid sender address");
        require(recipient != address(0), "Invalid recipient address");
        require(balanceOf[sender] >= amount, "Insufficient balance");
        require(allowance[sender][msg.sender] >= amount, "Allowance exceeded");

        balanceOf[sender] -= amount;
        balanceOf[recipient] += amount;
        allowance[sender][msg.sender] -= amount;
        return true;
    }

    function burn(uint256 amount) public onlyOwner {
        require(balanceOf[owner] >= amount, "Insufficient balance to burn");
        totalSupply -= amount;
        balanceOf[owner] -= amount;
    }

    // Vulnerability: Reentrancy example
    // Unsafe function susceptible to reentrancy attack
    function withdraw(uint256 amount) public onlyOwner {
        require(balanceOf[owner] >= amount, "Insufficient balance");
        // Funds are transferred before balance is updated, which may lead to reentrancy attack
        payable(msg.sender).transfer(amount);
        balanceOf[owner] -= amount;
    }

    // Example of timestamp dependency vulnerability
    function isSaleOpen() public view returns (bool) {
        return block.timestamp > 1622527200;  // Timestamp-based logic
    }
}
