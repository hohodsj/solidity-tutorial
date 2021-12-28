from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
from web3 import Web3

"""
When rerun delete build/deployments/5777
"""


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    # entrance_fee = 25 * 10 ** 15
    print("Funding")
    print(f"account:{account}")
    fund_me.fund(
        {
            "from": account,
            "value": entrance_fee,
        }
    )


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
