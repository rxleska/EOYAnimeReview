import numpy as np
import matplotlib.pyplot as plt
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime

Anime = GetAnime()

fig = plt.figure()
ax = plt.axes()

x, y = [], []

for show in Anime['COMPLETED']:
    x.append(show.progression.finished.month)
    y.append(show.rating.score)
    # z = np.linspace(0, 1, 100)
    # x = z * np.sin(25 * z)
    # y = z * np.cos(25 * z)

ax.scatter(x, y, s=5)

plt.show()
