# <a href="https://roadmap.sh/projects/github-user-activity">GitHub User Activity CLI</a> 🔍

A simple command-line tool built with Python that fetches and displays the recent public activity of a specified GitHub user using the GitHub API.

## 🚀 Features

- Fetches public GitHub activity using the GitHub Events API
- Displays different types of events such as:
  - Pushed commits
  - Created repositories/branches
  - Opened issues
- Simple and beginner-friendly CLI interface

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies with:

```bash
pip install requests
```
## 📦 Installation
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/ShrooqAyman/GitHub-User-Activity.git
```

## 🛠️ Usage
From the terminal, run the script with a GitHub username:
```bash
python github-user-activity.py <username>
```
### Example
```bash
python github-user-activity.py shrooqAyman
```
### Output
```bash
Recent activity for shrooqayman:

- Started in ShrooqAyman/GitHub-User-Activity
- Started in ShrooqAyman/GitHub-User-Activity
- Pushed 1 commits in ShrooqAyman/Task-Tracker
- Pushed 2 commits in ShrooqAyman/Task-Tracker
- DeleteEvent in ShrooqAyman/Task-Tracker
- Started in ShrooqAyman/Task-Tracker
- Pushed 1 commits in ShrooqAyman/Task-Tracker
```
