class Car:
    color="Orange"
    maxspeed=165
    acceleration=30
    tyre_friction=10
    start_engine=False
    currentspeed=65


    def startEngine(self):
        self.start_engine=True
        print("Enigne Started")
        print("car is started")
    def stop_engine(self):
        self.stop_engine = False
        print("Engine stopped")
        print("car not started yet")
    def sound_horn(self):
        if(self.start_engine):
            print("Beep Beep")
        else:
            print("Engine is not started")
    def Apply_brakes(self):
        if self.currentspeed>0 and self.currentspeed>=self.tyre_friction:
            self.currentspeed-=self.tyre_friction
            print("appling brakes")
            print("current speed:",self.currentspeed)
        else:
            print("not applicable brakes")
    def Apply_Acceleration(self):
        if self.currentspeed<self.maxspeed:
            self.currentspeed+=self.acceleration
            print("applied acceleration")
        else:
            print("not applied acceleration")

carObj = Car()
carObj.startEngine()
carObj.stop_engine()
carObj.startEngine()
carObj.sound_horn()
carObj.Apply_brakes()
carObj.Apply_Acceleration()





