import random


class Objects:

    def __init__(self, rep,env,x=None,y=None):
        self.coordinates = []
        self.rep = rep
        self.env = env
        if x is None:
            self.x = random.randrange(env.x)
        else:
            self.x = x
        if y is None:
            self.y = random.randrange(env.y)
        self.coordinates.append(self.x,self.y)

    def __repr__(self):
        return self.rep

class Environment:
    def __init__(self,x_dim,y_dim):
        self.x = x_dim
        self.y = y_dim
