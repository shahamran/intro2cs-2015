from torpedo import *
from asteroid import *
from spaceship import *
from gameMaster import *

class GameRunner:

    def __init__(self, amnt = 3):
        self.game = GameMaster()
        self.screenMaxX = self.game.get_screen_max_x()
        self.screenMaxY = self.game.get_screen_max_y()
        self.screenMinX = self.game.get_screen_min_x()
        self.screenMinY = self.game.get_screen_min_y()
        shipStartX = (self.screenMaxX-self.screenMinX)/2 + self.screenMinX
        shipStartY = (self.screenMaxY-self.screenMinY)/2 + self.screenMinY
        self.game.set_initial_ship_cords( shipStartX, shipStartY )
        self.game.add_initial_astroids(amnt)
        # a list of asteroid sizes and matching scores (size, score)
        self._AST_SIZE = [ (1,100), (2,50), (3,20) ]
        # number of dimensions in which the game works (2 in this case)
        self.DIMS = 2
        # the max number of torpedos allowed on screen
        self.MAX_TORPEDOS = 20
        # the max speed of the spaceship (to get a game that behaves better)
        self.MAX_SHIP_SPEED = 10
        # text for the messages shown in the game (title, message)
        self.LOSE_MSG = ("You LOSE!", \
            "It appears you are allergic to Kryptonite! You lost!")
        self.WIN_MSG = ("You WIN!", \
            "You destroyed all the asteroids! Good Job!")
        self.QUIT_MSG = ("Goodbye", "Game ended by user")
        self.SHIP_LOST_MSG = ("Oops!", "You hit an asteroid!")


    def run(self):
        self._do_loop()
        self.game.start_game()


    def _do_loop(self):
        self.game.update_screen()
        self.game_loop()
        # Set the timer to go off again
        self.game.ontimer(self._do_loop,5)

    
    def _move_object(self, obj):
        """
        Call this method in order to move an object on the screen, according
        to it's speed.

        :param obj: the object to be moved
        :type obj: baseObject
        """

        speed = ( obj.get_speed_x(), obj.get_speed_y() )
        position = ( obj.get_x_cor(), obj.get_y_cor() )
        axis_min = ( self.screenMinX, self.screenMinY )
        axis_max = ( self.screenMaxX, self.screenMaxY )
        new_cord = [0] * self.DIMS
        for i in range(self.DIMS):
            delta = axis_max[i] - axis_min[i]
            new_cord[i] = (speed[i] + position[i] - axis_min[i]) % \
                                            delta + axis_min[i]
        obj.move(new_cord[0], new_cord[1])

        
    def _handle_key_press(self, ship, torpedos, asteroids):
        """
        Checks if one of the game controller keys was pressed and acts
        accordingly if so.
        
        :param ship: the ship
        :type ship: SpaceShip
        :param torpedos: the list of torpedos that are currently on screen
        :type torpedos: list ( of PhotonTorpedo objects )
        :param asteroids: the list of asteroids on screen
        :type asteroids: list ( of Asteroid objects )
        """

        speed = ( ship.get_speed_x(), ship.get_speed_y() )
        pos = ( ship.get_x_cor() , ship.get_y_cor() )
        angle = ship.get_angle()
        angle_rad = math.radians(angle)
        factor = ( math.cos(angle_rad) , math.sin(angle_rad) )

        # handles left key press
        if self.game.is_left_pressed():
            ship.increase_angle()

        # handles right key press
        if self.game.is_right_pressed():
            ship.decrease_angle()

        # handles up key press
        if self.game.is_up_pressed():
            # increase speed only if the ship is not too fast
            total_speed = (speed[0] ** 2 + speed[1] ** 2) ** (1/2)
            if total_speed < self.MAX_SHIP_SPEED:
                new_speed = [0] * self.DIMS
                for i in range(self.DIMS): # sets the desired ship speed
                    new_speed[i] = speed[i] + factor[i]
                ship.set_speed_x(new_speed[0])
                ship.set_speed_y(new_speed[1])

        # handles fire key press
        if self.game.is_fire_pressed():
        # only shoots if there are less than MAX_TORPEDOS torpedos on screen
            if len(torpedos) < self.MAX_TORPEDOS:
                tor_speed = [0] * self.DIMS
                for i in range(self.DIMS): # sets the desired torpedo speed
                    tor_speed[i] = speed[i] + 2 * factor[i]
                self.game.add_torpedo(pos[0], pos[1], tor_speed[0], \
                                                      tor_speed[1], angle)


    def _handle_intersection(self, torpedo, asteroids):
        """
        Checks if a torpedo hit an asteroid and updates the game accordingly.
        
        :param torpedo: the torpedo needed to be checked
        :type torpedo: baseObject ( PhotonTorpedo )
        :param asteroids: a list of asteroids on screen
        :type asteroids: list ( of Asteroid objects )

        :retrun: True if an intersection is made, False otherwise
        """

        is_hit = False
        for asteroid in asteroids:
            if self.game.intersect(torpedo, asteroid):
                # checks what size of asteroid was hit
                for size,score in self._AST_SIZE:
                    if asteroid.get_size() != size: continue
                    if size > 1: # only split an asteroid if it was a big one
                        speed = ( asteroid.get_speed_x(),\
                                  asteroid.get_speed_y() )
                        pos = ( asteroid.get_x_cor(), asteroid.get_y_cor() )
                        tor_speed = ( torpedo.get_speed_x(),\
                                      torpedo.get_speed_y() )
                        size -= 1
                        new_speed = [0] * self.DIMS
                        for i in range(self.DIMS): # sets desired speed
                            new_speed[i] = (tor_speed[i] + speed[i]) / \
                                  ( (speed[0] ** 2 + speed[1] ** 2) ** (1/2) )

                        self.game.add_asteroid(pos[0], pos[1], \
                                         new_speed[0], new_speed[1], size)
                        self.game.add_asteroid(pos[0], pos[1], \
                                        -new_speed[0], -new_speed[1], size)
                    
                    self.game.add_to_score(score)
                    self.game.remove_asteroid(asteroid)
                    is_hit = True
                    break
        return is_hit


    def check_endgame(self, asteroids):
        """
        Checks if there is a reason to stop the game and does it if so.
        Message changing will be done from HERE (for winning, losing, quit).
        
        :param asteroids: list of asteroids on screen
        :type asteroids: list ( of Asteroid objects )
        """

        msg = ""
        title = ""
        game_end = True
        lives = self.game.get_num_lives()
        
        if lives <= 0: # Checks if the player has lost
            title, msg = self.LOSE_MSG
        elif self.game.should_end(): # Checks if the user hit a quit button
            title, msg = self.QUIT_MSG
        elif len(asteroids) < 1: # Checks if the player has won
            title, msg = self.WIN_MSG
        else:
            game_end = False

        if game_end:
            self.game.show_message(title, msg)
            self.game.end_game()


    def ship_reset(self):
        """
        Moves the ship to the middle of the screen and zeros it's speed
        """

        start_x = (self.screenMaxX-self.screenMinX) / 2 + self.screenMinX
        start_y = (self.screenMaxY-self.screenMinY) / 2 + self.screenMinY
        ship = self.game.get_ship()
        ship.move(start_x, start_y)
        ship.set_speed_x(0)
        ship.set_speed_y(0)

        
    def game_loop(self):
        """
        A loop that runs and handles all the events in the game.
        """

        ship = self.game.get_ship()
        asteroids = self.game.get_asteroids()
        torpedos = self.game.get_torpedos()
        dead_torpedos = []

        # handles user input
        self._handle_key_press(ship, torpedos, asteroids)

        # moves the ship on the screen
        self._move_object(ship)

        # moves the asteroids on the screen and checks if the ship
        # hit an asteroid
        for asteroid in asteroids:
            if self.game.intersect(ship, asteroid):
                self.game.ship_down()
                title, msg = self.SHIP_LOST_MSG
                self.game.show_message(title, msg)
                self.game.remove_asteroid(asteroid)
                self.ship_reset()
                continue
            self._move_object(asteroid)

        # moves the torpedos on the screen and checks if a torpedo hits an
        # asteroid or if it 'faded' (torpedo life ended)
        for torpedo in torpedos:
            if torpedo.get_life_span() > 0:
                self._move_object(torpedo)
                is_hit = self._handle_intersection(torpedo, asteroids)
                if is_hit:
                    dead_torpedos.append(torpedo)
            else:
                dead_torpedos.append(torpedo)
        self.game.remove_torpedos(dead_torpedos) # removes 'dead' torpedos

        # checks if the game should end, and does so if it should
        self.check_endgame(asteroids)


def main():
    runner = GameRunner()
    runner.run()

if __name__ == "__main__":
    main()
