import json
from math import pi

class Agent:

    def __init__(self, position, **attr):
        self.position = position
        for attribute_name, attribute_value in attr.items():
            setattr(self, attribute_name, attribute_value)

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

class Zone:
    
    ZONES = []
    MIN_LONGITUDE_DEG = -180
    MAX_LONGITUDE_DEG = 180
    MIN_LATITUDE_DEG = -90
    MAX_LATITUDE_DEG = 90
    WIDTH_DEG = 1
    HEIGHT_DEG = 1
    
    def __init__(self, corner_left, corner_right):
        self.corner_left = corner_left
        self.corner_right = corner_right
        self.inhabitants = []

    def add_inhabitants(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def contains(self, position):
        return position.longitude >= min(self.corner_left.longitude,
                                         self.corner_right.longitude) and \
            position.longitude < max(self.corner_left.longitude,
                                     self.corner_right.longitude) and \
            position.latitude >= min(self.corner_left.latitude,
                                     self.corner_right.latitude) and \
            position.latitude < max(self.corner_left.latitude,
                                    self.corner_right.latitude)

    @property
    def population(self):
        return len(self.inhabitants)

    @classmethod
    def initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEG,
                              cls.MAX_LATITUDE_DEG,
                              cls.HEIGHT_DEG):
            for longitude in range(cls.MIN_LONGITUDE_DEG,
                                   cls.MAX_LONGITUDE_DEG,
                                   cls.WIDTH_DEG):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEG,
                                            latitude + cls.HEIGHT_DEG)
                zone = Zone(bottom_left_corner,top_right_corner)
                cls.ZONES.append(zone)

    @classmethod
    def find_zone_that_contains(cls, position):
        # Compute the index in the ZONES array that contains the given position
        longitude_index = int((position.longitude_deg
                               - cls.MIN_LONGITUDE_DEG)
                               / cls.WIDTH_DEG)
        latitude_index = int((position.latitude_deg
                              - cls.MIN_LATITUDE_DEG)
                              / cls.HEIGHT_DEG)
        longitude_bins = int((cls.MAX_LONGITUDE_DEG
                              - cls.MIN_LONGITUDE_DEG)
                             / cls.WIDTH_DEG) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone
        
        
def main():
    Zone.initialize_zones()
    for agents_attributes in json.load(open("agents-100k.json")):
        latitude = agents_attributes.pop('latitude')
        longitude = agents_attributes.pop('longitude')
        position = Position(longitude, latitude)
        agent = Agent(position, **agents_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitants(agent)
        print("Zone population: ", zone.population)
main()

