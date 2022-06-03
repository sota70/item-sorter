from dataclasses import replace
from itemstack import ItemStack

class Chest:

    def __init__(self, contents_size: int, display_name: str):
        air = ItemStack("air", 0)
        self.contents = [air for i in range(contents_size)]
        self.contents_size = contents_size
        self.display_name = display_name

    def sort(self):
        for i in range(self.contents_size):
            for j in range(self.contents_size - i - 1):
                if self.contents[j].get_id() < self.contents[j + 1].get_id(): continue
                self.contents[j], self.contents[j + 1] = self.contents[j + 1], self.contents[j]

    def put_items(self, items: list[ItemStack]):
        for new_item in items:
            found_empty_slot = self.put_item(new_item)
            if not found_empty_slot: return

    def put_item(self, item: ItemStack) -> bool:
        replace_succeed = False
        for current_item_idx in range(self.contents_size):
            if replace_succeed: break
            current_item = self.contents[current_item_idx]
            current_item_id = current_item.get_id()
            if current_item_id != item.get_id():
                if current_item_id != 0: continue
                self.contents[current_item_idx] = item
                replace_succeed = True
                continue
            total_size = current_item.count + item.count
            if total_size <= current_item.get_max_stackable_size():
                current_item.count += item.count
                replace_succeed = True
                continue
            rest = current_item.get_max_stackable_size() - current_item.count
            current_item.count = current_item.get_max_stackable_size()
            item.count -= rest
        return replace_succeed