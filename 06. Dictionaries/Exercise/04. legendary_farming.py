elements = input().lower()
elements = elements.split(" ")

shards = 0
fragments = 0
motes = 0

resource_for_obtaining = ''

junk_item_dictionary = {}
legendary_item_dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}

key_materials_reached = False

while not key_materials_reached:

    for el in range(0, len(elements), 2):
        current_item = elements[el + 1]
        quantity = int(elements[el])

        if current_item == "motes":
            motes += quantity
        elif current_item == "shards":
            shards += quantity
        elif current_item == "fragments":
            fragments += quantity

        if motes >= 250:
            motes -= 250
            legendary_item_dictionary[current_item] = motes
            resource_for_obtaining = 'motes'
            key_materials_reached = True
            break
        elif fragments >= 250:
            fragments -= 250
            legendary_item_dictionary[current_item] = fragments
            resource_for_obtaining = 'fragments'
            key_materials_reached = True
            break
        elif shards >= 250:
            shards -= 250
            legendary_item_dictionary[current_item] = shards
            resource_for_obtaining = 'shards'
            key_materials_reached = True
            break

        if current_item == "motes" or current_item == "shards" or current_item == "fragments":
            legendary_item_dictionary[current_item] += quantity
        else:
            if current_item not in junk_item_dictionary:
                junk_item_dictionary[current_item] = quantity
            else:
                junk_item_dictionary[current_item] += quantity

    if not key_materials_reached:
        elements = input().lower()
        elements = elements.split(" ")

if resource_for_obtaining == "shards":
    print(f"Shadowmourne obtained!")
elif resource_for_obtaining == "fragments":
    print(f"Valanyr obtained!")
elif resource_for_obtaining == "motes":
    print(f"Dragonwrath obtained!")


for (key_material_name, key_material_qty) in legendary_item_dictionary.items():
    print(f'{key_material_name}: {key_material_qty}')

for (junk_material_name, junk_material_qty) in junk_item_dictionary.items():
    print(f"{junk_material_name}: {junk_material_qty}")
