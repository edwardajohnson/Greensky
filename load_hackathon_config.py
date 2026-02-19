# Save as: load_hackathon_config.py

import json
import os

# Parse buyer config
config = {}
with open("buyer-redacted") as f:
    for line in f:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            config[key] = value

print("=== YOUR HEDERA ACCOUNT ===")
print(f"Account ID: {config['hedera_id']}")
print(f"Location: {config['location']}")  # Your receiver position
print(f"Smart Contract: {config['smart_contract_address']}")

# Parse sellers (all receivers in network)
with open("sellers.json") as f:
    sellers = json.load(f)

print(f"\n=== NETWORK RECEIVERS ({len(sellers)} total) ===")
for seller in sellers[:5]:
    print(f"  {seller['name']}: ({seller['lat']}, {seller['lon']})")

# Save structured config
with open("hackathon_config.json", "w") as f:
    json.dump({
        "buyer": {
            "hedera_id": config['hedera_id'],
            "location": json.loads(config['location']),
            "private_key": config['private_key'],
            "smart_contract": config['smart_contract_address']
        },
        "sellers": sellers,
        "hedera": {
            "mirror_api": config['mirror_api_url'],
            "evm_rpc": config['eth_rpc_url']
        }
    }, f, indent=2)

print("\n✅ Saved hackathon_config.json")
