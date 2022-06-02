from itemstack import ItemStack

class Chest:

    def __init__(self, contents_size: int):
        air = ItemStack("air", 0)
        self.contents = [air for i in range(contents_size)]
        self.contents_size = contents_size

    def sort(self):
        for i in range(self.contents_size):
            for j in range(self.contents_size - i - 1):
                if self.contents[j] < self.contents[j + 1]: continue
                self.contents[j], self.contents[j + 1] = self.contents[j + 1], self.contents[j]

    def put_items(self, items: list[ItemStack]):
        for new_item in items:
            found_empty_slot = False
            for current_item_idx in range(self.contents_size):
                current_item_id = self.contents[current_item_idx].get_id()
                if current_item_id == 1: continue
                self.contents[current_item_idx] = new_item
                found_empty_slot = True
            if not found_empty_slot: return