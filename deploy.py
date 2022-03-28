from web3 import Web3
from pprint import pprint
import json
from time import sleep
import os

if __name__ == '__main__':
    abifile = 'HelloWorld.abi'
    bytecodefile = 'HelloWorld.bytecode'
    addressfile = 'HelloWorld.address'

    duration = 60

    # ABIの読み込み
    with open(abifile, mode='rt') as fp:
        abi = json.load(fp) # fp.read()

    # バイトコードの読み込み
    with open(bytecodefile, mode='rt') as fp:
        bytecode = fp.read()

    w3 = Web3(Web3.HTTPProvider('http://172.17.0.2:8545', request_kwargs={'timeout': duration}))
    
    print('Ethノードのアカウント一覧:', w3.eth.accounts)
    w3.eth.default_account = w3.eth.accounts[0]

    mycontract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # コントラクトのデプロイトランザクションを発行
    print('コントラクトのデプロイトランザクションを発行します。')
    tx_hash = None
    while tx_hash is None:
        try:
            print('アカウントを', duration, '秒アンロックします。')
            unlockresult = w3.parity.personal.unlock_account(w3.eth.default_account, 
                os.getenv('KOVAN_PASSWORD')
            )
            print('アンロック結果:', unlockresult)

            print('コントラクトのデプロイトランザクションを発行します。')
            tx_hash = mycontract.constructor().transact()
        except:
            import traceback
            traceback.print_exc()
            sleep(3)
    print('デプロイトランザクションのhash:', tx_hash.hex())

    # トランザクション終了を待つ
    tx_receipt = None
    print('トランザクション終了をwaitします。')
    while tx_receipt is None:
        try:
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        except:
            import traceback
            traceback.print_exc()
            sleep(3)
    print('終了しました。')

    # コントラクトのアドレスを保存する
    print('コントラクトのアドレスを保存します。')
    pprint(tx_receipt)
    print('デプロイされたコントラクトアドレス:', tx_receipt.contractAddress)
    with open(addressfile, mode='wt') as fp:
        fp.write(tx_receipt.contractAddress)

    print('コントラクトのデプロイが終了しました。')
