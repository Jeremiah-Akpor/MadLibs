""" This is the main file for the Mad Libs game. """

import importlib
import random
import logging
from stories.get_stories import get_stories
from stories.story import Story

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

logging.info("MAIN: ---Starting the Mad Libs game.---")
logging.info("MAIN: Collecting stories.")
# Get the list of stories
stories = get_stories()  # returns list of strings

# Get a random story
idx = random.randint(0, len(stories) - 1)
story = stories[1]
logging.info("MAIN: Selected story: %s", story)

logging.info("MAIN: Importing the story module.")
# Import the story module
story_module = importlib.import_module(f"stories.{story}_story")

logging.info("MAIN: Getting the story class.")
# Get the story class
story_class = getattr(story_module, story)


def madlibs_helper(paragraph_num: int, class_of_story: Story):
    """It is an helper function for the MadLibs method"""
    logging.info("MAIN: Running the Mad Libs helper function.")
    logging.info("MAIN: Getting user inputs.")
    user_inputs = class_of_story.get_inputs(paragraph_num)
    new_user_inputs = []

    # Get user inputs
    for user_input in user_inputs:
        # Get the constants for constant module
        temp = user_input
        user_input = input(f"Enter a/an {user_input}: ")
        logging.info("MAIN: User input for %s : %s", temp, user_input)
        new_user_inputs.append(user_input)
    logging.info("MAIN: Updating the story with the new user input.")
    class_of_story.update_story(paragraph_num, new_user_inputs)


def madlibs(class_of_story=story_class):
    """the madlibs game"""
    logging.info("MAIN: Running the Mad Libs game.")
    for i in range(1, class_of_story.num_of_paragraph + 1):
        if i == class_of_story.num_of_paragraph:
            madlibs_helper(i, class_of_story)
            print()
            print(class_of_story.print_story())
            logging.info("MAIN: Finished the Mad Libs game.")
        elif i == 1:
            madlibs_helper(i, story_class)
            print()
            print(class_of_story.title)
            print(class_of_story.get_paragraph(i))
            logging.info("MAIN: Printed paragraph %s.", i)
        else:
            madlibs_helper(i, class_of_story)
            print()
            print(class_of_story.get_paragraph(i))
            logging.info("MAIN: Printed paragraph %s.", i)


if __name__ == "__main__":
    madlibs()
