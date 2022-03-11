# Prey - Predator Model

## Students

- [Jérôme Auguste](https://github.com/jerome-auguste)
- [Magali Morin](https://github.com/magalimorin18)

## Description of the project

In the class of SMA we had to develop a simple model consisting of three agent types: Wolf, Wheep and GrassPatch. 
All agents evolve in a space represented by a grid.

Agents' possible actions : 
   - Sheep and Wolf : eat, reproduce, move
   - GrassPatch : when eaten by a Sheep, take some time to fully grow again, is eaten by the Sheeps


## Run the code

Install requirements  
```bash
    pip install -r requirements.txt
```
Run the server
```bash
    mesa runserver
```

## Organisation of the project

- ``prey_predator/random_walker.py``: This defines the ``RandomWalker`` agent, which implements the behavior of moving randomly across a grid, one cell at a time. Both the Wolf and Sheep agents will inherit from it.
- ``prey_predator/agents.py``: Defines the Wolf, Sheep, and GrassPatch agent classes.
- ``prey_predator/schedule.py``: Defines a custom variant on the RandomActivation scheduler, where all agents of one class are activated (in random order) before the next class goes -- e.g. all the wolves go, then all the sheep, then all the grass.
- ``prey_predator/model.py``: Defines the Prey-Predator model itself
- ``prey_predator/server.py``: Sets up the interactive visualization server
- ``run.py``: Launches a model visualization server.

## Implementation

- Display icons and current energy : on the grid Sheeps and Wolves are both represented by icons with their current energy.

![Capture d’écran (199)](https://user-images.githubusercontent.com/51906903/157892026-ebec08d5-3fe3-4cef-adff-2e663a694c16.png)

- Chasing mode : at first the movements of the Sheeps and Wolves were at random. To obtain better results, we implemented a real Wolf and Sheep movement behaviour (Wolves chasing sheeps, Sheeps running away from wolves).

- Energy gained : we decided to quantify the energy gained by a Wolf to the energy of the Sheep he eats.

- Tests (à compléter) 

## Parameters

The parameters that can be modified are:

 - Number of Wolves and Sheeps on the grid before start (10-200)
 - Reproduction rate of Wolves and Sheeps (0-1)
 - Energy gained from eating Sheep (1-50)
 - Energy gained from eating Grass (1-20)
 - Energy at creation for Wolves and Sheeps (1-100)
 - Grass growing time (1-100)
 - Chasing mode (True/False)

The optimal parameters were : 

| Parameters                      | Value  |
| --------------------------------|--------|
| Number of Wolves at start       | 10     |
| Number of Sheeps at start       | 40     |
| Reproduction rate of Wolves     | 0.09   |
| Reproduction rate of Sheeps     | 0.09   |
| Energy gained from eating Sheep | 10     |
| Energy gained from eating Grass | 10     |
| Energy at creation for Wolves   | 4      |
| Energy at creation for Sheeps   | 10     |
| Grass growing time              | 10     |
| Chasing mode                    | False  |



## Results

Screen shot du résultat

![Capture d’écran (200)](https://user-images.githubusercontent.com/51906903/157895818-c2af1910-acf4-4bca-8fe9-0824dadea255.png)

Observations : 

