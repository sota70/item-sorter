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
                print(item.display_name)

                # self.__put_item(item, store_chest)

    def __put_item(self, item: ItemStack, chest: StoreChest):
        pass