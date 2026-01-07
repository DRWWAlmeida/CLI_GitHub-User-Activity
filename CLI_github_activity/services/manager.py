import requests


class Manager():
    def __init__(self):
        pass

    def check(self, user_name):
        user_name = user_name
        url = f"https://api.github.com/users/{user_name}/events"

        events = requests.get(url)
        print(events.text)
