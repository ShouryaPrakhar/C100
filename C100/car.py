class Car(object):
    def __init__(self , model , color , company , speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("Accelerating")


    def changeGear(self):
        print("Gear Changed")

ferrari = Car("Ferrari1A Version7" , "Yellow" , "Ferrari" , "250mph")

print("Model:"+ ferrari.model)
print("Car Color:"+ ferrari.color)
print("Company which made it:"+ ferrari.company)
print("Max Speedlimit:"+ ferrari.speedLimit)

print(ferrari.start())
print(ferrari.changeGear())
print(ferrari.accelarate())
print(ferrari.stop())