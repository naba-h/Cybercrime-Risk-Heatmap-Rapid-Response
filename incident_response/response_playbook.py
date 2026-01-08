"""
Rapid Incident Response Playbook
Part of Cybercrime Risk Heatmap & Rapid Response Framework
"""

INCIDENT_PLAYBOOK = {
    "Phishing": [
        "Isolate affected email accounts",
        "Reset compromised credentials",
        "Enable multi-factor authentication (MFA)",
        "Monitor suspicious login activity"
    ],
    "Malware": [
        "Isolate infected endpoint",
        "Run full malware removal scan",
        "Apply security patches",
        "Update endpoint detection rules"
    ],
    "Ransomware": [
        "Disconnect affected systems immediately",
        "Identify ransomware strain",
        "Restore systems from secure backups",
        "Notify SOC and initiate incident reporting"
    ]
}

def get_response_actions(incident_type):
    return INCIDENT_PLAYBOOK.get(
        incident_type,
        ["Escalate incident to SOC team for detailed investigation"]
    )

if __name__ == "__main__":
    incident = "Malware"
    actions = get_response_actions(incident)

    print(f"Incident Type: {incident}")
    print("Recommended Response Actions:")
    for action in actions:
        print(f"- {action}")
