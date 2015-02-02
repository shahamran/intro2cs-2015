import math
from baseObject import BaseObject
from objectShapes import TORPEDO_SHAPE

class HeatSeeker(BaseObject):
    
    RADIUS = 4
    TORPEDO_LIFESPAN = 100
    
    def __init__(self,canvas,x,y,dx,dy,direction,asteroid,axis_min,axis_max):
        super().__init__(canvas,x,y,dx,dy,TORPEDO_SHAPE,direction,HeatSeeker.RADIUS)
        self.set_color("Cyan")
        self.lifespan = HeatSeeker.TORPEDO_LIFESPAN 
        self.asteroid = asteroid
        self.axis_min = axis_min
        self.axis_max = axis_max

    def get_life_span(self):
        return self.lifespan
    
    def get_asteroid(self):
        """
        Get the asteroid that the missile is tracking.
        :return: Asteroid (baseObject)
        """
        return self.asteroid

    def get_type(self):
        """
        Returns a string that specify the type of torpedo
        """
        return "missile"

    def move(self,fake_x,fake_y):
        """
        Tracks the asteroid!!!
        fake_x and fake_y are not used in this method, they are only for the
        similarity to the PhotonTorpedo object.
        """
        x,y = self.get_x_cor(), self.get_y_cor()
        position = (x,y)
        self.lifespan -= 1
        axis_min, axis_max = self.axis_min, self.axis_max
        asteroid = self.asteroid
        speed = ( self.get_speed_x(), self.get_speed_y() )
        angle = self.get_angle()

        a_x,a_y = asteroid.get_x_cor(), asteroid.get_y_cor()
        # calculates the angle to face the asteroid (the slope of the line
        # that connects the torpedo and the asteroid)
        if a_x == x:
            slope = 90 if a_y > y else 270
        else:
            slope = math.degrees( math.atan((a_y - y) / (a_x - x)) )
        if a_x < x : slope += 180

        angle = slope
        new_angle = math.radians(angle)
        self.set_angle(angle)
        factor = ( math.cos(new_angle) , math.sin(new_angle) )
        
        new_speed = [0,0]
        new_cord = [0,0]
        for i in range(2):
            new_speed[i] = 0.9 * speed[i] + 0.5 * factor[i]
            delta = axis_max[i] - axis_min[i]
            new_cord[i] = (new_speed[i] + position[i] - axis_min[i]) % \
                                            delta + axis_min[i]
        self.set_speed_x(new_speed[0])
        self.set_speed_y(new_speed[1])
        super().move(new_cord[0],new_cord[1])
