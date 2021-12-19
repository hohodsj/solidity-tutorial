from brownie import accounts, config

def deploy_simple_storage():
    # brownie generated account
    # account = accounts[0]
    # print(account)

    # brownie set account with brownie accounts new <id>
    # account = accounts.load("test-net-account")
    # print(account)

    # environment variable
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)
    

def main():
    deploy_simple_storage()