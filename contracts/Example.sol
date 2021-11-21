// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;


contract Example {

    event Message(
        address sender,
        string message,
        uint value
    );

    function message(string memory message) external payable {
        emit Message(msg.sender, message, msg.value);
    }
}
