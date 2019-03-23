import json
from math import pi

class Agent:

    def __init__(self, position, **attr):
        self.position = position
        for attribute_name, attribute_value in attr.items():
            setattr(self, attribute_name, attribute_value)
    
    def sayHello(self, str) :
        return "Hello " + str

class Position:
    def __init__(self, longitude_deg, latitude_deg):
        self.longitude_deg = longitude_deg
        self.latitude_deg = latitude_deg

    @property
    def longitude(self):
        #longitude en radian
        return self.longitude_deg * pi / 180

    @property
    def latitude(self):
        #latitude en radian
        return self.latitude_deg * pi / 180
        
        
def main():    
    for agents_attributes in json.load(open("agents-100k.json")):
        latitude = agents_attributes.pop('latitude')
        longitude = agents_attributes.pop('longitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agents_attributes)
        print(agent.position.longitude)

main()

