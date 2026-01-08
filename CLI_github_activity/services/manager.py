import requests


class Manager():
    def __init__(self):
        pass

    def fetch_activity(self, user_name):
        user_name = user_name
        url = f"https://api.github.com/users/{user_name}/events"

        response = requests.get(url)

        return response.json()
    
    def output(self, event):
        
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name", "repositório desconhecido")

        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            return f"Pushed {len(commits)} commits to {repo}"

        if event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "updated")
            return f"{action.capitalize()} an issue in {repo}"

        if event_type == "WatchEvent":
            return f"Starred {repo}"

        if event_type == "ForkEvent":
            return f"Forked {repo}"

        return None

    

