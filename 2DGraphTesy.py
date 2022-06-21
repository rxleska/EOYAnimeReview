import numpy as np
import matplotlib.pyplot as plt
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime


Anime = GetAnime()

# fig = plt.figure()
# ax = plt.axes()

f, diagram = plt.subplots(1)

# x, y = [], []
# count = 0
# outOf = 0
# types = set()

for show in Anime['COMPLETED']:
    # for character in show.characters:
    #     outOf = outOf + 1
    #     if (not character.bloodType == None) and (not character.bloodType == "Unknown"):
    #         count = count + 1
    #         types.add(character.bloodType)

    x = (show.rating.score)
    y = (len(show.tags))
    diagram.plot(x, y, 'bo')
    diagram.annotate(show.name.english, (x, y), fontsize=6)
    # z = np.linspace(0, 1, 100)
    # x = z * np.sin(25 * z)
    # y = z * np.cos(25 * z)

# print(f'{count} out of {outOf}')
# print(types.__str__())

# ax.scatter(x, y, s=5)

plt.show()
