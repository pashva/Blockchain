import json
from web3 import Web3
import hashlib
ganache_url="http://127.0.0.1:7545"

web3=Web3(Web3.HTTPProvider(ganache_url))
#Entity1 account
web3.eth.defaultAccount=web3.eth.accounts[0]
#Entity2 account
# print(web3.eth.accounts[1])

# print(type(web3.eth.accounts[1]))
# print(web3.eth.accounts)

abi=json.loads('[{"inputs":[{"internalType":"address","name":"investor","type":"address"},{"internalType":"uint256","name":"inr_invested","type":"uint256"}],"name":"buy_obsidians","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"investor","type":"address"}],"name":"equity_in_obsidian","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"inr_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_obsidian_bought","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"buyer","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer_obsidian","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
bytecode='608060405264174876e80060005560018055600060025534801561002257600080fd5b5061043c806100326000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c8063143124541461005c578063439647ef146100b45780635820cbb1146100d25780637fa6edbc146100f0578063d3d98c221461015e575b600080fd5b61009e6004803603602081101561007257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506101ac565b6040518082815260200191505060405180910390f35b6100bc6101f5565b6040518082815260200191505060405180910390f35b6100da6101fb565b6040518082815260200191505060405180910390f35b61015c6004803603606081101561010657600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610201565b005b6101aa6004803603604081101561017457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061034a565b005b6000600360008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b60025481565b60015481565b828073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461023a57600080fd5b81600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205403600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050505050565b80600054600254600154830201111561036257600080fd5b60006001548302905080600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205401600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550806002600082825401925050819055505050505056fea2646970667358221220608365f911318bf669aa1ecff6b65725e982fea07a45fb82b0f19d90010f4e6864736f6c63430007060033'

Obsidian = web3.eth.contract(abi=abi,bytecode=bytecode)

tx_hash=Obsidian.constructor().transact()
print(tx_hash)

tx_receipt= web3.eth.waitForTransactionReceipt(tx_hash)

print(tx_receipt)

contract1=web3.eth.contract(
    address=tx_receipt.contractAddress,
    
    abi=abi
)

# print(contract1.functions.equity_in_obsidian("0x7ba8CA2b64C533b32fEE6f2f77cE7BbC3bc8ada8").call())

# print(contract1.functions.buy_obsidians("0xf0FA3be9e4b76Ca9104fd005FC24e8E6cE20c8C5",50).transact())
# print(contract1.functions.equity_in_obsidian("0xf0FA3be9e4b76Ca9104fd005FC24e8E6cE20c8C5").call())

# print(contract1.functions.buy_obsidians("0x7Cec657E5880A08beEE0EF814a9B897143388B08",10).transact())
# web3.eth.defaultAccount="0x7Cec657E5880A08beEE0EF814a9B897143388B08"
# x=contract1.functions.transfer_obsidian("0x7Cec657E5880A08beEE0EF814a9B897143388B08","0x7ba8CA2b64C533b32fEE6f2f77cE7BbC3bc8ada8",10).transact()
# print(x)
# print(x.tx_hash)
# contract2=web3.eth.contract(
#     address="0x953dC77F30C9D3C3e14a8C7479e0aF9F5b9AF568",
#     abi=abi
# )
# print(contract1.functions.getMessage().call())
# print(contract2.functions.getMessage().call())
# contract1.functions.setMessage("new value").transact()
# print(contract.functions.getMessage().call())


# def get_balance(address):
#     # get crypto contract address from database
#     contract_address="0xf1Cc67D6B5D5bD9D4E85f45013850b1AADec073A"
#     ##################################
#     web3.eth.default_account=address
#     abi=json.loads('[{"inputs":[{"internalType":"address","name":"investor","type":"address"},{"internalType":"uint256","name":"inr_invested","type":"uint256"}],"name":"buy_obsidians","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"investor","type":"address"}],"name":"equity_in_obsidian","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"inr_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"max_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_obsidian_bought","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"buyer","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer_obsidian","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#     contract=web3.eth.contract(
#     address=contract_address,
#     abi=abi
#     )
#     x=contract.functions.equity_in_obsidian(address).call()
#     return x
# def buy_coin(address,amount):
#      # get crypto contract address from database
#     contract_address="0xf1Cc67D6B5D5bD9D4E85f45013850b1AADec073A"
#     ##################################
#     web3.eth.default_account=address
#     abi=json.loads('[{"inputs":[{"internalType":"address","name":"investor","type":"address"},{"internalType":"uint256","name":"inr_invested","type":"uint256"}],"name":"buy_obsidians","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"investor","type":"address"}],"name":"equity_in_obsidian","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"inr_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"max_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_obsidian_bought","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"buyer","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer_obsidian","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#     contract=web3.eth.contract(
#     address=contract_address,
#     abi=abi
#     )
#     x=contract.functions.buy_obsidians(address,amount).transact()
#     y=get_balance(address)
#     return {"new balance":y}



# def transfer_crypto(address1,address2,amount):
#     print(get_balance(address=address1))
#     print(get_balance(address=address2))
#       # get crypto contract address from database
#     contract_address="0xf1Cc67D6B5D5bD9D4E85f45013850b1AADec073A"
#     ##################################
#     web3.eth.default_account=address1
#     abi=json.loads('[{"inputs":[{"internalType":"address","name":"investor","type":"address"},{"internalType":"uint256","name":"inr_invested","type":"uint256"}],"name":"buy_obsidians","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"investor","type":"address"}],"name":"equity_in_obsidian","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"inr_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"max_obsidians","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_obsidian_bought","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"seller","type":"address"},{"internalType":"address","name":"buyer","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer_obsidian","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
#     contract=web3.eth.contract(
#     address=contract_address,
#     abi=abi
#     )
#     x=contract.functions.transfer_obsidian(address1,address2,10).transact()
#     print(get_balance(address=address1))
#     print(get_balance(address=address2))
    

# transfer_crypto("0xb363495BE625e00dcC397b0B9D1d25Af164761D5","0x70874AdD33C8b8f51289A633c1a377278997863F",10)