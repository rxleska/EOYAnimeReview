import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import Anime
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime


def GetTotal(arr):
    i = 0
    for x in arr:
        i = i + x
    return i


Anime = GetAnime()

fig = plt.figure()
ax = plt.axes(projection='3d')

x, y, z = [], [], []


for show in Anime['COMPLETED']:
    xa = show.rating.score
    scoreDist = show.rating.mediaStats.scoreDistribution
    distTotal = GetTotal(scoreDist.values())
    for distKey in scoreDist.keys():
        ya = distKey
        za = scoreDist[distKey]/distTotal

        x.append(xa)
        y.append(ya)
        z.append(za)
    # z = np.linspace(0, 1, 100)
    # x = z * np.sin(25 * z)
    # y = z * np.cos(25 * z)

ax.scatter3D(x, y, z, s=5)

plt.show()
