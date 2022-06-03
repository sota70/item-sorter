from chest import Chest
from itemstack import ItemStack
from store_chest import StoreChest

class ChestSorter:

    def __init__(self, temp_chest: Chest, store_chests: list[StoreChest]):
        self.__temp_chest = temp_chest
        self.__store_chests = store_chests

    def sort(self):
        for item in self.__temp_chest.contents:
            for store_chest in self.__store_chests:
                if not item.get_id() in store_chest.get_filters(): continue
                # debug
                print(f"{item.display_name}({item.count}) in {store_chest.display_name}")

                # self.__put_item(item, store_chest)