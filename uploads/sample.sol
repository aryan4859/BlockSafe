// example_contract.sol
pragma solidity ^0.8.0;

contract VulnerableContract {
    address owner = 0x1234567890abcdef1234567890abcdef12345678;

    function withdraw(uint256 amount) public {
        msg.sender.call{value: amount}(""); // Unchecked call
    }

    function increment(uint256 value) public {
        value++;
    }

    function getTime() public view returns (uint256) {
        return block.timestamp; // Block timestamp usage
    }
}