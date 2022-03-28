import solcx
from pprint import pprint
import json

if __name__ == '__main__':
    srcfile = 'HelloWorld.sol'
    outbyte = 'HelloWorld.bytecode'
    outabi = 'HelloWorld.abi'
    contractname = 'PyHelloWorld'

    #print('インストール可能なsolcのバージョンをチェックします。')
    #pprint(solcx.get_installable_solc_versions())

    #print('バージョン0.8.7をインストールします。')
    # solcx.install_solc('0.8.7')

    print('HelloWorld.solをコンパイルします。')
    resultdict = solcx.compile_files(
        [srcfile],
        output_values=['abi', 'bin'],
        base_path='node_modules'
    )

    print('コンパイルが完了しました。結果を保存します。')

    mycontract = resultdict[srcfile + ':' + contractname]

    with open(outbyte, 'wt') as fp:
        fp.write(mycontract['bin'])

    with open(outabi, 'wt') as fp:
        json.dump(mycontract['abi'], fp)

    print('compile.pyを終了します。')

