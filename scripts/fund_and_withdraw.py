from brownie import FundMe
from scripts.helpful_scripts import get_account

# 05:45 de kaldım
# ValueError: No data was returned - the call likely reverted
# Hatasını aldım
# Withdraw a geçmedim


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    enterance_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is {enterance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": enterance_fee})


def main():
    fund()
