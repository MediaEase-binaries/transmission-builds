#!/usr/bin/env python3
import yaml

matrix = []

def add(version, config):
    """Add build combinations to the matrix.
    
    Args:
        version (str): Transmission version
        config (dict): Dictionary containing stability and supported OSes
            Format: {
                "stability": "stable|oldstable|next",
                "oses": ["debian-11", "ubuntu-22.04", etc...]
            }
    """
    for os in config["oses"]:
        matrix.append({
            "version": version,
            "stability": config["stability"],
            "os": os
        })

# Configuration based on version support
TRANSMISSION_CONFIGS = {
    "4.0.3": {
        "stability": "oldstable",
        "oses": ["debian-11", "ubuntu-22.04"]
    },
    "4.0.4": {
        "stability": "stable",
        "oses": ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"]
    },
    "4.0.5": {
        "stability": "stable",
        "oses": ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"]
    },
    "4.0.6": {
        "stability": "stable",
        "oses": ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"]
    },
    "4.1.0-beta.2": {
        "stability": "next",
        "oses": ["debian-12", "ubuntu-24.04"]
    }
}

# Add each version to the matrix
for version, config in TRANSMISSION_CONFIGS.items():
    add(version, config)

# Output the matrix in GitHub Actions compatible format
print(yaml.safe_dump({ "include": matrix }, sort_keys=False))
