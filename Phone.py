from Item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # call to super functions to have access to all attributes/ methods
        super().__init__(
            name, price, quantity
        )

        # Run validations ti the received arguments
        assert broken_phone >= 0, f'Broken Phones {broken_phone} is not greater than zero'

        # Assign to self object

        self.broken_phone = broken_phone
