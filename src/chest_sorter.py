from chest import Chest
from itemstack import ItemStack
from store_chest import StoreChest

class ChestSorter:

    def __init__(self, temp_chest: Chest, store_chests: list[StoreChest]):
        self.__temp_chest = temp_chest
        self.__store_chests = store_chests

    def sort(self):
        for item_idx in range(self.__temp_chest.contents_size):
            self.__sort(item_idx)

    def __sort(self, item_idx):
        for store_chest in self.__store_chests:
            temp_item = self.__temp_chest.contents[item_idx]
            temp_item_id = temp_item.get_id()
            if not temp_item_id in store_chest.get_filters(): continue
            replace_succeed = store_chest.put_item(temp_item)
            if not replace_succeed: continue
            self.__temp_chest.contents[item_idx] = ItemStack("air", 0)
            break

    def register_store_chest(self, store_chest: StoreChest):
        store_chest_id = store_chest.get_id()
        has_same_chest = False
        for s_chest in self.__store_chests:
            if s_chest.get_id() != store_chest_id: continue
            has_same_chest = True
            break
        if has_same_chest:
            print("Already registered this store chest")
            return
        self.__store_chests.append(store_chest)

    def set_temp_chest(self, temp_chest: Chest):
        if isinstance(temp_chest, StoreChest):
            print("This is not a temp chest")
            return
        self.__temp_chest = temp_chest