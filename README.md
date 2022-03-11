# Prey - Predator Model

## Students

- [Jérôme Auguste](https://github.com/jerome-auguste)
- [Magali Morin](https://github.com/magalimorin18)

## Description of the project

In the class of SMA we had to develop a simple model consisting of three agent types: wolves, sheep, and grass evolving in a space represented as a grid.
Agents actions : 
   Sheep and Wolf : eat, reproduce, move
   GrassPatch : eaten by the sheeps, when eaten take some time to fully grow again.


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

- Icons and current energy : on the grid, sheeps and wolves are both represented with icons and their current energy.![Capture d’écran (199)](https://user-images.githubusercontent.com/51906903/157892026-ebec08d5-3fe3-4cef-adff-2e663a694c16.png)

- Chasing mode : at first the movements of the sheeps and wolves were at random. To obtain better results, we implemented a real Wolf and Sheep movement behaviour (Wolves chasing sheeps, Sheeps running away from wolves).

- Tests : we designed tests to verify our code (à compléter) 

## Parameters

The parameters we could change were : 
 - Number of wolves and sheeps at the begining on the grid
 - Reproduction rate of wolves and sheeps
 - Energy at creation of wolves and sheeps
 - Grass growing time 
 - Chasing mode 

The optimal parameters were : 



## Results

Screen shot du résultat

Observations : 

