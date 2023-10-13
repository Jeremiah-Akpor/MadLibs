""" This is the main file for the Mad Libs game. """

import importlib
import random
from stories.get_stories import get_stories
from stories.story import Story
from stories import constant

# Get the list of stories
stories = get_stories()  # returns list of strings

# Get a random story
idx = random.randint(0, len(stories) - 1)
story = stories[idx]

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
        place_holder = getattr(constant, f"{user_input}")
        place_holder = input(f"Enter a/an {user_input}: ")
        new_user_inputs.append(place_holder)
    class_of_story.set_input(paragraph_num, new_user_inputs)
    print(class_of_story.get_paragraph(paragraph_num))


for i in range(1, story_class.num_of_paragraph + 1):
    madlibs_helper(i, story_class)
