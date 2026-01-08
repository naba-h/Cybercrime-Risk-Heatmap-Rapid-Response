"""
Risk Scoring Engine
Cybercrime Risk Heatmap & Rapid Response Framework
"""

import pandas as pd

def calculate_risk_score(severity, likelihood, asset_value):
    return round((severity * likelihood * asset_value) / 10, 2)

data = {
    "attack_type": ["Phishing", "Malware", "Ransomware", "DDoS"],
    "system": ["Email", "Workstation", "Server", "Network"],
    "severity": [3, 4, 5, 4],
    "likelihood": [4, 3, 2, 5],
    "asset_value": [3, 4, 5, 4]
}

df = pd.DataFrame(data)

df["risk_score"] = df.apply(
    lambda row: calculate_risk_score(
        row["severity"], row["likelihood"], row["asset_value"]
    ),
    axis=1
)

df.to_csv("processed_risk.csv", index=False)
print("Risk scores generated successfully")
