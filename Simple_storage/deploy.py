import json
import os
from dotenv import load_dotenv
load_dotenv()

from web3 import Web3
from solcx import compile_standard, install_solc
install_solc('0.6.0')


with open("./SimpleStorage.sol","r") as file:
    simple_storage_file = file.read()

# Compile our solidity

compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file, indent=4)
    

# Get bytecode 
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# Get abi
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# For connecting to Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xf4e2fbCd9cA59D40E7BD7Cb9b222c57a6A984526"
private_key = os.getenv("PRIVATE_KEY")

'''Procedure to follow:
1. Build the Contract Deploy Transaction
2. Sign the Transaction
3. Send the Transaction 
'''

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latest Transaction
nonce = w3.eth.get_transaction_count(my_address)

transaction = SimpleStorage.constructor().build_transaction({
    "chainId": chain_id, "from": my_address, "nonce": nonce
})

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send this signed Transaction
print("Deploying Contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")

# Working with the contract, we need 
# - Contract address and Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Call -> Simulate makinf the call and getting a return value
# Transact -> Actually make a state change

# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
print("Updating Contract...")

store_transaction = simple_storage.functions.store(15).build_transaction({
    "chainId": chain_id, "from": my_address, "nonce": nonce + 1
})
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")

print(simple_storage.functions.retrieve().call())

