// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage{
    // uint256 favoriteNumber = 5;
    // bool favoriteBool = true;
    // string favoriteString = "String";
    // int favoriteInteger = -5;
    // address favoriteAddress = 0x5755645cf57887878787D64579;
    // bytes32 favoriteBytes = "cat";

    uint256 public favoriteNumber;

    function store(uint256 _favoriteNumber) public returns(uint256) {
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }  

    struct People{
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public NametofavoriteNumber;

    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

    // function retrieve(uint256 favoriteNumber) public pure{
    //     favoriteNumber + favoriteNumber;
    // } 

    function addperson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        NametofavoriteNumber[_name] = _favoriteNumber;
    }
}
