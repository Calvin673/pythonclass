class cupcakemachine:
    def __init__(self, cupcakes, cost):
        self.cupcakes = cupcakes
        self.cost = cost
        self.order_number = 0

    def add_stock(self, cupcakes, cost):
        self.cupcakes += cupcakes
        self.cost = cost
        print(
            f"successfully added {cupcakes} cupcakes at ${cost} each. Total cupcakes: {self.cupcakes}")

    def takeorder(self, cupcakes):
        if self.cupcakes > cupcakes:
            self.cupcakes -= cupcakes
            cost = cupcakes * self.cost
            self.order_number += 1
            print(
                f"order number {self.order_number} of cupcakes costs: {cost}")

        else:
            self.order_number += 1
            print(f"order number {self.order_number} cannot be filled")


machine = cupcakemachine(10, 1.75)
machine.takeorder(2)
machine.takeorder(3)
machine.takeorder(10)
machine.takeorder(1)