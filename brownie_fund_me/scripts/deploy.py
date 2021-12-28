from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    DECIMALS,
    STARTING_PRICE,
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fund me contract

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(
            f"price feed from {network.show_active()} price_feed_address {price_feed_address}"
        )
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address  # get the most recent deloyed

    print(f"price_feed_address:{price_feed_address}")
    fund_me = FundMe.deploy(
        price_feed_address,  # pass parameter to constructor this way
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    print(f"getPrice {fund_me.getPrice()}")
    # print(f"Entrance fee: {fund_me.getEntranceFee()}")
    return fund_me


def main():
    deploy_fund_me()
