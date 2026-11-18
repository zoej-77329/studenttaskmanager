
import unittest
import main


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        main.reset_tasks()

    def test_add_task(self):
        task = main.add_task("Complete Assignment")

        self.assertEqual(task["title"], "no Assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(task["id"], 1)

    def test_complete_task(self):
        task = main.add_task("Study Git")

        result = main.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = main.add_task("Submit Project")

        result = main.delete_task(task["id"])

        self.assertIsNotNone(result)
        self.assertEqual(len(main.tasks), 0)


if __name__ == "__main__":
    unittest.main()
