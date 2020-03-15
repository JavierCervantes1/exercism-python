def converter(period):
    def inside(self):
        return round(self.seconds / period, 2)
    return inside

class SpaceAge:
    on_mercury = converter(7600530.24)
    on_venus = converter(19413907.2)
    on_earth = converter(31558149.76)
    on_mars = converter(59354294.4)
    on_jupiter = converter(374335776.0)
    on_saturn = converter(929596608.0)
    on_uranus = converter(2651370019.3)
    on_neptune = converter(5200418592.0)
    
    def __init__(self, seconds):
        self.seconds = seconds
