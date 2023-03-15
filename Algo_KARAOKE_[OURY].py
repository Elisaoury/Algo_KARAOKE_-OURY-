## A ##
class chanson : 
     def __init__(self,name,score):
          self.__nom = name 
          self.__pointChanson = score
     def getNom(self):
          return self.__nom 
     def getPointChanson(self):
          return self.__pointChanson 
          

chanson1 = chanson("chanson1",60)
chanson2 = chanson("chanson2",70)
chanson3 = chanson("chanson3",80)
chanson4 = chanson("chanson4",90)
chanson5 = chanson("chanson5",100)


class player : 
    def __init__(self, name,score,sing):
        self.__nom = name 
        self.__point = score
        self.__chanson = sing
    def getNom(self):
        return self.__nom
    def getPoint(self):
        return self.__point
    def getChanson(self):
        return self.__chanson
    def Score(self,nombreDeScoreGagne):
        self.__point = 0
        if (self.__point == 0) :
            print ( self.__nom+" n'as pas encore essayer la chanson ")
        if (self.__point >= 50):
            print ( self.__nom+self.__point +" de point sur cette chanson")

    


joueur1  = player("joueur1",0)
joueur2  = player("joueur2",0)
joueur3  = player("joueur3",0)
joueur4  = player("joueur4",0)


## B ##

class karaoke:
    def __init__(self,name):
        self.__nom = name
    def getNom(self):
        return self.__nom
    
class chanson(karaoke):
    def __init__(self,name):
        self.nom = name
    def getNom(self):
        return self.__nom
chanson0 = chanson("0")
chanson1 = chanson("1")
chanson2 = chanson("2")
chanson3 = chanson("3")
chanson4 = chanson("4")
chanson5 = chanson("5")

class player(karaoke):
     def __init__(self, name,score,sing):
        self.__nom = name 
        self.__point = score
        self.__chanson = sing
     def getNom(self):
        return self.__nom
     def getPoint(self):
        return self.__point
     def getChanson(self):
        return self.__chanson