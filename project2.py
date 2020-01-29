from random import randint as ri

A=ri (0, 10)
B=ri (0, 10)
C=ri (0, 10)

if A > B:
    print ("пьорфект!")
elif A < B:
    print ("грусть(")
elif A == B:
    print ("Теперь эта!")
    if (A + B) < C:
        print ("фантастик!")
    elif (A + B) > C:
        print ("всё тлен!")
    elif (A + B) == C:
        print ("Страдания!")
