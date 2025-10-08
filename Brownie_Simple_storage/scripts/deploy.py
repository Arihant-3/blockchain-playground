from brownie import accounts, config, SimpleStorage

def deplo_simple_storage():
    account = accounts[0]
    # print(account)
    
    # account = accounts.load("protected-account")
    # print(account)
    
    # account = accounts.add(config['wallets']['from_key'])
    # print(account)
    
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)
    
def main():
    deplo_simple_storage()
    
    