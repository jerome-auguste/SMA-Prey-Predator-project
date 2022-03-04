from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from prey_predator.agents import Wolf, Sheep, GrassPatch
from prey_predator.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Sheep:
        # ... to be completed
        portrayal = {"Shape": "circle",
                    "Color": "grey",
                    "Filled": "true",
                    "Layer": 1,
                    "r": 0.3}
    elif type(agent) is Wolf:
        # ... to be completed
        portrayal = {"Shape": "circle",
                    "Color": "red",
                    "Filled": "true",
                    "Layer": 2,
                    "r": 0.3}

    elif type(agent) is GrassPatch:
        # ... to be completed
        portrayal = {"Shape": "rect",
                    "Color": "green",
                    "Filled": "true",
                    "Layer": 0,
                    "w": 0.7,
                    "h": 0.7}

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
