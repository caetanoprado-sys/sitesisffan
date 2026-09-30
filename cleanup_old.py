with open("index.html", "r") as f:
    lines = f.readlines()

# Remove lines 3243 to 3383 (the old positioning + money sections)
# 0-indexed: 3242 to 3382
del lines[3242:3382]

with open("index.html", "w") as f:
    f.writelines(lines)

print("Cleaned up old sections.")
