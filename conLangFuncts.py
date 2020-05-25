import random

def consonantInv():
    conNum = random.choice(range(6,59))
    conList = ["p","b","m","ʙ","ɸ","β","ɱ","ⱱ","f","v","ʋ","t","d","n","r","ɾ","θ","ð","s","z","ʃ","ʒ","ɬ","ɮ","ɹ","l","ʈ","ɖ","ɳ","ɽ","ʂ","ʐ","ɻ","ɭ","c","ɟ","ɲ","ç","ʝ","j","ʎ","k","g","ŋ","x","ɣ","ɰ","ʟ","q","ɢ","ɴ","ʀ","χ","ʁ","ħ","ʕ","ʔ","h","ɦ"]
    conWeights = [83.1,63.6,94.2,0.0,8.6,12.0,0.2,0.2,39.9,21.1,1.3,40.1,26.6,44.8,21.1,1.6,4.0,4.9,43.5,13.7,41.5,13.5,5.3,0.7,2.4,38.6,7.5,6.0,5.3,3.1,0.2,0.9,3.8,6.0,12.0,9.5,31.3,2.4,2.7,83.8,4.4,89.4,56.1,52.5,20.8,12.2,2.7,0.2,11.5,3.1,0.2,0.9,9.8,4.9,4.2,2.2,47.9,61.9,3.5]
    cInventory = [ ]
    while len(cInventory) < conNum:
        consonant = random.choices(conList, weights=conWeights, k=1)
        if consonant not in cInventory:
            cInventory.append(consonant)
    return cInventory

def vowelInv():
    vowelNum = random.choice(range(2,28))
    vowelList = ["i","y","ɨ","ʉ","ɯ","u","ɪ","ʏ","ʊ","e","ø","ɘ","ɵ","ɤ","o","ə","ɛ","œ","ɜ","ɞ","ʌ","ɔ","æ","ɐ","a","ɶ","ɑ","ɒ"]
    vowelWeights = [87.1,5.3,13.5,1.3,9.1,81.8,16.4,0.9,14.6,37.5,2.7,4.4,0.9,2.7,40.1,16.9,41.2,1.8,3.3,0.2,2.2,35.9,8.6,3.1,5.8,0.0,5.5,4.2]
    vInventory = [ ]
    while len(vInventory) < vowelNum:
        vowel = random.choices(vowelList, weights=vowelWeights, k=1)
        if vowel not in vInventory:
            vInventory.append(vowel)
    return vInventory

## phoneme frequencies from here: http://web.phonetik.uni-frankfurt.de/upsid_segment_freq.html
