### Variables de configuracion
import os

##Variables RUTAS
MainMain = os.getcwd()
MainPath = MainMain+"\\Source_NoTocar"
#MainPath = "C:\\Users\\danie\\Documents\\MyStudio\\Pokemon_ChupadaDePito\\Source_NoTocar"
ImgCuadro = f"{MainPath}\\Img\\cuadro.png"
BgImg = f"{MainPath}\\Img\\fondo.png"
Icon = f"{MainPath}\\Img\\pokemon.png"
SprCharPath = f"{MainPath}\\Sprites\\Charizard"
SprGengPath = f"{MainPath}\\Sprites\\Gengar"
SprArrPath = f"{MainPath}\\Sprites\\FlechaS"
mFile = f"{MainPath}\\Music\\Music.mp3"
ABfile = f"{MainPath}\\Music\\SFX_PRESS_AB.wav"
FartFile = f"{MainPath}\\Music\\fart.wav"
sfxHitFile = f"{MainPath}\\Music\\Hit_Normal_Damage.mp3.mpeg"
SFXhealFile = f"{MainPath}\\Music\\In-Battle_Heal_HP_Restore_XY.mp3.mpeg"
SFXboostFile = f"{MainPath}\\Music\\boostStat.wav"

FPSs = 12

##Ventana Juego
ventana_ancho = 480
ventana_alto = 725

##Posiciones flecha
"""1    2
   3    4"""
dPos1 = {"x":30,"y":583}
dPos2 = {"x":230,"y":583}
dPos3 = {"x":30,"y":633}
dPos4 = {"x":230,"y":633}

##Stats
PuntosSalud = 100
TotSalud = 100

PSenemigo = 100
TotPSenemigo = 100

##AtaquesUsuarioFlags
lFlagAtaq = {"fSlot1":0,"fSlot2":0,"fSlot3":0,"fSlot4":0}

Rojo = (255,0,0)
Verde = (92, 184, 67)
Gris = (100,100,100)
LightBlue = (0,162,198)
Pink = (255, 60, 217)