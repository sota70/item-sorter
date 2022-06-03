class ItemStack:

    def __init__(self, display_name: str, id: int, max_stackable_size: int=64, count: int=1):
        self.display_name = display_name
        self.__id = id
        self.__max_stackable_size = max_stackable_size
        self.count = count

    def get_id(self) -> int:
        return self.__id

    def get_max_stackable_size(self) -> int:
        return self.__max_stackable_size

    def merge(self, item: any):
        if not isinstance(item, ItemStack):
            raise Exception("item parameter is not ItemStack type")
        total_size = self.count + item.count
        if total_size <= self.__max_stackable_size:
            self.count += item.count
            item.count = 0
            # item count 0 means air so it returns air itemstack
            return ItemStack("air", 0)
        rest = self.__max_stackable_size - self.count
        self.count = self.__max_stackable_size
        item.count -= rest
        return item