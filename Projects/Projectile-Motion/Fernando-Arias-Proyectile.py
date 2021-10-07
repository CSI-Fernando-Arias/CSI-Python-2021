import math


gun = "AK-74"
cartridge = "5.45x39mm"
ammunition= "5.45x39mm PPBS gs"
velocity = 905
buildingName = "Minillas North Tower"
buildingHeight = 72.85

#Calculate the time that the bullet will fly for
time= (math.sqrt(2*buildingHeight)/9.8)
#Calculate the distance the bullet will travel using the folloeing equation
distance =  velocity*time

print (f"The weapon i choose was {gun} and the cartridge of the gun is {cartridge}. This cartridge has this type of ammunition {ammunition}, the velocity of this ammunition is {velocity}m/s. The building I choose was {buildingName} and it has a height of {buildingHeight}m. The bullet will travel for this much time {time} and for this distance {distance}.")