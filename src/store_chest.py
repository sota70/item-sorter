from chest import Chest

class StoreChest(Chest):

    def __init__(
        self,
        contents_size: int,
        filters: list[int],
        display_name: str,
        id: int
    ):
        super().__init__(contents_size, display_name, id)
        self.__filters = filters

    def get_filters(self) -> list[int]:
        return self.__filters