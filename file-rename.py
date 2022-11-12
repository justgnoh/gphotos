import json
import os

# Read Json Files
for file in os.listdir("./"):
    if file.endswith(".json"):
        targetFile = open(file)
        data = json.load(targetFile)
        print(data["title"])
    targetFile.close()

# Find Said File

# Rename Said File

# Update JSON
