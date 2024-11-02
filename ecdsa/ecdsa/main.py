import logging
import sha3

logging.basicConfig(level=logging.INFO)

def calculate_ethereum_address(public_key_hex):
    
    keccak = sha3.keccak_256()
    logging.info("Step 1: Creating Keccak-256 hash of the public key")
    
    keccak.update(bytes.fromhex(public_key_hex))
    hashed_public_key = keccak.hexdigest()
    logging.info("Hashed Public Key: %s", hashed_public_key)
    
    raw_address = hashed_public_key[-40:]
    logging.info("Step 2: Extract last 20 bytes of the hash as the raw address (no 0x prefix): %s", raw_address)
    
    address = "0x" + raw_address
    logging.info("Step 3: Add '0x' prefix to the address: %s", address)
    
    checksummed_address = apply_eip55_checksum(address)
    logging.info("Step 4: Apply EIP-55 checksum to get final address: %s", checksummed_address)
    
    return checksummed_address

def apply_eip55_checksum(address):

    address_hex = address[2:].lower()
    
    keccak = sha3.keccak_256()
    keccak.update(address_hex.encode("utf-8"))
    hash_address = keccak.hexdigest()
    logging.info("Hash of address for EIP-55 checksum: %s", hash_address)
    
    checksummed_address = "0x"
    for i, char in enumerate(address_hex):
        if int(hash_address[i], 16) >= 8:
            checksummed_address += char.upper()
        else:
            checksummed_address += char.lower()
    
    logging.info("Checksummed Address: %s", checksummed_address)
    return checksummed_address
