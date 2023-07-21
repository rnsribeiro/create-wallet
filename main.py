from eth_keys import keys
from eth_keys.backends import NativeECCBackend
from eth_utils import decode_hex
from eth_utils.crypto import keccak

def generate_wallet_from_seed(seed):
    # Derivação da chave privada a partir da seed
    private_key_bytes = keccak(seed)
    private_key = keys.PrivateKey(private_key_bytes, backend=NativeECCBackend)

    # Criação do objeto Wallet a partir da chave privada
    wallet = private_key.public_key.to_checksum_address()
    return private_key, wallet

# Geração de uma frase de recuperação (seed) aleatória de 12 palavras
mnemonic = "Rodrigo Ribeiro"  # Substitua essa frase pela sua própria frase de recuperação

# Codifica a frase de recuperação para bytes usando UTF-8
seed = mnemonic.encode('utf-8')

# Geração da carteira Ethereum determinística a partir da seed
private_key, address = generate_wallet_from_seed(seed)

# Exibição da frase de recuperação, chave privada, chave pública e endereço da carteira
print('Seed:', mnemonic)
print('Chave privada:', private_key)
print('Chave pública:', private_key.public_key)
print('Endereço da carteira:', address)
