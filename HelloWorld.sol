// SPDX-License-Identifier: GPL3
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/access/Ownable.sol";

contract PyHelloWorld is Ownable {

    string hellomessage = "Hello, World! - by py-solc-x and web3.py!";

    constructor() payable {
    }

    function hello() public view returns (string memory) {
        return hellomessage;
    }

    function destroy() public onlyOwner {
        selfdestruct(payable(msg.sender));
    }
}