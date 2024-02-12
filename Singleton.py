class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        """Virtually private constructor."""
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

