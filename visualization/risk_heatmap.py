"""
Cybercrime Risk Heatmap Visualization
Part of Cybercrime Risk Heatmap & Rapid Response Framework
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "attack_type": ["Phishing", "Malware", "Ransomware", "DDoS"],
    "system": ["Email", "Workstation", "Server", "Network"],
    "risk_score": [36, 48, 50, 40]
}

df = pd.DataFrame(data)

pivot = df.pivot(index="attack_type", columns="system", values="risk_score")

sns.heatmap(pivot, annot=True, cmap="Reds")
plt.title("Cybercrime Risk Heatmap")
plt.show()
