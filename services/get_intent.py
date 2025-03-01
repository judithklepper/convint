## extract intent start (maar eerst Spacy???)
def get_numerics(textnum, numwords={}):
    #code Bas om nummers te extracten
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]
        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    return result + current



def which_course(request):
    first_course = ['starter', 'soup', 'first course', 'appetizer', 'entree']
    main_course = ['main course', 'main dish']
    dessert = ['dessert', 'desert', 'sweet treat', 'pastry', 'pudding', 'sweet course']

    request_split = request.split()
    course = ""
    for w in request_split:
        if w not in first_course or main_course or dessert:
            course = "Unknown"

        #        @...TODO


def amount_of_persons(request):
    for w in request:
        if get_numerics(w) == int:
            persons = get_numerics(w)
        else:
            persons = "Unknown"
        return persons
