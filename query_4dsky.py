# Save as: query_4dsky.py

from web3 import Web3
import json

# Connect to EVM RPC
rpc_url = "https://testnet.hashio.io/api"
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Check connection
print(f"✅ Connected to Hedera EVM: {w3.is_connected()}")

# Load config
with open("hackathon_config.json") as f:
    config = json.load(f)

contract_address = config["buyer"]["smart_contract"]
print(f"✅ 4DSky Contract: {contract_address}")

# Query contract (need ABI, but for now just check it exists)
code = w3.eth.get_code(contract_address)
print(f"✅ Contract is deployed: {len(code)} bytes")

# The sellers are likely registered on this contract
# Next step: Query contract to get Mode-S endpoints for each receiver
