from game.casting.actor import Actor

class Artifact(Actor):
    """
    An object representing either a gem or a stone. 
    The responsibility of an Artifact is to say its score.
    
    Attributes:
        _points (int): A score of an artifact.
    """
    def __init__(self):
        super().__init__()
        
        
    def count_points(self):
        points = 0

        if(self.get_text()== "*"):
            points = 1
        else:
            points = -1
        return points