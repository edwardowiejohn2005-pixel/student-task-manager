import json
from pathlib import Path

FILE = Path(__file__).with_name("tasks.json")

def load(): return json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else []
def save(tasks): FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
def create_task(tasks, title):
    if not title.strip(): raise ValueError("Task title cannot be empty")
    task = {"id": max((t["id"] for t in tasks), default=0) + 1,
            "title": title.strip(), "done": False}
    tasks.append(task)
    return task
def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id: return task
    raise ValueError("Task ID not found")

def main():
    tasks = load()
    while True:
        print("\n1 List  2 Add  3 Rename  4 Complete  5 Delete  6 Exit")
        choice = input("Choice: ").strip()
        try:
            if choice == "1":
                for t in tasks: print(t["id"], "[x]" if t["done"] else "[ ]", t["title"])
            elif choice == "2": print("Created:", create_task(tasks, input("Title: ")))
            elif choice in ("3", "4", "5"):
                tid = int(input("Task ID: "))
                task = find_task(tasks, tid)
                if choice == "3":
                    title = input("New title: ").strip()
                    if not title: raise ValueError("Task title cannot be empty")
                    task["title"] = title
                elif choice == "4": task["done"] = True
                else: tasks.remove(task)
            elif choice == "6": break
            else: print("Invalid choice"); continue
            if choice != "1": save(tasks)
        except ValueError as exc: print("Error:", exc)

if __name__ == "__main__": main()
