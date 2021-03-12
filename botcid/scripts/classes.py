class DICT(object):

    def __init__(self,name):
        self.__name = name
        self.__LIST = {}


    def name(self):
        return self.__name

    def getlist(self):
        return self.__LIST

    def getkey(self,clave):
        LISTA = list(self.__LIST.keys())
        flag = False
        for i in range(len(LISTA)):
            if LISTA[i]==clave:
                flag = True
                return LISTA[i]
        if not flag:
            return False

    def keyexist(self,clave):
        LISTA = list(self.__LIST.keys())
        flag = False
        for i in range(len(LISTA)):
            if LISTA[i]==clave:
                flag = True
                return True
        if not flag:
            return False

    def getitem(self,clave):
        return self.__LIST.get(clave)

    def additem(self,clave,valor):
        self.__LIST.setdefault(clave,valor)

    def setitem(self,clave,valor):
        self.__LIST[clave] = valor
    
    def delkey(self,clave):
        self.__LIST.pop(clave)