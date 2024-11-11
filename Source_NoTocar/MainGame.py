from pygame import mixer
import pygame
import sys
#import os
from Config import *
from InterfazGame import *
import time
from Stats import *
from Moves import *
from Calculos import *

## MAIN PROGRAM ##
#Iniciar Juego
pygame.init()

#Inicializar stats pokemon
Chariz = StatsCharizard()
Gengar = StatsGengar()

#Movimientos init
LanzLlama = ListMoves.MT35()
BSombra = ListMoves.MT30()
Relaj = ListMoves.MT221()
Agil = ListMoves.MT04()
Scratch = ListMoves.MT322()
AtakAla = ListMoves.MT60()

#Init slots
Chariz.setMoveSlots(LanzLlama,1)
Chariz.setMoveSlots(Relaj,2)
Chariz.setMoveSlots(Agil,3)
Chariz.setMoveSlots(AtakAla,4)
uSlot1 = Chariz.getMoveSlots(1)
uSlot2 = Chariz.getMoveSlots(2)
uSlot3 = Chariz.getMoveSlots(3)
uSlot4 = Chariz.getMoveSlots(4)

#Configurar ventana
icono = pygame.image.load(Icon)
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Pokemon Game")
pygame.display.set_icon(icono)

#Rutas sprites
rutaImagen = ImgCuadro
ImgFondo = BgImg


# Inicializar posicion flecha selector menu
posicion_x = dPos1["x"]
posicion_y = dPos1["y"]

##lista sprite flecha seleccion menu
f_index = 0
frames = SpriteGenerate(SprArrPath, 35, 48)


# Reloj para controlar la velocidad de la animación
reloj = pygame.time.Clock()
fps = FPSs



###lista sprite Pokemon
f_indexC = 0
framesC = SpriteGenerate(SprCharPath, 412, 338)

f_indexG = 0
framesG = SpriteGenerate(SprGengPath, 199.8, 170.1)



#Menu actual
#nota: 0 es el menu principal
MoveSet = 0

#Ini combate
DelayIniCombat = 0

#Fin de turno
EndAttack = 0

#huir:
Cagao = 0
cUntilRun = 0

