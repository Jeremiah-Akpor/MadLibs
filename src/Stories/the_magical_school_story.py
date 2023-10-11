"""The Magical School"""
# pylint: disable=import-error
from story import Story
import constant as cons


the_magical_school = Story("     The Magical School", 2)

inputs_1 = [
    cons.ADJECTIVE_1,
    cons.NOUN_1,
    cons.PROFESSION_1,
    cons.NAME_1,
    cons.ADJECTIVE_2,
    cons.PLACE_1,
    cons.MAGIC_WORD_1,
    cons.OBJECT_1,
    cons.ANIMAL_1,
    cons.NAME_2,
    cons.ADJECTIVE_3
]

paragraph_1 = (
    f"In a {cons.ADJECTIVE_1} school for aspiring {cons.NOUN_1}, "
    f"a young {cons.PROFESSION_1}  named \n{cons.NAME_1} discovered"
    f" a {cons.ADJECTIVE_2} spellbook in the {cons.PLACE_1}. \n"
    f"The first spell they tried was ´{cons.MAGIC_WORD_1}´, "
    f"which turned \ntheir {cons.OBJECT_1} into a {cons.ANIMAL_1}. "
    f"Their best friend, {cons.NAME_2}, was so {cons.ADJECTIVE_3} \n"
    f"that they decided to explore further.\n"
)

inputs_2 = [
    cons.ADJECTIVE_4
]

paragraph_2 = (
    f"The duo then found a {cons.ADJECTIVE_4} potion recipe. "
    f"After gathering all \nthe {cons.INGREDIENT_1} and "
    f"chanting the {cons.MAGIC_WORD_2}, they took a sip. To "
    f"their {cons.EMOTION_1}, \ntheir {cons.EMOTION_1}, they"
    f" gained the ability to {cons.VERB_1}. They became the \n"
    f"talk of the school  and went on to have many more "
    f"{cons.ADJECTIVE_5} adventures."
)

the_magical_school.set_paragraph(1, paragraph_1)
the_magical_school.set_paragraph(2, paragraph_2)
the_magical_school.set_input(1, inputs_1)
the_magical_school.set_input(2, inputs_2)

the_magical_school.print_story()
