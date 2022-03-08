"""Agents definition classes (Sheep, Wolf or GrassPatch)"""
from mesa import Agent
from prey_predator.random_walk import RandomWalker


class Sheep(RandomWalker):
    """
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        
    def try_reproduce(self): # TODO : introduce energy consumption
        if self.random.random() <= self.model.sheep_reproduce:
            a = Sheep(self.model.next_id(), self.pos, self.model, self.moore, energy=20)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)
            
    def try_eat(self):
        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cell_agents:
            if isinstance(agent, GrassPatch) and agent.fully_grown:
                self.energy += self.model.sheep_gain_from_food
                agent.fully_grown = False
                break
    
    def try_die_from_energy(self):
        if self.energy == 0:
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
            

    def step(self):
        """
        A model step. Move, then eat grass and reproduce.
        """
        # ... to be completed
        self.random_move()
        self.energy -= 1
        self.try_reproduce()
        self.try_eat()
        self.try_die_from_energy()
        


class Wolf(RandomWalker):
    """
    A wolf that walks around, reproduces (asexually) and eats sheep.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
    
    def try_reproduce(self): # TODO : introduce energy consumption
        if self.random.random() <= self.model.wolf_reproduce:
            a = Wolf(self.model.next_id(), self.pos, self.model, self.moore, energy=20)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)
    
    def try_eat(self):
        cell_agents = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cell_agents:
            if isinstance(agent, Sheep):
                self.energy += self.model.wolf_gain_from_food
                self.model.schedule.remove(agent)
                self.model.grid.remove_agent(agent)
                break
    
    def try_die_from_energy(self):
        if self.energy == 0:
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
        

    def step(self):
        # ... to be completed
        self.random_move()
        self.energy -= 1
        self.try_reproduce()
        self.try_eat()
        self.try_die_from_energy()
        


class GrassPatch(Agent):
    """
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    """

    def __init__(self, unique_id, pos, model, fully_grown, countdown):
        """
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        """
        super().__init__(unique_id, model)
        # ... to be completed
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.current_countdown = self.countdown
    
    def grow(self):
        if not self.fully_grown and self.current_countdown > 0:
            self.current_countdown -= 1
        else:
            self.current_countdown = self.countdown
            self.fully_grown = True

    def step(self):
        # ... to be completed
        self.grow()
