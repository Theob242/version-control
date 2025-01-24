from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("../version.md", "w") as f:
    f.write(f"Version generated on: {now}")
