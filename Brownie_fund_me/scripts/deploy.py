from brownie import Fund_Me
from scripts.helpful_scripts import get_account

def deploy_fund_me():
    account = get_account()
    fund_me = Fund_Me.deploy({"from": account})
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()