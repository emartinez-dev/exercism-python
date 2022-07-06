class SpaceAge:
    def __init__(self, seconds):
        EARTH_YEAR = 31557600
        self.earth = seconds / EARTH_YEAR
        pass
    
    def on_mercury(self):
        MERCURY = .2408467
        return round(self.earth / MERCURY, 2)

    def on_venus(self):
        VENUS = .61519726
        return round(self.earth / VENUS, 2)

    def on_earth(self):
        return round(self.earth, 2)
    
    def on_mars(self):
        MARS = 1.8808158
        return round(self.earth / MARS, 2)

    def on_jupiter(self):
        JUPITER = 11.862615
        return round(self.earth / JUPITER, 2)

    def on_saturn(self):
        SATURN = 29.447498
        return round(self.earth / SATURN, 2)
    
    def on_uranus(self):
        URANUS = 84.016846
        return round(self.earth / URANUS, 2)

    def on_neptune(self):
        NEPTUNE = 164.79132
        return round(self.earth / NEPTUNE, 2)
