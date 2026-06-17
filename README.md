#  GitHub Activity Tracker

A simple command-line Python tool that fetches and displays a user's recent GitHub activity using the GitHub API.

---

##  Features

- Fetches GitHub user activity in real time
- Displays repository events in terminal
- Shows actions like:
  - PushEvent (commits)
  - CreateEvent (new repository)
  - ForkEvent (forked repository)
- Handles basic errors like invalid usernames and API failures

---

##  How It Works

1. Takes a GitHub username from command-line input  
2. Sends a request to GitHub API  
3. Receives JSON data of user events  
4. Parses and displays readable activity in terminal  

---

## 🛠️ Technologies Used

- Python 
- Requests library 
- GitHub REST API 
- sys.argv for CLI input

---

##  Installation

1. Clone the repository:

```bash
git clone https://github.com/Iush-sub/github_tracker.git
```
2. Navigate to the project folder:

```bash
cd github_tracker
```
3. Run the program:

```bash
python app.py Username
```
---
## Project Roadmap

This project is based on the Github User Activity CLI project roadmap:

https://roadmap.sh/projects/github-user-activity

## Author

Aayush Subedi
