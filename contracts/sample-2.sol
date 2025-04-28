// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract VulnerableBank {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: _amount}(""); // vulnerable: unchecked call
        require(success, "Transfer failed");

        balances[msg.sender] -= _amount; // vulnerable: reentrancy possible
    }

    function donate(address _to) public payable {
        balances[_to] += msg.value;
    }

    function kill() public {
        selfdestruct(msg.sender); // dangerous if not restricted
    }
}
