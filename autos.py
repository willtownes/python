class Automobile(object):
    color = 'Black'
    door_count = 0
    wheel_count = None
    public_transit = False

#this is a method
    def __init__(self, color=None, door_count=None, wheel_count=None, public_transit=None):
        if color is not None:
            self.color = color
        if door_count is not None:
            self.door_count = door_count
        if wheel_count is not None:
            self.wheel_count = wheel_count
        if public_transit is not None:
            self.public_transit = public_transit

    def autostatus(self):
        print self.color
        print self.door_count
        print self.wheel_count
        print self.public_transit

        
