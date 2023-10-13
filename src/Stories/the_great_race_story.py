""" The Great Race"""

from . import constant as cons
from .story import Story

the_great_race = Story(" The Great Race", 2)

inputs_1 = [
    cons.NAME_1,
    cons.NAME_2,
    cons.EVENT_1,
    cons.ADJECTIVE_1,
    cons.VEHICLE_1,
    cons.COLOR_1,
    cons.VEHICLE_2,
    cons.PLACE_1,
    cons.OBSTACLE_1,
    cons.OBSTACLE_2,
]

paragraph_1 = (
    f"{cons.NAME_1} and {cons.NAME_2} were fierce competitors in the annual "
    f"{cons.EVENT_1}. {cons.NAME_1} chose a {cons.ADJECTIVE_1} \n"
    f"{cons.VEHICLE_1} for the race, while {cons.NAME_2} opted for a "
    f"{cons.COLOR_1} {cons.VEHICLE_2}. They raced through \n{cons.PLACE_1},"
    f" dodging {cons.OBSTACLE_1} and {cons.OBSTACLE_2} along the way.\n"
)


inputs_2 = [
    cons.ADJECTIVE_2,
    cons.NAME_1,
    cons.NUMBER_1,
    cons.ADJECTIVE_3,
    cons.SOUND_1,
    cons.NAME_1,
    cons.PRIZE_1,
    cons.ADJECTIVE_4
]

paragraph_2 = (
   f"As they approached the finish line, both competitors were neck and neck. "
   f"\nIn a {cons.ADJECTIVE_2} finish, {cons.NAME_1} managed to pull ahead by "
   f"just {cons.NUMBER_1} seconds, thanks to \na {cons.ADJECTIVE_3} maneuver. "
   f"The crowd erupted in {cons.SOUND_1}, and {cons.NAME_1} was awarded the "
   f"{cons.PRIZE_1}, \nbecoming a {cons.ADJECTIVE_4} legend in the process."
)

the_great_race.set_paragraph(1, paragraph_1)
the_great_race.set_paragraph(2, paragraph_2)
the_great_race.set_input(1, inputs_1)
the_great_race.set_input(2, inputs_2)

# the_great_race.print_story()