#Atacar/Combate:
AtaqueTurn = 0
DelayAttack = 0
DelayEnemyAttack = 0
DelayBetweenAtt = 0
DelayEfectEstado = 0
lDelayEffEstado = 0
fAfterEstado = 0
flagMyTurnEnd = 0
flagTurnEnd = 0
CompareVel = 0
PSzeroUser = 0
PSzeroEnemy = 0
EndBattle = 0
SoundEstado = 0
lSoundEstado = 0

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ChannelOst.stop()
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                if posicion_x == dPos1["x"] and posicion_y == dPos1["y"]:
                    SFXplay(ABfile)
                    posicion_x += 200
                if posicion_x == dPos3["x"] and posicion_y == dPos3["y"]:
                    SFXplay(ABfile)
                    posicion_x += 200
            if evento.key == pygame.K_DOWN:
                if posicion_x == dPos1["x"] and posicion_y == dPos1["y"]:
                    if MoveSet != 101:
                        SFXplay(ABfile)
                        posicion_y += 50
                if posicion_x == dPos2["x"] and posicion_y == dPos2["y"]:
                    if MoveSet != 101:
                        SFXplay(ABfile)
                        posicion_y += 50
            if evento.key == pygame.K_LEFT:
                if posicion_x == dPos2["x"] and posicion_y == dPos2["y"]:
                    SFXplay(ABfile)
                    posicion_x -= 200
                if posicion_x == dPos4["x"] and posicion_y == dPos4["y"]:
                    SFXplay(ABfile)
                    posicion_x -= 200
            if evento.key == pygame.K_UP:
                if posicion_x == dPos3["x"] and posicion_y == dPos3["y"]:
                    SFXplay(ABfile)
                    posicion_y -= 50
                if posicion_x == dPos4["x"] and posicion_y == dPos4["y"]:
                    SFXplay(ABfile)
                    posicion_y -= 50

            if evento.key == pygame.K_z:
                if MoveSet == 0:
                    if posicion_x == dPos1["x"] and posicion_y == dPos1["y"]:
                        SFXplay(ABfile)
                        MoveSet = 1
                    if posicion_x == dPos4["x"] and posicion_y == dPos4["y"]:
                        SFXplay(ABfile)
                        Cagao = 1
                        ChannelOst.pause()
                        SFXplay(FartFile,0.9)
                elif MoveSet == 1:
                    if posicion_x == dPos1["x"] and posicion_y == dPos1["y"]:
                        SFXplay(ABfile)
                        MoveSet = 99
                        lFlagAtaq["fSlot1"] = 1
                    elif posicion_x == dPos2["x"] and posicion_y == dPos2["y"]:
                        SFXplay(ABfile)
                        MoveSet = 99
                        lFlagAtaq["fSlot2"] = 1
                    elif posicion_x == dPos3["x"] and posicion_y == dPos3["y"]:
                        SFXplay(ABfile)
                        MoveSet = 99
                        lFlagAtaq["fSlot3"] = 1
                    elif posicion_x == dPos4["x"] and posicion_y == dPos4["y"]:
                        SFXplay(ABfile)
                        MoveSet = 99
                        lFlagAtaq["fSlot4"] = 1
                    
                elif MoveSet == 101:
                    if posicion_x == dPos1["x"] and posicion_y == dPos1["y"]:
                        MoveSet = 0
                        PSzeroUser = 0
                        PSzeroEnemy = 0
                        Chariz.PS = Chariz.TotalPS
                        Gengar.PS = Gengar.TotalPS
                        ChannelOst.stop()
                        #ChannelOst = OstBattle(mFile)
                        DelayIniCombat = 0
                    if posicion_x == dPos2["x"] and posicion_y == dPos2["y"]:
                        ChannelOst.stop()
                        pygame.quit()
                        sys.exit()
                
            if evento.key == pygame.K_x:
                if MoveSet == 1:
                    SFXplay(ABfile)
                    MoveSet = 0

    #Delay tras huir --> cerrar juego
    if cUntilRun == 50:
        ChannelOst.stop()
        pygame.quit()
        sys.exit()
    
    #Delay inicio combate
    #Musica combate
    DelayIniCombat += 1
    if DelayIniCombat == 3:
        ChannelOst = OstBattle(mFile)
    
    #Fin del combate
    #Resetear todo
    if EndBattle == 55:
        EndBattle = 0
        MoveSet = 101
        #lFlagAtaq = {keys: 0 for keys in lFlagAtaq.values()}
        lFlagAtaq["fSlot1"], lFlagAtaq["fSlot2"], lFlagAtaq["fSlot3"], lFlagAtaq["fSlot4"] = 0, 0, 0, 0
        posicion_x = dPos1["x"]
        posicion_y = dPos1["y"]
        EndAttack = 0
        flagMyTurnEnd = 0
        flagTurnEnd = 0
        DelayAttack = 0
        DelayBetweenAtt = 0
        DelayEnemyAttack = 0
        DelayEfectEstado = 0
        lDelayEffEstado = 0
        fAfterEstado = 0
        CompareVel = 0
        SoundEstado = 0
        lSoundEstado = 0
        AtaqueTurn = 0
        
    
    #Delay tras fin del turno
    #Resetear el turno
    if EndAttack == 20:
        MoveSet = 0
        #lFlagAtaq = {keys: 0 for keys in lFlagAtaq.values()}
        lFlagAtaq["fSlot1"], lFlagAtaq["fSlot2"], lFlagAtaq["fSlot3"], lFlagAtaq["fSlot4"] = 0, 0, 0, 0
        posicion_x = dPos1["x"]
        posicion_y = dPos1["y"]
        EndAttack = 0
        flagMyTurnEnd = 0
        flagTurnEnd = 0
        DelayAttack = 0
        DelayBetweenAtt = 0
        DelayEnemyAttack = 0
        DelayEfectEstado = 0
        lDelayEffEstado = 0
        fAfterEstado = 0
        CompareVel = 0
        SoundEstado = 0
        lSoundEstado = 0
        AtaqueTurn = 0


    # Color pantalla base
    ventana.fill((200, 255, 255))

    ### INICIALIZAR INTERFAZ ##
    # Background
    CrearImagen(ventana, ImgFondo, 850, ventana_alto, -340, 0)

    # Sprite de mi pokemon
    ventana.blit(framesC[f_indexC],(-58,270)) #charizard
    ventana.blit(framesG[f_indexG],(258,50)) #gengar
    
    #Barra vida usuario
    CrearImagen(ventana, rutaImagen, 350, 66, 326, 400)
    CrearTexto(ventana, f"PS  {Chariz.PS}/{Chariz.TotalPS}",20,350,426)
    
    #Barra vida enemigo
    CrearImagen(ventana, rutaImagen, 350, 66, -120, 100)
    CrearTexto(ventana, f"PS  {Gengar.PS}/{Gengar.TotalPS}",20,10,124)

    # Cuadro menu combate
    CrearImagen(ventana, rutaImagen, 450, 60, 15, 500) #cuadro preguntas guia
    CrearImagen(ventana, rutaImagen, 450, 150, 15, 555) #menu selector

    if Cagao == 0 and all(flag == 0 for flag in lFlagAtaq.values()):
        # Flechita seleccionar MENU animada
        ventana.blit(frames[f_index],(posicion_x,posicion_y))
        
    if MoveSet == 0:
        if Cagao == 0:
            # Menu principal
            CrearTexto(ventana, "¿Que deberia hacer Charizard?",20,48,522)
            CrearTexto(ventana, "Luchar",25,76,595)
            CrearTexto(ventana, "Mochila",25,276,595)
            CrearTexto(ventana, "Pokemon",25,76,645)
            CrearTexto(ventana, "Huir",25,276,645)
        elif Cagao == 1:
            CrearTexto(ventana, "¡Vaya! Parece que eres un cagao",20,60,595)
    elif MoveSet == 1:
        # Menu combate ataques
        CrearTexto(ventana, "Elige un movimiento",20,48,522)
        CrearTexto(ventana, uSlot1["name"],25,76,595,Rojo)
        CrearTexto(ventana, uSlot2["name"],25,276,595,Gris)
        CrearTexto(ventana, uSlot3["name"],25,76,645,Pink)
        CrearTexto(ventana, uSlot4["name"],25,276,645,LightBlue)
    elif MoveSet == 99:
        
        #Ataque seleccionado por jugador
        if lFlagAtaq["fSlot1"] == 1:
            AtaqueUser = uSlot1
        elif lFlagAtaq["fSlot2"] == 1:
            AtaqueUser = uSlot2
        elif lFlagAtaq["fSlot3"] == 1:
            AtaqueUser = uSlot3
        elif lFlagAtaq["fSlot4"] == 1:
            AtaqueUser = uSlot4

        #Si el PS de uno de los dos pokemon llega a 0:
        if PSzeroUser == 1:
            CrearTexto(ventana, f"{Chariz.name} se ha debilitado..",16,60,595)
            CrearTexto(ventana, "¡Has perdido el combate!",16,60,645)
            flagMyTurnEnd = 2
            EndBattle += 1
        elif PSzeroEnemy == 1:
            CrearTexto(ventana, "¡Has ganado el combate! Enhorabuena",18,60,595)
            CrearTexto(ventana, "Tu ego subio por las nubes :)",19,60,645)
            flagMyTurnEnd = 2
            EndBattle += 1

        #Compare velocidades Pokemon
        if CompareVel == 0:
            if Gengar.Vel < Chariz.Vel:
                FirstPok = Chariz
                FirstMove = AtaqueUser
                LastPok = Gengar
                LastMove = BSombra
            elif Gengar.Vel > Chariz.Vel:
                FirstPok = Gengar
                FirstMove = BSombra
                LastPok = Chariz
                LastMove = AtaqueUser
            CompareVel = 1

        #Entrar primer move del turno
        if flagMyTurnEnd == 0:

            if fAfterEstado == 0:
                printattck = FirstMove["name"]
                CrearTexto(ventana, f"¡{FirstPok.name} uso {printattck}!",20,60,595)

            DelayAttack += 1
            if DelayAttack == 22:
                
                if FirstMove["Catego"] != "Estado":
                    SFXplay(sfxHitFile, vol=0.6)
                    PSResult1 = TurnCalc(tipoMove = FirstMove["sType"],
                    PotMov         = FirstMove["Potencia"],
                    CategoriaMove  = FirstMove["Catego"],
                    VidaTarget     = LastPok.PS,
                    DefTarg        = LastPok.Defensa,
                    DefSpTarg      = LastPok.DefSp,
                    AtakUser       = FirstPok.Ataque,
                    SpecialAtkUser = FirstPok.AtaqueSp,
                    TipoPokUser    = FirstPok.tipo)
                    LastPok.PS = PSResult1
                    AtaqueTurn = 1
                elif FirstMove["Catego"] == "Estado":
                    EstadoRes = TurnCalcEstado(FirstMove,FirstPok)
                    fAfterEstado = 1

                #Si en el primer ataque muere un pokemon (PS a 0)
                if LastPok.PS == 0:
                    if FirstPok.EO == "user":
                        PSzeroEnemy = 1
                        fAfterEstado = 0
                    elif FirstPok.EO == "enemy":
                        PSzeroUser = 1
                        fAfterEstado = 0

            if AtaqueTurn == 1: #Atacamos, next turn
                DelayBetweenAtt += 1
                if DelayBetweenAtt == 10:
                    if PSzeroEnemy == 0 and PSzeroUser == 0:
                        flagMyTurnEnd = 1
                        AtaqueTurn = 0

            if fAfterEstado == 1: #Efecto move estado running
                
                if EstadoRes["stat"] == "PS":
                    FirstPok.PS = EstadoRes["result"]
                    CrearTexto(ventana, f"¡{FirstPok.name} ha restaurado sus PS!",18,60,595)
                    if SoundEstado == 0:
                        SFXplay(SFXhealFile, vol=0.5)
                        SoundEstado = 1
                elif EstadoRes["stat"] == "Vel":
                    FirstPok.Vel = EstadoRes["result"]
                    CrearTexto(ventana, f"¡La velocidad de {FirstPok.name} aumentó mucho!",16,60,595)
                    if SoundEstado == 0:
                        SFXplay(SFXboostFile, vol=0.5)
                        SoundEstado = 1
                
                DelayEfectEstado += 1
                if DelayEfectEstado == 17:
                    fAfterEstado = 99
            
            elif fAfterEstado == 99:

                if EstadoRes["stat"] == "PS":
                    CrearTexto(ventana, f"¡{FirstPok.name} ha restaurado sus PS!",18,60,595)
                elif EstadoRes["stat"] == "Vel":
                    CrearTexto(ventana, f"¡La velocidad de {FirstPok.name} aumentó mucho!",16,60,595)

                DelayBetweenAtt += 1
                if DelayBetweenAtt == 17:
                    flagMyTurnEnd = 1
                    fAfterEstado = 0
            
        #Ultimo pokemon en atacar
        if flagMyTurnEnd == 1:

            if fAfterEstado == 0:
                printSndAttck = LastMove["name"]
                CrearTexto(ventana, f"¡{LastPok.name} uso {printSndAttck}!",20,60,595)

            DelayEnemyAttack += 1
            if DelayEnemyAttack == 22:
                if LastMove["Catego"] != "Estado":
                    SFXplay(sfxHitFile, vol=0.6)
                    PSResult2 = TurnCalc(tipoMove = LastMove["sType"],
                    PotMov         = LastMove["Potencia"],
                    CategoriaMove  = LastMove["Catego"],
                    VidaTarget     = FirstPok.PS,
                    DefTarg        = FirstPok.Defensa,
                    DefSpTarg      = FirstPok.DefSp,
                    AtakUser       = LastPok.Ataque,
                    SpecialAtkUser = LastPok.AtaqueSp,
                    TipoPokUser    = LastPok.tipo)
                    FirstPok.PS = PSResult2
                elif LastMove["Catego"] == "Estado":
                    lEstadoRes = TurnCalcEstado(LastMove, LastPok)
                    fAfterEstado = 1

                #Si el ultimo en atacar mata al rival
                if FirstPok.PS == 0:
                    if LastPok.EO == "user":
                        PSzeroEnemy = 1
                    elif LastPok.EO == "enemy":
                        PSzeroUser = 1
                else:
                    flagTurnEnd = 1

            
            """ if fAfterEstado == 8: #Termina efecto move estado, end turn
                flagTurnEnd = 1 """
            if fAfterEstado == 1: #Efecto move estado running
                flagTurnEnd = 0
                
                if lEstadoRes["stat"] == "PS":
                    LastPok.PS = lEstadoRes["result"]
                    CrearTexto(ventana, f"¡{LastPok.name} ha restaurado sus PS!",18,60,595)
                    if lSoundEstado == 0:
                        SFXplay(SFXhealFile, vol=0.5)
                        lSoundEstado = 1
                elif lEstadoRes["stat"] == "Vel":
                    LastPok.Vel = lEstadoRes["result"]
                    CrearTexto(ventana, f"¡La velocidad de {LastPok.name} aumentó mucho!",16,60,595)
                    if lSoundEstado == 0:
                        SFXplay(SFXboostFile, vol=0.5)
                        lSoundEstado = 1
                
                lDelayEffEstado += 1
                if lDelayEffEstado == 17:
                    fAfterEstado = 99

            elif fAfterEstado == 99:
                flagTurnEnd = 1
                if lEstadoRes["stat"] == "PS":
                    #LastPok.PS = lEstadoRes["result"]
                    CrearTexto(ventana, f"¡{LastPok.name} ha restaurado sus PS!",18,60,595)
                elif lEstadoRes["stat"] == "Vel":
                    #LastPok.Vel = lEstadoRes["result"]
                    CrearTexto(ventana, f"¡La velocidad de {LastPok.name} aumentó mucho!",16,60,595)


        #Delay fin del turno
        if flagTurnEnd == 1:
            EndAttack += 1

    elif MoveSet == 101:
        if PSzeroUser == 1:
            CrearTexto(ventana, "Te has cagao... ¿Quieres volver a empezar?",16,48,522)
        elif PSzeroEnemy == 1:
            CrearTexto(ventana, "Buen trabajo, ¿Quieres volver a empezar?",16,48,522)
        CrearTexto(ventana, "Al toque mi rey",18,76,600)
        CrearTexto(ventana, "Mejor no, tengo lío",18,276,600)
        

    #Delay antes de huir
    if Cagao == 1:
        cUntilRun += 1

    # Actualizar ventana
    pygame.display.flip()

    # Velocidad animacion FPS
    reloj.tick(fps)

    # Pasar al siguiente frame:
    f_index = (f_index + 1) % len(frames)
    f_indexC = (f_indexC + 1) % len(framesC)
    f_indexG = (f_indexG + 1) % len(framesG)


# Salir del programa
#pygame.quit()