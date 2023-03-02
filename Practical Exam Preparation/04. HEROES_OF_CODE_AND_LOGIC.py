heroes_to_choose_from = int(input())
hero_names_dict = {}
# index 0 = Health
# index 1 = Mana

for hero in range(heroes_to_choose_from):
    hero_name = input().split()
    hero_names_dict[hero_name[0]] = [int(hero_name[1]), int(hero_name[2])]


current_action = input()

while not current_action == "End":
    split_action = current_action.split(" - ")
    command = split_action[0]

    if command == "CastSpell":
        name_of_hero = split_action[1]
        mana_needed = int(split_action[2])
        spell_name = split_action[3]

        if hero_names_dict[name_of_hero][1] - mana_needed >= 0:
            hero_names_dict[name_of_hero][1] -= mana_needed
            print(f"{name_of_hero} has successfully cast {spell_name} and now has {hero_names_dict[name_of_hero][1]} MP!")
        else:
            print(f"{name_of_hero} does not have enough MP to cast {spell_name}!")


    elif command == "TakeDamage":
        name_of_hero = split_action[1]
        damage = int(split_action[2])
        attacker = split_action[3]

        if hero_names_dict[name_of_hero][0] - damage > 0:
            hero_names_dict[name_of_hero][0] -= damage
            print(f"{name_of_hero} was hit for {damage} HP by {attacker} and now has {hero_names_dict[name_of_hero][0]} HP left!")
        else:
            hero_names_dict.pop(name_of_hero)
            print(f"{name_of_hero} has been killed by {attacker}!")


    elif command == "Recharge":
        name_of_hero = split_action[1]
        amount = int(split_action[2])

        if hero_names_dict[name_of_hero][1] + amount > 200:
            amount = 200 - int(hero_names_dict[name_of_hero][1])
            print(f"{name_of_hero} recharged for {amount} MP!")
            hero_names_dict[name_of_hero][1] = 200
        else:
            hero_names_dict[name_of_hero][1] += amount
            print(f"{name_of_hero} recharged for {amount} MP!")


    elif command == "Heal":
        name_of_hero = split_action[1]
        amount = int(split_action[2])

        if hero_names_dict[name_of_hero][0] + amount > 100:
            amount = 100 - int(hero_names_dict[name_of_hero][0])
            print(f"{name_of_hero} healed for {amount} HP!")
            hero_names_dict[name_of_hero][0] = 100
        else:
            hero_names_dict[name_of_hero][0] += amount
            print(f"{name_of_hero} healed for {amount} HP!")

    current_action = input()


for info in hero_names_dict.items():
    print(info[0])
    print(f"HP: {info[1][0]}")
    print(f"MP: {info[1][1]}")