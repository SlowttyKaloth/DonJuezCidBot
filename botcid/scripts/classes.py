class DICT(object):

    def __init__(self,name):
        self.__name = name
        self.__LIST = {}
    
    def __repr__(self):
        return 'test'

    def name(self):
        return self.__name

    def getlist(self):
        return self.__LIST

    def getkeybypos(self,pos):
        LISTA = list(self.__LIST.keys())
        if pos > len(LISTA):
                return False
        else:
            return LISTA[pos]

    def getkeybyitem(self,item):
        LISTAK = list(self.__LIST.keys())
        LISTAI = list(self.__LIST.values())
        for i in range(len(LISTAI)):
            if LISTAI[i]==item:
                j = i
            else:
                return None
        i = 0
        if j > len(LISTAK):
            return None
        else:
            return LISTAK[j]


    def getkeypos(self,key):
        LISTA = list(self.__LIST.keys())
        flag = False
        for i in range(len(LISTA)):
            if LISTA[i]==key:
                flag = True
                return i
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

    def itemexist(self,item):
        LISTA = list(self.__LIST.values())
        flag = False
        for i in range(len(LISTA)):
            if LISTA[i]==item:
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
        return clave
    
    def delkey(self,clave):
        self.__LIST.pop(clave)

class var(object):
    def __init__(self):
        self.__var = 0

    def setvar(self,value):
        self.__var = value
        return value

    def getvar(self):
        return self.__var 