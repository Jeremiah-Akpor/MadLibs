""" This is the main file for the Mad Libs game. """

import importlib
import random
from stories.get_stories import get_stories
from stories.story import Story

# Get the list of stories
stories = get_stories()  # returns list of strings

# Get a random story
idx = random.randint(0, len(stories) - 1)
story = stories[1]

# Import the story module
story_module = importlib.import_module(f"stories.{story}_story")

# Get the story class
story_class = getattr(story_module, story)


def madlibs_helper(paragraph_num: int, class_of_story: Story):
    """It is an helper function for the MadLibs method"""

    user_inputs = class_of_story.get_inputs(paragraph_num)
    new_user_inputs = []

    # Get user inputs
    for user_input in user_inputs:
        # Get the constants for constant module
        user_input = input(f"Enter a/an {user_input}: ")
        new_user_inputs.append(user_input)
    class_of_story.update_story(paragraph_num, new_user_inputs)


def madlibs(class_of_story=story_class):
    """the madlibs game"""
    for i in range(1, class_of_story.num_of_paragraph + 1):
        if i == class_of_story.num_of_paragraph:
            madlibs_helper(i, class_of_story)
            print()
            print(class_of_story.print_story())
        elif i == 1:
            madlibs_helper(i, story_class)
            print()
            print(class_of_story.title)
            print(class_of_story.get_paragraph(i))
        else:
            madlibs_helper(i, class_of_story)
            print()
            print(class_of_story.get_paragraph(i))


if __name__ == "__main__":
    madlibs()
