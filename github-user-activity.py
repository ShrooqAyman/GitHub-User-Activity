import sys
import requests

def get_user_activity(username):
    """
    Fetches and displays recent public activity for a given GitHub username.

    Parameters:
        username (str): GitHub username to fetch activity for.

    Returns:
        None
    """
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for user '{username}'. Status code: {response.status_code}")
        return
    events = response.json()
    if not events:
        print(f"No recent public activity found for '{username}'.")
        return

    print(f"Recent activity for {username}:\n")
    for event in events:
        repo_name = event["repo"]["name"]
        event_type = event.get("type")

        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            count_commits = len(commits)
            print(f"- Pushed {count_commits} commits in {repo_name}")

        elif event_type == "CreateEvent":
            print(f"- Started in {repo_name}")
        
        elif event_type == "IssuesEvent":
            print(f"- Opened a new issue  in {repo_name}")
        
        else:
            print(f"- {event_type} in {repo_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
            print("Please enter username")
    else:
        username = sys.argv[1]
        get_user_activity(username)