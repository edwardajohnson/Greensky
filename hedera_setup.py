# Save as: hedera_setup.py

from hedera import Client, AccountId, PrivateKey
import json

# Load config
with open("hackathon_config.json") as f:
    config = json.load(f)

# Connect to Hedera testnet
client = Client.forTestnet()

# Set operator (your Hedera account)
operator_id = AccountId.fromString(config["buyer"]["hedera_id"])
operator_key = PrivateKey.fromString(config["buyer"]["private_key"])

client.setOperator(operator_id, operator_key)

# Test connection
account_balance = client.getBalance(operator_id).get()
print(f"✅ Connected to Hedera testnet")
print(f"✅ Your account: {operator_id}")
print(f"✅ Balance: {account_balance} tinybar")

# Query Mirror Node
import requests
mirror_url = config["hedera"]["mirror_api"]
response = requests.get(f"{mirror_url}/accounts/{operator_id}")
print(f"✅ Mirror Node: {response.json()['account']}")

client.close()
