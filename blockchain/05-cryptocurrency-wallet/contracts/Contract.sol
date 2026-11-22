// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Cryptocurrency Wallet
/// @notice Study UTXO transaction signing, key derivation, and peer-to-peer consensus.
contract RiseAheadLedger {
    struct Record {
        address submitter;
        string payload;
        uint256 timestamp;
    }

    Record[] public records;
    event RecordAdded(uint256 indexed id, address indexed submitter, string payload);

    function addRecord(string calldata payload) external {
        records.push(Record(msg.sender, payload, block.timestamp));
        emit RecordAdded(records.length - 1, msg.sender, payload);
    }

    function totalRecords() external view returns (uint256) {
        return records.length;
    }
}
