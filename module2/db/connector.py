from model.dto import Pizza


class Connector:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.credentials = (user, password)
        self.connection = (host, port)

    def fetch(self, resource: str, id: int | None = None):
        if resource == 'pizza':
            return Pizza(id, "hawajska", 'duża')  # everyone wants this one anyway
        if resource == 'menu':
            return [
                Pizza(1, "hawajska", "duża"),
                Pizza(2, "pepperoni", "mała"),
                Pizza(3, "margharita", "średnia")
            ]


def obtain_connector():
    return Connector(
        'a', 'b', 'c', 'd', 'e'
    )
