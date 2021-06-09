class Player:
    def __init__(self, point, name):
        self.point = point
        self.name = name
    
    def __str__(self):
        return f"{self.point} - {self.name}"