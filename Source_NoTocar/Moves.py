##Movimientos


class ListMoves:
    def __init__(self):
        pass
    def MT35(): #LANZALLAMAS
        DictDataMove35 = {"Potencia":95,"sType":"fuego","Catego":"Especial","name":"Lanzallamas"}
        return DictDataMove35
    def MT30(): #BOLA SOMBRA
        DictDataMove30 = {"Potencia":80,"sType":"fantasma","Catego":"Especial","name":"Bola Sombra"}
        return DictDataMove30
    def MT221(): #RELAJO (custom)
        DictDataMove221 = {"Potencia":None,"sType":"normal","Catego":"Estado",
        "name":"Siesta",
        "efect":"cura",
        "quantity":75}
        return DictDataMove221
    def MT04(): #AGILIDAD
        DictDataMove04 = {"Potencia":None,"sType":"Psiquico","Catego":"Estado",
        "name":"Agilidad",
        "efect":"boost",
        "stat":"Vel",
        "quantity":2}
        return DictDataMove04
    def MT322(): #ARAÑAZO (custom)
        DictDataMove322 = {"Potencia":40,"sType":"normal","Catego":"Fisico","name":"Arañazo"}
        return DictDataMove322
    def MT60(): #ATAQUE ALA
        DictDataMove322 = {"Potencia":60,"sType":"volador","Catego":"Fisico","name":"Ataque Ala"}
        return DictDataMove322


