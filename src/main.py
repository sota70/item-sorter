from chest import Chest
from chest_sorter import ChestSorter
from itemstack import ItemStack
from store_chest import StoreChest

dirt_block = ItemStack("dirt", 1)
wood_block = ItemStack("wood", 2)
coal = ItemStack("coal", 3)
temp_chest = Chest(27, "Temporary Chest")
temp_chest.put_items([
    dirt_block, dirt_block, dirt_block,
    wood_block, wood_block,
    coal
])
store_chest1 = StoreChest(27, [ 1 ], "Storage1")
store_chest2 = StoreChest(27, [ 2, 3 ], "Storage2")
chest_sorter = ChestSorter(temp_chest, [ store_chest1, store_chest2 ])
chest_sorter.sort()