
from dane_x_y import Ux, Uy, Nx, Ny, Mx, My, ERx, ERy, KIx, KIy, DOTx, DOTy,SMILEx,SMILEy, NOSEx
from dane_x_y import Sx,Sy, Ax, Ay, SUx, SUy ,Px,Py,ER2x,ER2y,EYE1x,EYE1y,EYE2x,EYE2y, NOSEy
from implementacja import s
import matplotlib.pyplot as plt

plt.gca().set_aspect('equal')
linewidthg = 0.7
colorg = "#95003d"

def drawN():
    M = 100
    ui = [i / M for i in range(M)]
    tN = [i / len(Nx) for i in range(len(Nx))]
    sxN = s(tN, Nx)
    syN = s(tN, Ny)
    line = plt.plot([sxN(u) for u in ui],[syN(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color=colorg)
def drawU():
    M = 40
    ui = [i / M for i in range(M)]
    tU = [i / len(Ux) for i in range(len(Ux))]
    sxU = s(tU, Ux)
    syU = s(tU, Uy)
    line = plt.plot([sxU(u) for u in ui],[syU(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color=colorg)


def drawM():
    M = 90
    ui = [i / M for i in range(M)]
    tM = [i / len(Mx) for i in range(len(Mx))]
    sxM = s(tM, Mx)
    syM = s(tM, My)
    line = plt.plot([sxM(u) for u in ui],[syM(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawER():
    M = 100
    ui = [i / M for i in range(M)]
    tM = [i / len(ERx) for i in range(len(ERx))]
    sxER = s(tM, ERx)
    syER = s(tM, ERy)
    line = plt.plot([sxER(u) for u in ui],[syER(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawKI():
    M = 100
    ui = [i / M for i in range(M)]
    tM = [i / len(KIx) for i in range(len(KIx))]
    sxKI = s(tM, KIx)
    syKI = s(tM, KIy)
    line = plt.plot([sxKI(u) for u in ui],[syKI(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawIDOT():
    M = 55
    ui = [i / M for i in range(M)]
    tM = [i / len(DOTx) for i in range(len(DOTx))]
    sxDOT = s(tM, DOTx)
    syDOT = s(tM, DOTy)
    line = plt.plot([sxDOT(u) for u in ui],[syDOT(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawS():
    M = 60
    ui = [i / M for i in range(M)]
    tM = [i / len(Sx) for i in range(len(Sx))]
    sxS = s(tM, Sx)
    syS = s(tM,Sy)
    line = plt.plot([sxS(u) for u in ui],[syS(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawA():
    M = 70
    ui = [i / M for i in range(M)]
    tM = [i / len(Ax) for i in range(len(Ax))]
    sxA = s(tM, Ax)
    syA = s(tM, Ay)
    line = plt.plot([sxA(u) for u in ui],[syA(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawSU():
    M = 140
    ui = [i / M for i in range(M)]
    tM = [i / len(SUx) for i in range(len(SUx))]
    sxSU = s(tM, SUx)
    sySU = s(tM, SUy)
    line = plt.plot([sxSU(u) for u in ui],[sySU(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawP():
    M = 150
    ui = [i / M for i in range(M)]
    tM = [i / len(Px) for i in range(len(Px))]
    sxP = s(tM, Px)
    syP = s(tM, Py)
    line = plt.plot([sxP(u) for u in ui],[syP(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawER2():
    M = 90
    ui = [i / M for i in range(M)]
    tM = [i / len(ER2x) for i in range(len(ER2x))]
    sxER2 = s(tM, ER2x)
    syER2 = s(tM, ER2y)
    line = plt.plot([sxER2(u) for u in ui],[syER2(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawEYE1():
    M = 30
    ui = [i / M for i in range(M)]
    tM = [i / len(EYE1x) for i in range(len(EYE1x))]
    sxEYE1 = s(tM, EYE1x)
    syEYE1 = s(tM, EYE1y)
    line = plt.plot([sxEYE1(u) for u in ui],[syEYE1(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawEYE2():
    M = 30
    ui = [i / M for i in range(M)]
    tM = [i / len(EYE2x) for i in range(len(EYE2x))]
    sxEYE2 = s(tM, EYE2x)
    syEYE2 = s(tM, EYE2y)
    line = plt.plot([sxEYE2(u) for u in ui],[syEYE2(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawSMILE():
    M = 20
    ui = [i / M for i in range(M)]
    tM = [i / len(SMILEx) for i in range(len(SMILEx))]
    sxSMILE = s(tM, SMILEx)
    sySMILE = s(tM, SMILEy)
    line = plt.plot([sxSMILE(u) for u in ui],[sySMILE(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawNOSE():
    M = 10
    ui = [i / M for i in range(M)]
    tM = [i / len(NOSEx) for i in range(len(NOSEx))]
    sxNOSE = s(tM, NOSEx)
    syNOSE = s(tM, NOSEy)
    line = plt.plot([sxNOSE(u) for u in ui],[syNOSE(u) for u in ui],linewidth = linewidthg)
    plt.setp(line, color = colorg)

def drawSMILEY():
    drawEYE1()
    drawEYE2()
    drawSMILE()
    drawNOSE()
def drawNUMERKI_SA_SUPER():
    drawN()
    drawU()
    drawM()
    drawER()
    drawKI()
    drawS()
    drawA()
    drawSU()
    drawP()
    drawER2()
    drawSMILEY()
    drawIDOT()
    plt.show()

drawNUMERKI_SA_SUPER()


