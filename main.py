import loger as L
import random as rand

logger = L.loger()

liste_rand = []

for i in range(25):
    for i in range(10):
        liste_rand += [rand.randrange(180)]
    print(liste_rand)
    logger.__add__(liste_rand)
    liste_rand = []

logger.archive()
print(logger.__repr__())
