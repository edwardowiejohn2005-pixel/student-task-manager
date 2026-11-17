import unittest
from app import create_task, find_task

class TaskTests(unittest.TestCase):
    def test_create_and_find(self):
        tasks=[]
        t=create_task(tasks, "Study Python")
        self.assertEqual(find_task(tasks, t["id"])["title"], "Study Python")
    def test_unique_id_after_deletion(self):
        tasks=[{"id": 3, "title": "Old", "done": False}]
        self.assertEqual(create_task(tasks, "New")["id"], 4)
    def test_blank_title(self):
        with self.assertRaises(ValueError): create_task([], " ")

if __name__ == "__main__": unittest.main()
