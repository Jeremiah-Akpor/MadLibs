"A class to represent a Mad Libs story."
from custom_exception import StoryException


class Story:
    """
    Attributes
    ----------
    title : str
        The title of the Mad Libs story.
    Paragraph1 : str
        The 1st paragraph of the story.
    Paragraph2 : str
        The 2nd paragraph of the story.
    InputOfParagraph1 : list
        The list of user inputs for paragraph 1.
    InputOfParagraph2 : list
        The list of user inputs for paragraph 2.

    Methods
    -------
    __init__(self, title, pg1, pg2, input_pg1, input_pg2):
    get_title(self): str
    get_paragraph(num): str
    get_input(num): list
    """

    def __init__(self, title, num_of_paragraph):
        """
        Parameters
        ----------
        title : str
            The title of the Mad Libs story.
        num_of_paragraph : int
            The number of paragraph in the story.
        paragraphs : dict
            A dictionary containing the list of paragraphs.
        input_of_paragraph : dict
            A dictionary containing the list of user
            inputs for each paragraph.
        has_paragraph : boolean
            this will be set to true if the paragraph
            has been set
        has_input: boolean
            this will be set to true if the inputs of
            the paragraph has been set

        """
        self.title = title
        self.num_of_paragraph = num_of_paragraph
        self.paragraphs = {}
        self.input_of_paragraph = {}
        self.has_paragraph = False
        self.has_input = False

    def get_title(self):
        """Return the title of the story."""
        return self.title

    def get_paragraph(self, num):
        """Return the paragraph of the story."""
        if not self.has_paragraph:
            raise StoryException(
                "The story does not contain any paragraph"
            )
        if num > self.num_of_paragraph | num <= 0:
            raise StoryException(
                f'the number of paragraph is {self.num_of_paragraph}')
        return self.paragraphs[num]

    def get_inputs(self, num):
        """Return the list of inputs depending
        on the paragraph in the story"""
        if not self.has_input:
            raise StoryException(
                "The paragraphs does not contain any user input"
            )
        if num > self.num_of_paragraph | num <= 0:
            raise StoryException(
                f'the number of paragraph is {self.num_of_paragraph}')
        return self.input_of_paragraph[num]
