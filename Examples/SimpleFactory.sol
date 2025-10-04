// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./SimpleStorage.sol";

// contract StorageFactory is SimpleStorage{ // Inherit from SimpleStorage
contract StorageFactory {

    SimpleStorage[] public simpleStorgeArray;

    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorgeArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // We need Address and ABI(Application Binary Interface)
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorgeArray[_simpleStorageIndex]));
        simpleStorage.store(_simpleStorageNumber);
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256){
        return  SimpleStorage(address(simpleStorgeArray[_simpleStorageIndex])).retrieve();
    }
}