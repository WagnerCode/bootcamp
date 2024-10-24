def text_analyzer(text=None):
    if text == None:
        print("What is the text to analyze?")
        text = input()
        print("The text contains", len(text), "printable character(s):")
        i = 0
        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        for letter in text:
            if text[i].islower():
                lower += 1
            elif text[i].isupper():
                upper += 1
            elif text[i].isspace():
                space += 1
            elif not (text[i].isnumeric()):
                punctuation += 1
            i += 1
        print("lower", lower)
        print("upper", upper)
        print("punctuation", punctuation)
        print("space", space)
    else:
        print("The text contains", len(text), "printable character(s):")
        i = 0
        upper = 0
        lower = 0
        punctuation = 0
        space = 0
        for letter in text:
            if text[i].islower():
                lower += 1
            elif text[i].isupper():
                upper += 1
            elif text[i].isspace():
                space += 1
            elif not (text[i].isnumeric()):
                punctuation += 1
            i += 1
        print("lower", lower)
        print("upper", upper)
        print("punctuation", punctuation)
        print("space", space)
