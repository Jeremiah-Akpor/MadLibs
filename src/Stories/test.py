import unittest
from story import Story
from custom_exception import StoryException


class TestStory(unittest.TestCase):
    """In each test method, setting paragraphs, setting inputs,
       getting paragraphs and inputs, and printing the story,
       are all tested."""

    def setUp(self):
        # Initialize a Story object for testing
        self.story = Story("My Story", 2)
        self.story.set_paragraph(1, "This is paragraph 1.")
        self.story.set_paragraph(2, "This is paragraph 2.")

    def test_set_paragraph(self):
        self.story.set_paragraph(3, "This is a new paragraph.")
        self.assertEqual(self.story.get_paragraph(3),
                         "This is a new paragraph.")

    def test_set_paragraph_invalid_key(self):
        with self.assertRaises(StoryException):
            self.story.set_paragraph("invalid_key",
                                     "This should raise an exception.")

    def test_set_paragraph_invalid_content(self):
        with self.assertRaises(TypeError):
            self.story.set_paragraph(3, 123)  # Content should be a string

    def test_set_input(self):
        self.story.set_input(1, ["noun", "verb"])
        self.assertEqual(self.story.get_inputs(1), ["noun", "verb"])

    def test_set_input_paragraph_not_set(self):
        with self.assertRaises(StoryException):
            self.story.set_input(3, ["adjective", "place"])

    def test_get_title(self):
        self.assertEqual(self.story.get_title(), "My Story")

    def test_get_paragraph(self):
        self.assertEqual(self.story.get_paragraph(2), "This is paragraph 2.")

    def test_get_inputs(self):
        self.story.set_input(2, ["adjective", "place"])
        self.assertEqual(self.story.get_inputs(2), ["adjective", "place"])

    def test_print_story(self):
        self.story.set_input(1, ["noun", "verb"])
        self.story.set_input(2, ["adjective", "place"])
        with self.assertRaises(SystemExit):
            self.story.print_story()  # This should probably raise SystemExit


if __name__ == '__main__':
    unittest.main()
