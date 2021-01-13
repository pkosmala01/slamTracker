class NoPlayerError(Exception):
    def __init__(self):
        super().__init__('Could not find a player with that name')
