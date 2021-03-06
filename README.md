# Prey - Predator Model

## Students

- [Jérôme Auguste](https://github.com/jerome-auguste)
- [Magali Morin](https://github.com/magalimorin18)

## Description of the project

In the class of SMA we had to develop a simple model consisting of three agent types: Wolf, Wheep and GrassPatch.
All agents evolve in a space represented by a grid.

Agents' possible actions:

   - Sheep and Wolf: eat, reproduce, move
   - GrassPatch: when eaten by a Sheep, take some time to fully grow again, is eaten by the Sheeps


## Run the code

Install requirements 

```bash
    pip install -r requirements.txt
```

Run the server

```bash
    mesa runserver
```

or, at the root of the project

```bash
    python ./run.py
```

## Organisation of the project

- ``prey_predator/random_walker.py``: This defines the ``RandomWalker`` agent, which implements the behavior of moving randomly across a grid, one cell at a time. Both the Wolf and Sheep agents will inherit from it.
- ``prey_predator/agents.py``: Defines the Wolf, Sheep, and GrassPatch agent classes.
- ``prey_predator/schedule.py``: Defines a custom variant on the RandomActivation scheduler, where all agents of one class are activated (in random order) before the next class goes -- e.g. all the wolves go, then all the sheep, then all the grass.
- ``prey_predator/model.py``: Defines the Prey-Predator model itself
- ``prey_predator/server.py``: Sets up the interactive visualization server
- ``run.py``: Launches a model visualization server.

## Implementation

- Display icons and current energy: on the grid Sheeps and Wolves are both represented by icons with their current energy.

![Capture d’écran (199)](https://user-images.githubusercontent.com/51906903/157892026-ebec08d5-3fe3-4cef-adff-2e663a694c16.png)

- Chasing mode: at first the movements of the Sheeps and Wolves were at random. To obtain better results, we implemented a real Wolf and Sheep movement behaviour (Wolves chasing sheeps, Sheeps running away from wolves).

- Energy gained: we decided to quantify the energy gained by a Wolf to the energy of the Sheep he eats.

- Tests: some unit tests can be run on the agents using pytest

## Parameters

The parameters that can be modified are:

- Number of Wolves and Sheeps on the grid before start (10-200)
- Reproduction rate of Wolves and Sheeps (0-1)
- Energy gained from eating Sheep (1-50)
- Energy gained from eating Grass (1-20)
- Energy at creation for Wolves and Sheeps (1-100)
- Grass growing time (1-100)
- Chasing mode (True/False)

These values were the equilibrium we found for this model. Changing one value makes it unstable unless we find the right equilibrium for all the other parameters: 

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
| Grass growing time              | 16     |
| Chasing mode                    | False  |



## Results

![Capture d’écran (204)](https://user-images.githubusercontent.com/51906903/157899361-148b092e-0149-4fdd-a9ef-dbc0149fde32.png)

### Analysis

At the initialization of the environment, grass patches are all fully grown so that sheeps can eat them and live longer (increasing reproduction chance). However, as soon as the sheep population increases, it gives more oportunities for wolves to eat and live longer (and so to reproduce). Therefore, wolves population grows and sheeps die faster (being eaten). Then at a certain point, wolves are not able to eat anymore and die from fatigue whereas free sheeps start to reproduce again while eating more fully grown grass.
Then the model oscillates again and again.
