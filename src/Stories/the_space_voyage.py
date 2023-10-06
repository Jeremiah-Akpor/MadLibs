""" The Space Voyage """
# pylint: disable=import-error
import constant as cons
from story import Story

the_space_voyage = Story("     The Space Voyage", 2)

inputs_1 = [
    cons.NAME_1,
    cons.ADJECTIVE_1,
    cons.PLANET_1,
    cons.SHIP_NAME_1,
    cons.NOUN_1,
    cons.ELEMENT_1,
    cons.NUMBER_1,
    cons.ADJECTIVE_2,
    cons.PHENOMENON_1,
]

paragraph_1 = (
    f"Captain {cons.NAME_1} was ready for the {cons.ADJECTIVE_1} journey to"
    f" Planet {cons.PLANET_1}. \n"
    f"The spaceship, named {cons.SHIP_NAME_1}, was filled with {cons.NOUN_1} "
    f"and powered by {cons.ELEMENT_1}. \n"
    f"After {cons.NUMBER_1} days in space, they encountered a "
    f"{cons.ADJECTIVE_2}  {cons.PHENOMENON_1} that threatened the mission.\n"
)

inputs_2 = [
    cons.TOOL_1,
    cons.ADJECTIVE_3,
    cons.PHENOMENON_1,
    cons.PLANET_1,
    cons.ADJECTIVE_4,
    cons.GIFT_1
]

paragraph_2 = (
    f"To solve the problem, the crew used a {cons.TOOL_1} and followed a"
    f" {cons.ADJECTIVE_3} plan.\n"
    f"After some tense moments, they successfully navigated through the"
    f" {cons.PHENOMENON_1}.\n"
    f"Finally, they landed on Planet {cons.PLANET_1} and were greeted "
    f"by {cons.ADJECTIVE_4} \naliens who offered them {cons.GIFT_1} as a"
    f" token of friendship."
)


the_space_voyage.set_paragraph(1, paragraph_1)
the_space_voyage.set_paragraph(2, paragraph_2)
the_space_voyage.set_input(1, inputs_1)
the_space_voyage.set_input(2, inputs_2)

the_space_voyage.print_story()
