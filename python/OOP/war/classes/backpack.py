

class Backpack:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return self
    
    def show_backpack(self):
        print(f'You have {len(self.items)} items in your backpack')
        for item in self.items:
            
            print(f"Name: {item.name}\nDescription: {item.effect_desc}")
        return self
    
    def consum_item(self, item_to_consum):
        for item in self.items:
            if item.id == item_to_consum.id:
                print(f"consuming {item_to_consum.name} ")
                self.items.remove(item)
                print(f"removed {item_to_consum.name} from inventory")
                return self