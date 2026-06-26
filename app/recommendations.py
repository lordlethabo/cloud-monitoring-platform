def get_recommendation(issue: str) -> str:
    if issue == "High CPU Usage":
        return "Investigate running processes, stop unnecessary services, and consider scaling the server."

    if issue == "High Memory Usage":
        return "Check for memory leaks, restart heavy services, and optimize application memory usage."

    if issue == "Low Disk Space":
        return "Remove unused files, rotate logs, clean temporary files, or increase disk storage."

    return "Review server health, check recent deployments, and investigate system logs."