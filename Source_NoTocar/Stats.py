##ESTADISTICAS / DATOS POKEMON


class StatsCharizard:
    def __init__(self):
        self.PS = 78
        self.TotalPS = 78
        self.Ataque = 84
        self.Defensa = 78
        self.AtaqueSp = 109
        self.DefSp = 85
        self.Vel = 100
        self.EO = "user"
        self.tipo = "fuego"
        self.name = "Charizard"
        self.dSlots = {"mSlot1":{},"mSlot2":{},"mSlot3":{},"mSlot4":{}}

    def setMoveSlots(self, move, slot):
        if slot == 1:
            self.dSlots["mSlot1"] = move
        elif slot == 2:
            self.dSlots["mSlot2"] = move
        elif slot == 3:
            self.dSlots["mSlot3"] = move
        elif slot == 4:
            self.dSlots["mSlot4"] = move

    def getMoveSlots(self, slot):
        if slot == 1:
            iRet = self.dSlots["mSlot1"]
        elif slot == 2:
            iRet = self.dSlots["mSlot2"]
        elif slot == 3:
            iRet = self.dSlots["mSlot3"]
        elif slot == 4:
            iRet = self.dSlots["mSlot4"]
        return iRet


class StatsGengar:
    def __init__(self):
        self.PS = 60
        self.TotalPS = 60
        self.Ataque = 65
        self.Defensa = 60
        self.AtaqueSp = 130
        self.DefSp = 75
        self.Vel = 110
        self.EO = "enemy"
        self.tipo = "fantasma"
        self.name = "Gengar"
        self.dSlots = {"mSlot1":"","mSlot2":"","mSlot3":"","mSlot4":""}

    def setMoveSlots(self, move, slot):
        if slot == 1:
            self.dSlots["mSlot1"] = move
        elif slot == 2:
            self.dSlots["mSlot2"] = move
        elif slot == 3:
            self.dSlots["mSlot3"] = move
        elif slot == 4:
            self.dSlots["mSlot4"] = move

    def getMoveSlots(self, slot):
        if slot == 1:
            iRet = self.dSlots["mSlot1"]
        elif slot == 2:
            iRet = self.dSlots["mSlot2"]
        elif slot == 3:
            iRet = self.dSlots["mSlot3"]
        elif slot == 4:
            iRet = self.dSlots["mSlot4"]
        return iRet
