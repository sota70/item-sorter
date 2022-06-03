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