# mainnet.py - Network parameters for the main Bitcoin network ("mainnet")

class MainNet:
    """
    Network parameters for the main Bitcoin network ("mainnet")
    """

    def __init__(self):
        # Magic bytes (4 bytes) used to identify messages on the network
        self.magic_bytes = bytes.fromhex("F9BEB4D9")

        # Default port used for connecting to nodes on the network
        self.default_port = 8333

        # Address prefixes for different types of addresses (e.g., P2PKH, P2SH)
        self.address_prefixes = {
            "P2PKH": bytes.fromhex("00"),  # Address starts with '1'
            "P2SH": bytes.fromhex("05"),   # Address starts with '3'
            # Add more address prefixes as needed
        }

        # Genesis block information (block height 0)
        self.genesis_block = {
            "hash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
            "timestamp": 1231006505,  # Unix timestamp (seconds since epoch)
            "nonce": 2083236893,
            # Add more genesis block parameters as needed
        }

        # Difficulty adjustment parameters
        self.difficulty_adjustment_interval = 2016
        # Add more difficulty adjustment parameters as needed

        # ... Add more network parameters as needed

# Instantiate the MainNet object
mainnet = MainNet()
