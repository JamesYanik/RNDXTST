

class Retriever:
    def __init__(self):
        self.__connector = "a"

    def get_pizza(self, id: int):
        return self.__connector.fetch("pizza", id)

    def get_menu(self):
        return self.__connector.fetch("menu")
