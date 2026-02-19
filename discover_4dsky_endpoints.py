# Save as: discover_4dsky_endpoints.py

import json

# Load sellers
with open("sellers.json") as f:
    sellers = json.load(f)

print(f"=== DISCOVERING {len(sellers)} RECEIVERS ===\n")

# Each seller should have a way to connect
# Likely: Neuron peer discovery via HCS or direct ZMQ endpoints

receivers_mapped = []

for seller in sellers:
    # Your system will need to:
    # 1. Query Hedera HCS discovery topic to find ZMQ endpoints
    # 2. Or use seller public_key to authenticate
    
    receiver = {
        "id": seller["name"].replace(" ", "_"),
        "public_key": seller["public_key"],
        "lat": seller["lat"],
        "lon": seller["lon"],
        "alt": seller["alt"],
        "name": seller["name"]
        # endpoint: (will be discovered via HCS or Neuron)
    }
    receivers_mapped.append(receiver)

# Save for MLAT system
with open("receivers.json", "w") as f:
    json.dump(receivers_mapped, f, indent=2)

print(f"✅ Mapped {len(receivers_mapped)} receivers")
print("\nFirst 5 receivers:")
for rx in receivers_mapped[:5]:
    print(f"  {rx['name']}: ({rx['lat']}, {rx['lon']})")
