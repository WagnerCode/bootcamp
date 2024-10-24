import random

def generator(text, sep=" ", option=None):
    mesto = text.split(sep)

    if option == "shuffle":
        while len(mesto) != 0:
            yield (mesto.pop(random.randrange(len(mesto))))

    elif option == "ordered":
        mesto.sort()
        for item in mesto:
            yield item

    elif option == "unique":
        mesto.sort()
        for item in mesto:
            while mesto.count(item) > 1:
                mesto.remove(item)
            yield item
    elif option == None:
        for item in mesto:
            yield item

text = "Le Lorem Ipsum est simplement du faux texte."
#text = "Le Lorem Ipsum Le Lorem Ipsum Le Le Le"
for word in generator(text, sep=" ", option="ordered"):
    print(word)
