import math
from ExperimentData import ExperimentData

def experiment(experimentData:ExperimentData):

    #Calculate the time that the bullet will fly for
    time = (math.sqrt(2 * experimentData.buildingHeight)/9.8)
    #Calculate the distance the bullet will travel using the folloeing equation
    distance =  experimentData.velocity*time
    print(f"The weapon i choose was {experimentData.gun} and the cartridge of the gun is {experimentData.cartridge}. This cartridge has this type of ammunition {experimentData.ammunition}, the velocity of this ammunition is {experimentData.velocity}m/s. The building I choose was {experimentData.buildingName} and it has a height of {experimentData.buildingHeight}m. The bullet will travel for this much time {time} and for this distance {distance}. There is no air resistance therefore it wont affect the time and distance it will travel.")


# experimentData = {
#  "gun" : "AK-74",
#  "cartridge" : "5.45x39mm",
#  "ammunition": "5.45x39mm PPBS gs",
#  "velocity" : 905,
#  "buildingName" : "Minillas North Tower",
#  "buildingHeight" : 72.85
#  }

myData = ExperimentData("AK-74", "5.45x39mm", "5.45x39mm PPBS gs", 905, "Minillas North Tower", 72.85)


experiment(myData)
