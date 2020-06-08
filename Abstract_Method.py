import abc

class Driver(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass
class HpDriver(Driver):
    def connect(self):
        print("HP printer")
        
class CanonDriver(Driver):
    def connect(self):
        print("Canon printer")
        
class SonyDriver(Driver):
    def connect(self):
        print("Sony printer")
        
class os:
    def install(self,d):
        d.connect()
Windows=os()
HP=HpDriver()
CC=CanonDriver()

SONY=SonyDriver()
Windows.install(HP)
Windows.install(CC)
Windows.install(SONY)


        
        
    