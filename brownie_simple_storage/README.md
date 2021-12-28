FileNotFoundError: [Errno 2] No such file or directory: 'ganache-cli': npm -g install --upgrade ganache-cli

brownie command cannot take # comments
create account: brownie accounts new alias-for-your-account-for-example-test-account
list all accounts: brownie accounts list
delete account: brownie accounts delete alias-for-your-account-for-example-test-account
run script: brownie run scripts/deploy.py
unit test with python debugger: brownie test --pdb

run brownie with a network remember account needs to exists in your network: brownie run scripts/deploy.py --network rinkeby

Enter brownie cli: brownie console