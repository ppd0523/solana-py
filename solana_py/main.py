from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
from solana.utils.cluster import ENDPOINT
from solana.transaction import Transaction, TransactionInstruction, AccountMeta
from solana.keypair import Keypair
from solana.publickey import PublicKey


main_keypair = Keypair.from_secret_key()

if __name__ == '__main__':
    conn = Client(ENDPOINT.https.mainnet_beta)

    data = int.to_bytes(1, 0x01, "little", signed=False)

    ix = TransactionInstruction(
        keys=[
            AccountMeta(main_keypair.public_key, True, True),
        ],
        program_id=PublicKey(""),
        data=data,
    )
    tx = Transaction().add(ix)

    tx_id = conn.send_transaction(tx, main_keypair, opts=TxOpts(preflight_commitment=Confirmed))
    print(tx_id)
