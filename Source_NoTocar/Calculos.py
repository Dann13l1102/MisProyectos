##Calculos turnos ataques


def TurnCalc(tipoMove, PotMov, CategoriaMove, VidaTarget, DefTarg, DefSpTarg, AtakUser, SpecialAtkUser, TipoPokUser):

    #STAB
    if tipoMove == TipoPokUser:
        Bonus = 1.5
    else:
        Bonus = 1
    
    if CategoriaMove == "Especial":
        StatAtk = SpecialAtkUser
        TargetStatDef = DefSpTarg
    elif CategoriaMove == "Fisico":
        StatAtk = AtakUser
        TargetStatDef = DefTarg
    
    Operacion = ((PotMov * StatAtk * Bonus) / TargetStatDef) / 6
    VidaResTarget = VidaTarget - round(Operacion)
    
    if VidaResTarget < 0:
        VidaResTarget = 0
    
    return VidaResTarget

#Movimientos de estado
def TurnCalcEstado(MoveData, UserData):
    
    if MoveData["efect"] == "cura":
        StatResult = {"stat":None,"result":None}
        PorcentajeCura = MoveData["quantity"]
        PScurados = round(UserData.TotalPS * (PorcentajeCura / 100))
        PSresultUser = UserData.PS + PScurados
        if PSresultUser > UserData.TotalPS:
            PSresultUser = UserData.TotalPS
        StatResult["stat"], StatResult["result"] = "PS", PSresultUser
        iRet = StatResult

    elif MoveData["efect"] == "boost":
        StatResult = {"stat":None,"result":None}
        PlusBoost = MoveData["quantity"]
        if MoveData["stat"] == "Vel": #Boosteamos la velocidad
            iStat = MoveData["stat"]
            VelRes = UserData.Vel * PlusBoost
            StatResult["stat"], StatResult["result"] = iStat, VelRes
            iRet = StatResult
    
    return iRet
                
