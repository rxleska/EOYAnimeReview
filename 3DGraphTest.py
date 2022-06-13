import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime

Anime = GetAnime()

fig = plt.figure()
ax = plt.axes(projection='3d')

x, y, z = [], [], []

for show in Anime['COMPLETED']:
    if show.definingChars.numberOfEpisodes < 39:
        x.append(show.rating.score)
        y.append(show.rating.meanScore)
        z.append(show.definingChars.numberOfEpisodes)
    # z = np.linspace(0, 1, 100)
    # x = z * np.sin(25 * z)
    # y = z * np.cos(25 * z)

ax.scatter3D(x, y, z, s=5)

plt.show()
