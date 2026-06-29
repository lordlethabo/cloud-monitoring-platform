RECOMMENDATIONS = {
    "High CPU Usage": (
        "Investigate running processes, optimize workloads, "
        "or increase CPU resources."
    ),
    "High Memory Usage": (
        "Check for memory leaks, restart affected services, "
        "or increase available memory."
    ),
    "Low Disk Space": (
        "Remove unnecessary files, archive old logs, "
        "or increase disk capacity."
    ),
}


def get_recommendation(issue: str) -> str:
    return RECOMMENDATIONS.get(
        issue,
        "No recommendation available."
    )
