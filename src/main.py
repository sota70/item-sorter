from chest import Chest
from chest_sorter import ChestSorter
from store_chest import StoreChest

temp_chest = Chest(27)
store_chest1 = StoreChest(27, [ 1 ])
chest_sorter = ChestSorter(temp_chest, [ store_chest1 ])
chest_sorter.sort()