import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
github_base = "https://github.com/IvanShepeta/LeetCode/blob/master"


difficulty_badge = {
    "Easy": '![Easy](https://img.shields.io/badge/-Easy-green)',
    "Medium": '![Medium](https://img.shields.io/badge/-Medium-orange)',
    "Hard": '![Hard](https://img.shields.io/badge/-Hard-red)'
}



problems = []

for difficulty in ["easy", "medium", "hard"]:
    folder = os.path.join(base_dir, difficulty)
    if not os.path.exists(folder):
        continue

    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            prob_id, title, link = None, None, None
            for line in lines:
                line = line.strip()
                m = re.search(r"Problem:\s*(\d+)\.\s*(.+)", line)
                if m:
                    prob_id = m.group(1)
                    title = m.group(2).strip()
                lm = re.search(r"Link:\s*(https?://\S+)", line)
                if lm:
                    link = lm.group(1).strip()
                if prob_id and title:
                    break

            if prob_id and title:
                if not link:
                    link = f"https://leetcode.com/problems/{title.lower().replace(' ','-')}"
                rel_path = os.path.relpath(filepath, base_dir).replace("\\", "/")
                github_link = f"{github_base}/{rel_path}"
                problems.append({
                    "id": prob_id,
                    "title": title,
                    "link": link,
                    "solution": "Python",
                    "solution_link": github_link,
                    "difficulty": difficulty.capitalize()
                })

# Sorted
problems = sorted(problems, key=lambda x: int(x["id"]))

# ==========================
# Header README
# ==========================
header = """
# 🧠 LeetCode Solutions

This repository contains my personal LeetCode solutions written in Python.  
I use it to track my progress, improve my problem-solving skills, and prepare for technical interviews.

"""


# ==========================
# Generate a Markdown table
# ==========================
md = header
md += "| # | Title | Solution | Difficulty |\n"
md += "|---|-------|----------|-----------|\n"
for p in problems:
    md += f'| {p["id"]} | [{p["title"]}]({p["link"]}) | [{p["solution"]}]({p["solution_link"]}) | {difficulty_badge[p["difficulty"]]}|\n'

# ==========================
# Write README.md
# ==========================
readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(md)

print(f"README.md успішно згенеровано з гарною шапкою та посиланнями на рішення!")
