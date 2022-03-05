import os
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from prey_predator.agents import Wolf, Sheep, GrassPatch
from prey_predator.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if isinstance(agent, Sheep):
        # ... to be completed
        portrayal = {"Shape": f"{os.path.dirname(os.path.realpath(__file__))}/sheep.png",
                     "x": 0,
                     "y": 0,
                     "scale": 0.5,
                     "Layer": 1}
        # portrayal = {"Shape": "circle",
        #             "Color": "white",
        #             "Filled": "true",
        #             "Layer": 1,
        #             "r": 0.5}
    elif isinstance(agent, Wolf):
        # ... to be completed
        portrayal = {"Shape": f"{os.path.dirname(os.path.realpath(__file__))}/wolf.png",
                     "x": 0,
                     "y": 0,
                     "scale": 0.5,
                     "Layer": 1}
        
        # portrayal = {"Shape": "circle",
        #             "Color": "red",
        #             "Filled": "true",
        #             "Layer": 2,
        #             "r": 0.5}

    elif isinstance(agent, GrassPatch):
        if agent.fully_grown:
        # ... to be completed
            portrayal = {"Shape": "rect",
                        "Color": "green",
                        "Filled": "true",
                        "Layer": 0,
                        "w": 1,
                        "h": 1}
        else:
            portrayal = {"Shape": "rect",
                        "Color": "yellow",
                        "Filled": "true",
                        "Layer": 0,
                        "w": 1,
                        "h": 1}

    return portrayal


canvas_element = CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Wolves", "Color": "#AA0000"}, {"Label": "Sheep", "Color": "#666666"}]
)

model_params = {
    # ... to be completed
}

server = ModularServer(
    WolfSheep, [canvas_element, chart_element], "Prey Predator Model", model_params
)
server.port = 8521
