import random

def prepareClearText(clearText):

    clearText = [int(i) for i in clearText]
    return clearText

def prepareKey():
    key = list(range(0, 256))
    key = random.sample(range(0,256),4)
    return key

def prepareSBox():

    sBox = list(range(0,256))
    sBox = random.sample(range(0,256),256)
    return sBox

def preparePermutation():

    permutation = list(range(0,4))
    permutation = random.sample(range(0,4),4)
    return permutation

def getSBoxText(sBox,clearText):

    modified = []
    for i in range(4):
         modified.append(sBox[clearText[i]])
    return modified

def getPermutationText(permutation,modText):

    modified = []
    for i in range(4):
        modified.append(modText[permutation[i]])
    return modified

def getXor(key,modText2):

    for i in range(len(modText2)):
        modText2[i] = modText2[i] ^ key[i]
    return modText2

def encryptSPN(clearText,key,sBox,permutation):

    modText = getSBoxText(sBox, clearText)
    modText2 = getPermutationText(permutation, modText)
    modText3 = getXor(key, modText2)

    return modText3

def inversePermutation(encryptedText: object, permutation: object) -> object:

    inverse =[0,0,0,0]
    result = [0,0,0,0]
    for i in range(4):
        inverse[permutation[i]]  = i
    for i in range(4):
        result[i] = encryptedText[inverse[i]]
    return result

def inverseSBox(encryptedText,sBox):

    result =[]
    for i in range(4):
        result.append(sBox.index(encryptedText[i]))
    return result

def decryptSPN(encryptedText,key,sBox,permutation):

    modText1 = getXor(key,encryptedText)
    modText2 = inversePermutation(modText1,permutation)
    modText3 = inverseSBox(modText2,sBox)

    return modText3