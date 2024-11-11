import pygame
from Config import *
from pygame import mixer

#Insertar imagen en la interfaz del juego
def CrearImagen(ventana, rutaImg, anchoImg, altoImg, px, py):
    # Cargar PNG
    ruta_imagen = rutaImg
    imagen = pygame.image.load(ruta_imagen).convert_alpha()
    # Redimensionar imagen
    iBattleImg = pygame.transform.scale(imagen, (anchoImg, altoImg))
    # Obtener rect imagen
    iBattleRect = iBattleImg.get_rect()
    # Inicio posicion de imagen en la ventana
    iBattleRect.x = px
    iBattleRect.y = py
    ventana.blit(iBattleImg, iBattleRect)


def CrearTexto(ventana, vTexto, tamTxt, posX, posY, color=(0,0,0)):
    # Crear un objeto de fuente
    fuente = pygame.font.SysFont("Consolas", tamTxt)
    Textvar = vTexto
    superficie_texto = fuente.render(Textvar, True, color)

    # Obtener el rectángulo del texto
    rect_texto = superficie_texto.get_rect()

    # Colocar el texto en coordenadas especificas
    rect_texto.x = posX
    rect_texto.y = posY
    ventana.blit(superficie_texto, rect_texto)

def OstBattle(mFile, Vol=0.2):
    MusicBattle = mFile
    mixer.init()
    audioOst = mixer.Sound(MusicBattle)
    audioOst.set_volume(Vol)
    CanalOst = audioOst.play(-1)
    # El segundo argumento -1 indica reproducir en bucle
    return CanalOst

def SFXplay(iFile, vol=0.2):
    MusicBattle = iFile
    mixer.init()
    audio = mixer.Sound(MusicBattle)
    audio.set_volume(vol)
    CanalSFX1 = audio.play()
    return CanalSFX1

def SpriteGenerate(vSprCharPath, ancho, alto):
    framesC = []
    CharPath = vSprCharPath
    sortCharPath = sorted(os.listdir(CharPath),key=str.lower)
    for file in sortCharPath:
        PngFrame = os.path.join(CharPath, file)
        ImgPok = pygame.image.load(PngFrame).convert_alpha()
        ImgScale = pygame.transform.scale(ImgPok, (ancho, alto))
        #412, 338
        framesC.append(ImgScale)
    return framesC