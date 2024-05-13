from Container import Container
from Sheet import Sheet

if __name__ == '__main__':
    # make the containers

    # left row
    character_name = Container(40, 10)
    character_desc = Container(60, 15)
    stats = Container(10, 50)
    inspiration = Container(20, 5)
    prof_bonus = Container(20, 5)
    saving_throws = Container(20, 15)
    skills = Container(20, 35)
    passive_wisdom = Container(30, 5)
    tool_profs = Container(30, 20)
    other_profs = Container(30, 20)

    # middle row
    armor_class = Container(,)
    initiative = Container(,)
    speed = Container(,)
    hp_max = Container(,)
    hp = Container(,)
    temp_hp = Container(,)
    hit_dice = Container(,)
    death_saves = Container(,)
    exhaustion = Container(,)
    attacks = Container(,)
    equipment = Container(,)

    # right row
    personality_traits = Container(,)
    ideals = Container(,)
    bonds = Container(,)
    flaws = Container(,)
    resource_1 = Container(,)
    resource_2 = Container(,)
    resource_3 = Container(,)
    resource_4 = Container(,)
    character_traits = Container(,)

    # add the containers to the sheet
    sheet = Sheet()
    sheet.add_container(character_name, 0, 0)
    sheet.add_container(character_desc, 40, 0)
