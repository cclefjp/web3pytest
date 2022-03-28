''' callcontract.py - デプロイしたコントラクトを呼び出す '''

import os
from web3 import Web3
from web3.contract import Contract

KOVAN_URL = os.getenv('KOVAN_URL')
address_file = 'HelloWorld.address'
abi_file = 'HelloWorld.abi'

w3 = Web3(Web3.HTTPProvider(KOVAN_URL))

print('w3.isConnected:', w3.isConnected())

''' コントラクトアドレスの読み出し '''
with open(address_file, mode='rt') as fp:
    hwadd = fp.read()

''' ABIの読み出し '''
with open(abi_file, mode='rt') as fp:
    abi = fp.read()

''' コントラクトオブジェクトの作成 '''
contract = w3.eth.contract(hwadd, abi=abi)

''' 関数を指定 '''
c_func = contract.functions.hello()

''' コントラクト関数の呼び出し '''
print('コントラクトを呼び出します。')
result = c_func.call()
print(result)

