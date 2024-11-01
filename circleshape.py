import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, other):
        # if only I had finished reading the assignment way
        return self.position.distance_to(other.position) <= self.radius + other.radius

        # my brute force way
        '''s_x,s_y = self.position.xy
        o_x, o_y = other.position.xy
        return ((o_x - s_x)**2 + (o_y - s_y)**2)**.5 <= (self.radius + other.radius)'''

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
