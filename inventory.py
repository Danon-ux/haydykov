class Item:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
    def add_item(name, description, quantity):
        new_item = Item(name, description, quantity)
        inventory.append(new_item)
    def remove_item(item_name):
    for item in inventory:
        if item.name == item_name:
            inventory.remove(item)
            return True
    return False
    def show_inventory():
        print("Ваш инвентарь:")
        for item in inventory:
            print(f"{item.name}: {item.description}")
inventory = []
add_item("Меч", "Острый меч для сражений", 1)
add_item("Щит", "Прочный щит для защиты", 2)
remove_item("Меч")


  
