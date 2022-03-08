"""Unit tests on agents"""
from prey_predator.agents import Wolf, Sheep
from prey_predator.model import WolfSheep

def test_reproduce_Wolf():
    
    # Set up the model with reproduction rate of 1 (always reproduce)
    model = WolfSheep(wolf_reproduce=1)
    initial_wolf_num = model.initial_wolves

    # One wolf step (including reproduce)
    first_wolf = next(iter(model.schedule.agents_by_breed[Wolf].values()))
    first_wolf.step()
    
    # Assert if the number of current Wolves is greater than the number of initial Wolves
    assert initial_wolf_num < model.schedule.get_breed_count(Wolf)
    

def test_reproduce_Sheep():
    
    # Set up the model with reproduction rate of 1 (always reproduce)
    model = WolfSheep(sheep_reproduce=1)
    initial_sheep_num = model.initial_sheep

    # One Sheep step (including reproduce)
    first_sheep = next(iter(model.schedule.agents_by_breed[Sheep].values()))
    first_sheep.step()
    
    # Assert if the number of current Sheeps is greater than the number of initial Sheeps 
    assert initial_sheep_num < model.schedule.get_breed_count(Sheep)