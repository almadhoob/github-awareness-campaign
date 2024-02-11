import os
import subprocess
import random
from datetime import datetime, timedelta

MY_PROJECT = "/home/ams/github-awareness-campaign"  # Change it to the absolute path of your project
subprocess.run(["mkdir", "garbage"], cwd=MY_PROJECT)
daily_max = 10

def commits(date):
    num_commits = random.randint(1, daily_max)

    for i in range(1, num_commits + 1):
        filename = f"app_{date.strftime('%Y%m%d')}_{i}.py"
        filepath = os.path.join(MY_PROJECT, "garbage", filename)
        with open(filepath, 'w') as f:
            f.write("print(\"Hello, World!\")")

        subprocess.run(["git", "add", filepath], cwd=MY_PROJECT)
        subprocess.run(["git", "commit", "-m", f"Commit {i} for {date.date()}", 
                        "--date", date.isoformat()], cwd=MY_PROJECT)


num_days = 365
start_date = datetime.now() - timedelta(days=num_days)

for i in range(num_days):
    if random.choice([True, False]):
        date = start_date + timedelta(days=i)
        commits(date)

