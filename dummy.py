import sys

if len(sys.argv) < 2:
    print("Usage: python test1.py <username>")
else:
    username = sys.argv[1]

    print("Program started successfully")
    print("Username received:", username)
    print("Hello,", username)
