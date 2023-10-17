"""
This module contains the function to get the stories from
the stories folder. """
import glob
import logging
from .custom_exception import StoryException

# Get the logger
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def get_stories():
    """Get a list of all story files in the 'stories' directory"""

    logging.info("GET_STORIES: ---Starting to collect stories.---")
    try:
        # Get all story files
        story_files = glob.glob("src/stories/*_story.py")
        logging.info("GET_STORIES: Found story files: %s", story_files)

        stories = []
        for story in story_files:
            story = story.split("\\")[1]
            story = story.split("_story")[0]
            stories.append(story)

        logging.info(
            "GET_STORIES: Successfully collected stories: %s", stories)
        logging.info(
            "GET_STORIES: Number of stories: %s", len(stories))
        return stories
    except StoryException as e:
        logging.error(
            "GET_STORIES: An error occurred while collecting stories: %s", e)
        return []
