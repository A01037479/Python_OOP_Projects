import random


class Asteroid:
    """
    A class represents asteroid
    """
    asteroid_id = 0

    def __init__(self, radius, position, velocity, timestamp):
        """
        Initialize a Asteroid object
        :param radius: an int
        :param position: an list
        :param velocity: an list
        :param timestamp: an date object
        """
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.timestamp = timestamp
        self.asteroid_id = Asteroid.increment_id()

    @classmethod
    def increment_id(cls):
        """
        Class method that increments unique id for asteroids
        :return: incremented asteroid id
        """
        cls.asteroid_id = cls.asteroid_id + 1
        return cls.asteroid_id

    def get_radius(self):
        """
        Accessor for radius
        :return: radius of an asteroid object
        """
        return self.radius

    def get_position(self):
        """
        Accessor for position
        :return: position of an asteroid object
        """
        return self.position

    def get_velocity(self):
        """
        Accessor for velocity
        :return: velocity of an asteroid object
        """
        return self.velocity

    def get_timestamp(self):
        """
        Accessor for timestamp
        :return: timestamp of an asteroid object
        """
        return self.timestamp

    def set_radius(self, radius):
        """
        Mutator for radius
        :param radius: radius for an asteroid object
        """
        self.radius = radius

    def set_position(self, position):
        """
        Mutator for position
        :param position: position for an asteroid object
        """
        self.position = position

    def set_velocity(self, velocity):
        """
        Mutator for velocity
        :param velocity: velocity for an asteroid object
        """
        self.velocity = velocity

    def set_timestamp(self, timestamp):
        """
        Mutator for timestamp
        :param timestamp: timestamp for an asteroid object
        :return:
        """
        self.timestamp = timestamp

    def move(self):
        """
        Moves an asteroid object
        """
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def __str__(self):
        """
        :return: String representation of Asteroid class
        """
        return f"Asteroid {self.asteroid_id} with radius{self.radius} created at{self.timestamp}. " \
               f"Position({self.position[0]},{self.position[1]},{self.position[2]}), " \
               f"Velocity({self.velocity[0]},{self.velocity[1]},{self.velocity[2]})."
