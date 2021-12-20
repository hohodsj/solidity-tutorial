from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # brownie generated account
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Transct
    # Call
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    # wait number of block chain is updated
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
