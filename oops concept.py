class Car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
        carObj=Car()
        carObj.sample_car_instance_method("hello again!")
        carObj2=Car()
        carObj2.sample_car_instance_method(2)
#sound horn:
#print "beep beep" if car engine is on
#print"car has not started yet" if car engine is off
class MethodExample:
    engine=On
    obj=MethodExample()
    obj.car()
    print(obj.engine)
###
class ClassMethodExample:
    classVar1=False
    classVar2="ON"
    @classmethod
    def sample_class_method(self):
        self.classVar1=True
        self.classVar2="OFF"
ClassMethodExample.sample_class_method()
print(ClassMethodExample.classVar1)
print(ClassMethodExample.classVar2)
##
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
    def stop_engine(self):
        self.start_engine = False
        print("Engine stopped")
    def sound_horn(self):
        if(self.start_engine):
            print("Beep Beep")
        else:
            print("Engine is not started")
    def Apply_brakes(self):
        if self.currentspeed>0 and self.currentspeed>=self.tyre_friction:
            print("appling brakes")
        else:
            print("not applicable brakes")

carObj = Car()
carObj.startEngine()
carObj.stop_engine()
carObj.startEngine()
carObj.sound_horn()

print(Car.StartEngine)
print("The Car Engine is:",Car.StartEngine)







