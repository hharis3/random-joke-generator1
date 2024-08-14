import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    return f"{joke['setup']} - {joke['punchline']}"

if __name__ == "__main__":
    print(get_joke())
You're right. 