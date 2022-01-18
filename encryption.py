from re import X
from random import uniform
import time
from hashlib import sha256, sha3_256
from chaos_model import Chaos
import numpy as np
#from chaos_model 
chaosM = Chaos()
X=[uniform(-12,12),uniform(-12,12),uniform(-12,12)] #Chaos 起始值
chaosX = np.array(X).transpose()
time.sleep(1)

a=""
while True:
    a = input("----------輸入q結束----------")
    if a == 'q':
        break
    else:
        chao=sha3_256(str(round(chaosX[0]*(10**5))).encode('utf-8')).hexdigest()
        print("chaotic numbers   : ", chao)     #混沌系統經由SHA256疊代亂數
        chaosX =chaosM.runChaos(chaosX)
    time.sleep(0.1)
