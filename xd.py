class libro:
    def __init__(self,codigo,titulo):
        self.__codigo=codigo
        self.__titulo=titulo
        self.lector=None

    def prestar(self, lector):
        if self.lector == None:
            self.lector=lector
            return True
        return False
