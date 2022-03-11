"""Unit tests on agents"""
from prey_predator.agents import Wolf, Sheep, GrassPatch
from prey_predator.model import WolfSheep

def test_reproduce_Wolf():
    
    # Set up the model with reproduction rate of 1 (always reproduce)
    model = WolfSheep(initial_wolves=1, initial_sheep=0, wolf_reproduce=1)
    initial_wolf_num = model.initial_wolves

    # One wolf reproduce
    first_wolf = next(iter(model.schedule.agents_by_breed[Wolf].values()))
    first_wolf.try_reproduce()
    
    # Assert if the number of current Wolves is one more than the initial number
    assert model.schedule.get_breed_count(Wolf) == initial_wolf_num + 1
    

def test_reproduce_Sheep():
    
    # Set up the model with reproduction rate of 1 (always reproduce)
    model = WolfSheep(initial_wolves=0, initial_sheep=1, sheep_reproduce=1)
    initial_sheep_num = model.initial_sheep

    # One sheep reproduce
    first_sheep = next(iter(model.schedule.agents_by_breed[Sheep].values()))
    first_sheep.try_reproduce()
    
    # Assert if the number of current Sheeps is one more than the initial number
    assert model.schedule.get_breed_count(Sheep) ==  initial_sheep_num + 1



def test_try_eat_Wolf():
    
    # Set up the model with 1 cell (all agents will be set on the same cell)
    model = WolfSheep(width=1, height=1, initial_wolves=1, initial_sheep=1)
    initial_sheep_num = model.initial_sheep
    initial_wolf_energy = model.initial_wolf_energy
    
    # One wolf eat Sheep
    first_wolf = next(iter(model.schedule.agents_by_breed[Wolf].values()))
    first_wolf.try_eat()
    
    assert model.schedule.get_breed_count(Sheep) == initial_sheep_num - 1
    assert first_wolf.energy == initial_wolf_energy + model.wolf_gain_from_food
    

def test_try_eat_Sheep():

    # Set up the model with 1 cell (all agents will be set on the same cell)
    model = WolfSheep(width=1, height=1, initial_wolves=0, initial_sheep=1)
    initial_sheep_energy = model.initial_sheep_energy

    # One sheep eat grass patch
    first_sheep = next(iter(model.schedule.agents_by_breed[Sheep].values()))
    first_sheep.try_eat()

    # The only grass patch the sheep has eaten
    grass_patch = next(iter(model.schedule.agents_by_breed[GrassPatch].values()))

    assert first_sheep.energy == initial_sheep_energy + model.sheep_gain_from_food
    assert grass_patch.fully_grown == False

    # When grass is not fully grown
    first_sheep.try_eat()

    assert first_sheep.energy == initial_sheep_energy + model.sheep_gain_from_food
    assert grass_patch.fully_grown == False


def test_try_die_from_energy():
    
    # Set up the model with 1 cell (all agents will be set on the same cell)
    model = WolfSheep(width=1, height=1, initial_wolves=1, initial_sheep=1, initial_sheep_energy=1, initial_wolf_energy=1)
    initial_wolves = model.initial_wolves
    initial_sheeps = model.initial_sheep
    
    # One wolf looses energy
    first_wolf = next(iter(model.schedule.agents_by_breed[Wolf].values()))
    first_wolf.energy -= 1
    assert first_wolf.energy == 0
    
    first_wolf.try_die_from_energy()
    assert model.schedule.get_breed_count(Wolf) == initial_wolves - 1
    
    # One sheep looses energy
    first_sheep = next(iter(model.schedule.agents_by_breed[Sheep].values()))
    first_sheep.energy -= 1
    assert first_sheep.energy == 0
    
    first_sheep.try_die_from_energy()
    assert model.schedule.get_breed_count(Sheep) == initial_sheeps - 1


def test_grow():
    # Set up the model with 1 cell (all agents will be set on the same cell)
    model = WolfSheep(width=1, height=1, initial_wolves=0, initial_sheep=1, initial_sheep_energy=1)
    
    # One sheep looses energy
    first_sheep = next(iter(model.schedule.agents_by_breed[Sheep].values()))
    first_sheep.try_eat()
    
    # The only grass patch the sheep has eaten
    grass_patch = next(iter(model.schedule.agents_by_breed[GrassPatch].values()))
    assert grass_patch.fully_grown == False
    
    for _ in range(grass_patch.countdown):
        grass_patch.grow()
    
    assert grass_patch.fully_grown == True
    
# TODO : Test chasing mode