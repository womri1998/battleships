class Submarine:
    """
    gets the locations in which the submarine is places, and saves it as a 3-tuple list,
    where each tuple represents a location and its status - hit or not hit

    :param list locations: the locations of the submarine
    """
    def __init__(self, locations: list):
        self.locations = [[*location, False] for location in locations]

    """
    checks if the submarine has been just hit in a not hit location
    
    :param (int, int) target: location to be hit
    :return: True iff target is a not hit location of the submarine
    """
    def is_hit(self, target: [int, int]) -> bool:
        for i in range(len(self.locations)):
            if [*target, False] == self.locations[i]:
                self.locations[i][2] = True
                return True
        return False

    """
    checks if the submarine is alive, meaning it has a not hit location
    
    :return: True iff not all of the locations are hit
    """
    def is_alive(self) -> bool:
        return False in [point[2] for point in self.locations]
