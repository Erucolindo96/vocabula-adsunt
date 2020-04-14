class Age:

    def __init__(self, age_id: int, name: str):
        self.__id = age_id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        id_str = str(self.get_id() if self.get_id() else '')
        name = self.get_name() if self.get_name() else ''
        return "(" + id_str + ", " + name + ")"
