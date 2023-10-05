"""The Mysterious Forest"""
import constant as cons
from story import Story

mysterious_forest = Story("The Mysterious Forest", 2)

inputs_1 = [
    cons.ADJECTIVE_1,
    cons.ANIMAL_1,
    cons.COLOR_1,
    cons.CLOTHING_1,
    cons.FOOD_1,
    cons.ADJECTIVE_2,
    cons.CREATURE_1,
    cons.OBJECT_1,
    cons.ADJECTIVE_3,
]

paragraph_1 = (
    f"Once upon a time, in a {cons.ADJECTIVE_1} forest, "
    f"there lived a {cons.ANIMAL_1}.\n"
    f"This {cons.ANIMAL_1} always wore a {cons.COLOR_1} {cons.CLOTHING_1} "
    f"and loved to eat {cons.FOOD_1}.\n"
    f"One day, it stumbled upon a {cons.ADJECTIVE_2} {cons.CREATURE_1} "
    f"who was searching for a {cons.OBJECT_1}.\n"
    f"Intrigued, they decided to join forces for a {cons.ADJECTIVE_3} "
    f"adventure.\n"
)


inputs_2 = [
    cons.ADJECTIVE_4,
    cons.NOUN_1,
    cons.ADVERB_1,
    cons.ADJECTIVE_5,
    cons.TIME_1,
    cons.OBJECT_1,
    cons.MONSTER_1,
    cons.TOOL_1,
]

paragraph_2 = (
    f"After walking for what seemed like {cons.TIME_1}, "
    f"they finally found the {cons.OBJECT_1} hidden under a {cons.NOUN_1}.\n"
    f"But just as they were about to celebrate, a {cons.ADJECTIVE_4} "
    f"{cons.MONSTER_1} appeared.\n"
    f"With quick thinking and a {cons.TOOL_1}, they managed to "
    f"scare it away.\n"
    f"The two became {cons.ADJECTIVE_5} friends and lived {cons.ADVERB_1} "
    f"ever after."
)

mysterious_forest.set_paragraph(1, paragraph_1)
mysterious_forest.set_paragraph(2, paragraph_2)
mysterious_forest.set_input(1, inputs_1)
mysterious_forest.set_input(2, inputs_2)

print(mysterious_forest.get_title())
print(mysterious_forest.get_paragraph(1))
print(mysterious_forest.get_paragraph(2))
