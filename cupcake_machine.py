class cupcakemachine:
    def __init__(self, cupcakes, cost):
        self.cupcakes = cupcakes
        self.cost = cost

    def add_stock(self, cupcakes, cost):
        self.cupcakes += cupcakes
        self.cost = cost
        print(f"successfully added {cupcakes} cupcakes at ${cost} each")

    def takeorder(self, cupcakes):
        if self.cupcakes >= cupcakes:
            self.cupcakes -= cupcakes
            cost = cupcakes * self.cost
            return "your git push -u origin mainorder of cupcakes costs: " + str(cost)
        else:
            return "Not enough cupcakes in stock"

machine = cupcakemachine(10, 2.5)
machine.add_stock(1000000, 2.5) 
print(machine.takeorder(1000)) 

