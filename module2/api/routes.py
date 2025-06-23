from db.retriever import Retriever

def get_pizza(id: int):
    retriever = Retriever()
    return retriever.get_pizza(id)

def get_menu():
    retriever = Retriever()
    return retriever.get_menu()
