import random
def main():
    randomquantity=generate_quantity()
    randomtense=generate_tense()
    print(make_sentence(1,"past"))
    print(make_sentence(1,"past"))
    print(make_sentence(1, "present"))
    print(make_sentence(3,"past"))
    print(make_sentence(2,"present"))
    print(make_sentence(4,"future"))
    print("See also:")
    print(make_sentence(randomquantity,randomtense))
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    quantity=quantity
    tense=tense
    sentence = str.capitalize(f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)} {get_prepositional_phrase(quantity)}.")
    capitalized_sentence=str.capitalize(sentence)
    return sentence
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity==1:
        nouns=[ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns=[ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    noun=random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs=["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif (tense == "present" and quantity == 1):
        verbs=[ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif (tense == "present" and quantity != 1):
        verbs=[ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs=[ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    verb = random.choice(verbs)
    return verb
def generate_tense():
    tenses = ["past", "present", "future"]
    tense=random.choice(tenses)
    return tense
def generate_quantity():
    quantities = [1, 3]
    quantity= random.choice(quantities)
    return quantity
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition=random.choice(prepositions)
    return preposition
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    prepositionalPhrase= (f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}")
    return prepositionalPhrase
def get_adjective():
    adjectives= ["quick", "slow", "sloppy", "difficult", "joyous", "charged", "energized", "plotting", "tall"]
    adjective=random.choice(adjectives)
    return adjective
main()