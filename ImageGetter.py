from urllib import response
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime
from PIL import Image
import requests
from io import BytesIO


def removeCharsNotAllowedInFileNames(strng):
    s = strng
    s = s.replace(" ", "~")
    s = s.replace("/", "")
    s = s.replace("\\", "")
    s = s.replace(":", "")
    s = s.replace("*", "")
    s = s.replace("?", "")
    s = s.replace("\"", "")
    s = s.replace("<", "")
    s = s.replace(">", "")
    s = s.replace("|", "")
    s = s.replace(".", "")
    s = s.replace("'", "")
    return s


anime = GetAnime()

jsonRep = "{\"Characters\":["
for show in anime["COMPLETED"]:
    try:
        # Gets show name
        showName = show.name.english if not (show.name.english == None or show.name.english == "") else (
            show.name.synonyms[0] if not (len(show.name.synonyms) < 1 or show.name.synonyms[0] == None or show.name.synonyms[0] == "") else show.name.native)

        showImg = show.imgs.coverImage[0]
        sRes = requests.get(showImg)
        simg = Image.open(BytesIO(sRes.content))
        sfp = "out\\show\\" + \
            removeCharsNotAllowedInFileNames(showName) + ".png"
        with open(sfp, 'wb') as s:
            simg.save(s)
            s.close

        for character in show.characters:
            try:
                # Gets Character name
                characterName = character.userPreferedName if not (
                    character.userPreferedName == None or character.userPreferedName == "") else character.nativeName
                role = character.role
                charImg = character.image
                age = character.age
                dob = character.birthday
                bloodtype = character.bloodType
                gend = character.gender
                des = character.description

                cRes = requests.get(charImg)
                cimg = Image.open(BytesIO(cRes.content))
                cfp = "out\\char\\" + \
                    removeCharsNotAllowedInFileNames(characterName)+"~" + \
                    removeCharsNotAllowedInFileNames(showName)+".png"
                with open(cfp, 'wb') as c:
                    cimg.save(c)
                    c.close

                x = {
                    "showName": showName.replace("\"", ""),
                    "showImgRel": removeCharsNotAllowedInFileNames(showName)+".png",
                    "character": characterName.replace("\"", ""),
                    "role": role.__str__().replace("\"", ""),
                    "imgRel": removeCharsNotAllowedInFileNames(characterName)+"~"+removeCharsNotAllowedInFileNames(showName)+".png",
                    "age": age.__str__().replace("\"", ""),
                    "bt": bloodtype.__str__().replace("\"", ""),
                    "gender": gend.__str__().replace("\"", ""),
                    "desc": des.__str__().replace("\'", "").replace("\"", "")
                }
                jsonRep = jsonRep + "\n" + x.__str__() + ","
            except:
                print(characterName)
                continue
    except:
        print(showName)
        continue


jsonRep = jsonRep[:-1] + "]}"

with open("out/out.json", 'w', encoding='utf-8') as file:
    file.write(jsonRep.replace("\'", "\""))
    file.close()
