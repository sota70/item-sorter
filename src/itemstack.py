class ItemStack:

    def __init__(self, display_name: str, id: int):
        self.display_name = display_name
        self.__id = id

    def get_id(self) -> int:
        return self.__id