"A class to represent a Mad Libs story."
from .custom_exception import StoryException


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
    __init__(self, title, num_of_paragraph):
    set_paragraph(self, key, new_paragraph): str
    set_input(self, key): list
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

    def set_paragraph(self, key, new_paragraph):
        """This function sets or updates a paragraph in the story.

        Parameters:
            key (int): to identify the paragraph
            new_paragraph (str): content of new paragraph"""
        if key > self.num_of_paragraph or key < 1:
            raise StoryException(
                f"The number of paragraphs is {self.num_of_paragraph}")
        self.paragraphs[key] = new_paragraph
        self.has_paragraph = True

    def set_input(self, key, new_inputs):
        """set or update the user input for the paragraph in the story.
        parameters:
            key(int): to identify the paragraph
            new_inputs(list): list of user input for the paragraph
        """
        if key not in self.paragraphs:
            raise StoryException(
                f"Paragraph '{key}' doesn't exist."
                " Please set the paragraph first")
        self.input_of_paragraph[key] = new_inputs
        self.has_input = True

    def get_title(self):
        """Return the title of the story."""
        return self.title

    def get_paragraph(self, num):
        """Return the paragraph of the story."""
        if not self.has_paragraph:
            raise StoryException("The story does not contain any paragraph")
        return self.paragraphs.get(num, "Paragraph not found")

    def get_inputs(self, num):
        """Return the list of inputs depending
        on the paragraph in the story"""
        if not self.has_input:
            raise StoryException(
                "The paragraphs do not contain any user input")
        return self.input_of_paragraph.get(num, [])

    def update_story(self, paragraph_num, user_inputs):
        """
            Update a specific paragraph in the story with user-provided inputs.

            Parameters:
            - paragraph_num (int): The number of the paragraph to update.
            - user_inputs (list): A list of user inputs to replace
            placeholders in the paragraph.

            Raises:
            - StoryException: If the paragraph number does not exist.
        """
        if paragraph_num not in self.paragraphs:
            raise StoryException(f"Paragraph {paragraph_num} does not exist")

        paragraph = self.paragraphs[paragraph_num]
        placeholders = self.input_of_paragraph.get(paragraph_num, [])

        for i, placeholder in enumerate(placeholders):
            paragraph = paragraph.replace(placeholder, user_inputs[i])

        self.paragraphs[paragraph_num] = paragraph

    def print_story(self):
        """Print the story with the user inputs."""
        if not self.has_paragraph or not self.has_input:
            raise StoryException("The story is incomplete")
        print(self.title)
        for num in range(1, self.num_of_paragraph + 1):
            print(self.get_paragraph(num))
