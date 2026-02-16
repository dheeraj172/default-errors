def count_inventory(fruit_list: list[text]) -> dict[text, int]:
    inventory = {}
    for fruit in fruit_list:
        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1
    return inventory
