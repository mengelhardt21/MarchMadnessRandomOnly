import random

def eval64 (seed1, seed2) :
    
    rand1 = seed1[1] * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2

def eval32 (seed1, seed2) :

    rand1 = seed1[1] * random.random() * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2
    
def eval16 (seed1, seed2) :

    rand1 = seed1[1] * random.random() * random.random() * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random() * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2
    
def eval8 (seed1, seed2) :

    rand1 = seed1[1] * random.random() * random.random() * random.random() * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random() * random.random() * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2
    
def eval4 (seed1, seed2) :

    rand1 = seed1[1] * random.random() * random.random() * random.random() * random.random() * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random() * random.random() * random.random() * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2

def eval2 (seed1, seed2) :

    rand1 = seed1[1] * random.random() * random.random() * random.random() * random.random() * random.random() * random.random() * random.random()
    rand2 = seed2[1] * random.random() * random.random() * random.random() * random.random() * random.random() * random.random() * random.random()

    if rand1 < rand2 :
        return seed1
    else :
        return seed2

def printWinner (team) :

    str = f"{team[0]}:{team[1]}"

    print(str)

s1 = eval64(('South',1),('South',16))
s2 = eval64(('South',8),('South',9))
s3 = eval64(('South',5),('South',12))
s4 = eval64(('South',4),('South',13))
s5 = eval64(('South',6),('South',11))
s6 = eval64(('South',3),('South',14))
s7 = eval64(('South',7),('South',10))
s8 = eval64(('South',2),('South',15))
s9 = eval32(s1, s2)
s10 = eval32(s3, s4)
s11 = eval32(s5, s6)
s12 = eval32(s7, s8)
s13 = eval16(s9, s10)
s14 = eval16(s11, s12)
s15 = eval8(s13, s14)

print("South Round of 64")
printWinner(s1)
printWinner(s2)
printWinner(s3)
printWinner(s4)
printWinner(s5)
printWinner(s6)
printWinner(s7)
printWinner(s8)
print("South Round of 32")
printWinner(s9)
printWinner(s10)
printWinner(s11)
printWinner(s12)
print("South Sweet Sixteen")
printWinner(s13)
printWinner(s14)
print("South Elite Eight")
printWinner(s15)

w1 = eval64(('West',1),('West',16))
w2 = eval64(('West',8),('West',9))
w3 = eval64(('West',5),('West',12))
w4 = eval64(('West',4),('West',13))
w5 = eval64(('West',6),('West',11))
w6 = eval64(('West',3),('West',14))
w7 = eval64(('West',7),('West',10))
w8 = eval64(('West',2),('West',15))
w9 = eval32(w1, w2)
w10 = eval32(w3, w4)
w11 = eval32(w5, w6)
w12 = eval32(w7, w8)
w13 = eval16(w9, w10)
w14 = eval16(w11, w12)
w15 = eval8(w13, w14)

print("West Round of 64")
printWinner(w1)
printWinner(w2)
printWinner(w3)
printWinner(w4)
printWinner(w5)
printWinner(w6)
printWinner(w7)
printWinner(w8)
print("West Round of 32")
printWinner(w9)
printWinner(w10)
printWinner(w11)
printWinner(w12)
print("West Sweet Sixteen")
printWinner(w13)
printWinner(w14)
print("West Elite Eight")
printWinner(w15)

e1 = eval64(('East',1),('East',16))
e2 = eval64(('East',8),('East',9))
e3 = eval64(('East',5),('East',12))
e4 = eval64(('East',4),('East',13))
e5 = eval64(('East',6),('East',11))
e6 = eval64(('East',3),('East',14))
e7 = eval64(('East',7),('East',10))
e8 = eval64(('East',2),('East',15))
e9 = eval32(e1, e2)
e10 = eval32(e3, e4)
e11 = eval32(e5, e6)
e12 = eval32(e7, e8)
e13 = eval16(e9, e10)
e14 = eval16(e11, e12)
e15 = eval8(e13, e14)

print("East Round of 64")
printWinner(e1)
printWinner(e2)
printWinner(e3)
printWinner(e4)
printWinner(e5)
printWinner(e6)
printWinner(e7)
printWinner(e8)
print("East Round of 32")
printWinner(e9)
printWinner(e10)
printWinner(e11)
printWinner(e12)
print("East Sweet Sixteen")
printWinner(e13)
printWinner(e14)
print("East Elite Eight")
printWinner(e15)

mw1 = eval64(('Midwest',1),('Midwest',16))
mw2 = eval64(('Midwest',8),('Midwest',9))
mw3 = eval64(('Midwest',5),('Midwest',12))
mw4 = eval64(('Midwest',4),('Midwest',13))
mw5 = eval64(('Midwest',6),('Midwest',11))
mw6 = eval64(('Midwest',3),('Midwest',14))
mw7 = eval64(('Midwest',7),('Midwest',10))
mw8 = eval64(('Midwest',2),('Midwest',15))
mw9 = eval32(mw1, mw2)
mw10 = eval32(mw3, mw4)
mw11 = eval32(mw5, mw6)
mw12 = eval32(mw7, mw8)
mw13 = eval16(mw9, mw10)
mw14 = eval16(mw11, mw12)
mw15 = eval8(mw13, mw14)

print("Midwest Round of 64")
printWinner(mw1)
printWinner(mw2)
printWinner(mw3)
printWinner(mw4)
printWinner(mw5)
printWinner(mw6)
printWinner(mw7)
printWinner(mw8)
print("Midwest Round of 32")
printWinner(mw9)
printWinner(mw10)
printWinner(mw11)
printWinner(mw12)
print("Midwest Sweet Sixteen")
printWinner(mw13)
printWinner(mw14)
print("Midwest Elite Eight")
printWinner(mw15)

f1 = eval4(s15, w15)
f2 = eval4(e15, mw15)

print("Final Four")
printWinner(f1)
printWinner(f2)

champ = eval2(f1, f2)
print("Champion")
printWinner(champ)