from ecdsa.main import calculate_ethereum_address

def test_calculate_ethereum_address_from_public_key():
    public_key_hex = "eb59103e1bf87fc458f0cd188c51f1a872beae04e4df620d47e7282e8afee09fa5ef139bc781bfc42538f59dcc42e01e5d7e49f531d22e6350dfa70ea23cb040"
    expected_address = "0xc8496F9C8B1922627A4597bb9702b7ad7A9AC55C"
    assert calculate_ethereum_address(public_key_hex) == expected_address

