from __future__ import annotations
from abc import ABC,abstractmethod


class JourneyToAirport(ABC):
    @abstractmethod
    def travel(self):
        pass
class ByBus(JourneyToAirport):
    def travel(self):
        print("traveling by bus")
class ByOla(JourneyToAirport):
    def travel(self):
        print("traveling by Ola")
class ByRapido(JourneyToAirport):
    def travel(self):
        print("traveling by Rapido")
        
class Context():
    def __init__(self, journeytoairport : JourneyToAirport):
        self._journeytoairport = journeytoairport
    
    #getter    
    @property
    def journeytoairport(self):
        return self._journeytoairport
    
    #setter
    @journeytoairport.setter
    def journeytoairport(self, journeytoairport):
        self._journeytoairport = journeytoairport
        
    def gotoairport(self):
        self._journeytoairport.travel()

context = Context(ByBus())        
choice = int(input("Enter choice. 1 for bus, 2 for rapido and 3 for ola:"))
if (choice == 1):
    context.journeytoairport = ByBus()
if (choice == 2):
    context.journeytoairport = ByRapido()
if (choice == 3):
    context.journeytoairport = ByOla()
    
context.gotoairport()
    
    
    
    

    
        
        
        
        