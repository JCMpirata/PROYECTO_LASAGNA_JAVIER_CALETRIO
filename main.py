expectedBakeTime = 40
preparationTimeLayer = 2

 def bakeTimeRemaining (elapsedBakeTime):
  """Calculate the bake time remaining.
    :param elapsedBakeTime: int baking time already elapsed
    :return: int remaining bake time (in minutes) derived from 'expectedBakeTime'
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `expectedBakeTime`.
    """
   return expectedBakeTime - elpasedBakeTime

def preparationTimeInMinutes(numberOfLayers):
  """Calculate the time.
    :param numberOfLayers: int the number of layers of the lasagna
    :return int amount of prep time (in minutes), based on 2 minutes per layer added. This function takes an integer representing the number of layers added to the dish, calculating preparation time using a time of 2 minutes per layer added.
    """
return numberOfLayers * PreparationTimeLayer

def elapsedTimeInMinutes(numberOfLayers, elapsedBakeTime):
  """Calculate the elapsed time.
    :param numberOfLayers: int the number of layers in the lasagna
    :param elapsedBakeTime: int elapsed cooking time
    :return: int  total time elapsed (in minutes) preparing and cooking. This function takes two integers representing the number of lasagna layers and the time already spent bakin and calculates the total elapsed minutes spent cooking the lasagna.
    """
  return preparationTimeInMinutes(numberOfLayers) + elapsedBakeTime





   
   


  