import random

def d10():
    return random.randint(1,10)
def d100():
    return random.randint(1,100)

# Returns the key value of a random weighted selection
# input Array Options, Array Options weight. Output: Selected Option
def roulette(options, weight):
    max = sum(weight)
    pick = random.uniform(0, max)
    current = 0
    for i, j in enumerate(weight):
        current += j
        if current > pick:
            return options[i]

# Rolls for a random distinguishing mark
def genDistinguisingMark():
    marks = ["Pox Marks", "Ruddy Face", "Scar", "Tattoo", "Earring", "Ragged Ear", "Nose Ring", "Wart", "Broken Nose",
             "Missing Tooth", "Snaggle Teeth", "Lazy Eye", "Missing Eyebrow(s)", "Missing Digit", "Missing Nail",
             "Distinctive Gait", "Curious Smell", "Huge Nose", "Large Mole", "Small Bald Patch",
             "Strange Colored Eye(s)"]
    weights = [5, 5, 5, 5, 5, 4, 6, 4, 6, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 4, 2]

    return roulette(marks, weights)

# Rolls for a random star sign
def genStarSign():
    signs = ["Wymund the Anchorite", "The Big Cross", "The Limner's Line", "Gnuthus the Ox", "Dragomas the Drake",
             "The Gloaming", "Grungni's Baldric", "Mammit the Wise", "Mummit the Fool", "The Two Bullocks",
             "The Dancer", "The Drummer", "The Piper", "Vobist the Faint", "The Broken Cart", "The Greased Goat",
             "Rhya's Cauldron", "Cackelfax the Cockerel", "The Bonesaw", "The Witchling Star"]
    weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 2]
    return roulette(signs, weights)

def genHumanBirthplace():
    out = ""
    province = ["Averland", "Hochland", "Middenland", "Nordland", "Ostermark", "Ostland", "Reikland", "Stirland",
                "Talabeclad", "Wissenland"]
    out += random.choice(province)+" "
    if out == "Averland ":
        out+= roulette(["Averheim (Capital City)", "Grenzstadt (Town)", "Hochsleben (Town)", "Loningbruck (Town)",
                        "Wuppertal (Town)", "Agbeiten (Villiage)", "Braundorf (Villiage)", "Kotzenheim (Villiage)",
                        "Zecher (Villiage)"], [25, 10, 10, 9, 9, 9, 9, 10, 10 ])

    elif out == "Hochland ":
        out += roulette(["Hergig (Capital City)", "Breder (Town)", "Krudenwalf (Town)",
                         "Bergendorf (Villiage)", "Esk (Villiage)", "Gruyden (Villiage)", "Koerin (Villiage)"],
                        [25, 13, 13, 13, 13, 13, 10])
    elif out == "Middenland ":
        out += roulette(["Middenheim (Capital City)", "Delberz (Town)", "Grimminhagen (Town)", "Norderingen (Town)",
                         "Holzbeck (Villiage)", "Immelscheld (Villiage)", "Pritzstock (Villiage)", "Sokh (Villiage"],
                         [25, 12, 12, 11, 10, 10, 10, 10])

    elif out == "Nordland ":
        out += roulette(["Salzenmund (Capital City)", "Beecerhoven (Town)", "Dietershafen (Town)",
                         "Grafenrich (Villiage)", "Luftburg (Villiage)", "Oldenlitz (Villiage)",
                         "Wilhelmskoog (Villiage)"], [25, 13, 13, 13, 13, 13, 10])
    elif out == "Ostermark ":
        out += roulette(["Bechafen (Capital City)", "Eisental (Town)", "Remer (Town)", "Bissendorf (Villiage)",
                         "Dorna (Villiage)", "Fortenhaf (Villiage)", "Heffengen (Villiage)"],
                        [25, 12, 12, 11, 10, 10, 10])
    elif out == "Ostland ":
        out += roulette(["Wolfenburg (Capital City)", "Ferlangen (Town)", "Vandengart (Town)", "Boven (Villiage)",
                         "Lubrecht (Villiage)", "Smallhof (Villiage)", "Zundap (Villiage)"],
                        [25, 12, 12, 11, 10, 10, 10])

    elif out == "Reikland ":
        out += roulette(["Altdorf (Imperial Capital City)", "Nuln (City)", "Bogenhafen (Town)", "Grunburg (Town)",
                         "Halheim (Villiage)", "Misthausen (Villiage)", "Teufelfeuer (Villiage)",
                         "Weissbruck (Villiage)"], [25, 15, 10, 10, 10, 10, 10, 10])
    elif out == "Stirland ":
        out += roulette(["Wurtbad (Capital City)", "Drakenhof (Town)", "Waldenhof (Town)", "Eschedorf (Villiage)",
                         "Furtzhausen (Villiage)", "Schwartzhafen (Villiage)", "Wurstheim (Villiage)"],
                        [25, 12, 12, 11, 10, 10, 10])
    elif out == "Talabeclad ":
        out += roulette(["Talabheim (Capital City)", "Bek (Town)", "Kemperbad (Town)", "Garndorf (Villiage)",
                         "Rangenhof (Villiage)", "Wellenborn (Villiage)", "Zurin (Villiage)"],
                        [25, 12, 12, 11, 10, 10, 10])
    elif out == "Wissenland ":
        out += roulette(["Wissenburg (Capital City)", "Grissenwald (Town)", "Pfeildorf (Town)",
                         "Ambosstein (Villiage)", "Koningsdorf (Villiage)", "Segeldorf (Villiage)",
                         "Steingart (Villiage)"], [25, 12, 12, 11, 10, 10, 10])
    return out

def genHumanRandomTalent():
    return roulette(["Acute Hearing", "Ambidextrous", "Coolheaded", "Excellent Vision",
              "Fleet Footed", "Hardy", "Lightning Reflexes", "Luck", "Marksman",
              "Mimic", "Night Vision", "Resistance to Disease", "Resistance to Magic",
              "Resistance to Poison", "Savvy", "Sixth Sense", "Strong-Minded", "Sturdy",
              "Suave", "Super Numerate", "Very Resilient", "Very Strong", "Warrior Born"],
             [4, 5, 4, 5, 4, 5, 4, 4, 5, 4, 5, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 5])

class wFRPChar:
    # Initizes the character
    def __init__(self):
            self.race = ""
            self.sex = ""
            self.career = ""
            self.stats = []
            # Initilizes only main stats (2d10). Secondary will be computed in the races.
            new = []
            for x in range(8):
                new.append(d10() + d10())
            self.stats.append(new)
            self.skills = []
            self.talents = []
            self.height = ""
            self.weight = ""
            self.hairColor = ""
            self.eyeColor = ""
            self.distMarks = ""
            self.siblings = 0
            self.starSign = ""
            self.age = 0
            self.birthPlace = ""
            self.Name = ""

    # TODO: Dwarf Names need to be done
    def genDwarf(self):
        self.skills.extend(["Common Knowledge(Dwarfs)", "Speak Language(Khazalid)", "Speak Language(Reikspiel)",
                            "Trade(Miner, Smith, or Stoneworker)"])
        self.talents.extend(["Dwarfcraft", "Grudge-born Fury", "Night Vision", "Resistance to Magic", "Stout-hearted",
                             "Sturdy"])
        # Main Stats
        for x in range(8):
            if x == 0 or x == 3:
                self.stats[0][x]+=30
            elif x == 4 or x == 7:
                self.stats[0][x] += 10
            else:
                self.stats[0][x] += 20

        # Secondary Stats
        sec = []
        # Attacks
        sec.append(1)
        # Wounds
        sec.append(roulette([11, 12, 13, 14], [3, 3, 3, 1]))
        # SB & TB
        sec.append(self.stats[0][2] // 10)
        sec.append(self.stats[0][3] // 10)
        # M, Mag, IP
        sec.extend([3, 0, 0])
        # FP
        sec.append(roulette([1, 2, 3], [4, 3, 3]))
        self.stats.append(sec)

        #Height
        if self.sex == "M":
            potato = 52 + d10()
            self.height = str(potato // 12)+"'"+str(potato%12)+"''"
        else:
            potato = 50 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"

        #Weight
        lbs = []
        for x in range(20):
            lbs.append(90 + (x * 5))
        self.weight = roulette(lbs, [1, 2, 2, 3, 4, 5, 5, 7, 8, 12, 15, 7, 7, 5, 5, 4, 3, 2, 2, 1])

        #HairColor
        self.hairColor = random.choice(["Ash Blonde", "Yellow", "Red", "Copper", "Light Brown", "Brown",
                                        "Brown", "Dark Brown", "Blue Black", "Black"])

        # Eye Color
        self.eyeColor = random.choice(["Pale Grey", "Blue", "Copper", "Light Brown", "Light Brown", "Brown", "Brown",
                                       "Dark Brown", "Dark Brown", "Purple"])

        # Siblings
        self.siblings = roulette([0, 1, 2, 3], [3, 4, 2, 1])

        # Age
        age = []
        for x in range(20):
            age.append(20 + (x * 5))
        self.age = random.choice(age)

        # Birthplace
        self.birthPlace = roulette(["Human", "Karak Norn (Grey Mountains)", "Karak Izor (The Vaults)",
                                    "Karak Hirn (Black Mountians", "Karak Kadrin (World's Edge Mountains)",
                                    "Karaz-A-Karak (World's Edge Mountains)", "Zhufbar (World's Edge Mountains)",
                                    "Barak Varr (The Black Gulf)"], [30, 10, 10, 10, 10, 10, 10, 10])
        if self.birthPlace == "Human":
            self.birthPlace = genHumanBirthplace()

        # Career Selection
        cars = ["Agitator", "Bodyguard", "Burgher", "Coachman", "Entertainer", "Hunter", "Jailer", "Marine",
                "Mercenary", "Militiaman", "Miner", "Noble", "Outlaw", "Pit Fighter", "Protagonist", "Ratcatcher",
                "Runebearer", "Scribe", "Seaman", "Servant", "Shieldbreaker", "Smuggler", "Soldier", "Student", "Thief",
                "Toll Keeper", "Tomb Robber", "Tradesman", "Troll Slayer", "Watchman"]
        self.career = roulette(["Agitator", "Bodyguard", "Burgher", "Coachman", "Entertainer", "Hunter", "Jailer",
                                "Marine", "Mercenary", "Militiaman", "Miner", "Noble", "Outlaw", "Pit Fighter",
                                "Protagonist", "Ratcatcher", "Runebearer", "Scribe", "Seaman", "Servant",
                                "Shieldbreaker", "Smuggler", "Soldier", "Student", "Thief", "Toll Keeper",
                                "Tomb Robber", "Tradesman", "Troll Slayer", "Watchman"],
                               [2, 4, 4, 2, 4, 4, 4, 1, 6, 4, 6, 2, 4, 5, 4, 4, 5, 2, 1, 2, 4, 3, 4, 2, 3, 3,
                                3, 4, 4, 2])

    # TODO: Elf Careers and Names need to be done
    def genElf(self):
        self.skills.extend(["Common Knowledge(Elves)", "Speak Language(Eltharin)", "Speak Language(Reikspiel)"])
        self.talents.extend(["Aethyric Attunement or SWG (Longbow)", "Coolheaded or Savvy", "Excellent Vision",
                             "Night Vision"])
        # Main Stats
        for x in range(8):
            if x == 1 or x == 4:
                self.stats[0][x] += 30
            else:
                self.stats[0][x] += 20

        # Secondary Stats
        sec = []
        # Attacks
        sec.append(1)
        # Wounds
        sec.append(roulette([9, 10, 11, 12], [3, 3, 3, 1]))
        # SB & TB
        sec.append(self.stats[0][2] // 10)
        sec.append(self.stats[0][3] // 10)
        # M, Mag, IP
        sec.extend([5, 0, 0])
        # FP
        sec.append(roulette([1, 2], [4, 6]))
        self.stats.append(sec)

        # Height
        if self.sex == "M":
            potato = 62 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"
        else:
            potato = 60 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"

        # Weight
        lbs = []
        for x in range(20):
            lbs.append(80 + (x * 5))
        self.weight = roulette(lbs, [1, 2, 2, 3, 4, 5, 5, 7, 8, 12, 15, 7, 7, 5, 5, 4, 3, 2, 2, 1])

        # HairColor
        self.hairColor = random.choice(["Silver", "Ash Blonde", "Corn", "Yellow", "Copper", "Light Brown",
                                        "Light Brown", "Brown", "Dark Brown", "Black"])

        # Eye Color
        self.eyeColor = random.choice(["Grey Blue", "Blue", "Green", "Copper", "Light Brown", "Brown", "Dark Brown",
                                       "Silver", "Purple", "Black"])

        # Siblings
        self.siblings = roulette([0, 1, 2, 3], [1, 4, 4, 1])

        # Age
        age = []
        for x in range(20):
            age.append(30 + (x * 5))
        self.age = random.choice(age)

        # Birthplace
        self.birthPlace = roulette(["Reikland Altdorf (Imperial Capital City)", "The Wasteland Marienburg (City)",
                                    "Laurelorn Forest", "The Great Forest", "Reikwald Forest"],
                                   [20, 20, 30, 15, 15])

    # TODO: Halfling Careers and Names
    def genHalfling(self):
        self.skills.extend([ "Academic Knowledge(Genealogy/Heraldry)", "Common Knowledge(Halflings)", "Gossip",
                             "Speak Language(Halfling)", "Speak Language(Reikspiel)", "Trade(Cook or Farmer)"])
        self.talents.extend(["Night Vision", "Resistance to Chaos", "SWG (Sling)"])
        self.talents.append(roulette(["Acute Hearing", "Ambidextrous", "Coolheaded", "Excellent Vision",
                                      "Fleet Footed", "Hardy", "Lightning Reflexes", "Luck", "Marksman",
                                      "Mimic", "Resistance to Disease", "Resistance to Magic",
                                      "Resistance to Poison", "Savvy", "Sixth Sense", "Strong-Minded", "Sturdy",
                                      "Suave", "Super Numerate", "Very Resilient", "Very Strong", "Warrior Born"],
                                     [5, 5, 5, 5, 5, 4, 4, 5, 4, 5, 4, 2, 4, 5, 5, 5, 5, 5, 5, 4, 4, 5]))
        # Main Stats
        for x in range(8):
            if x == 1 or x == 4 or x == 7:
                self.stats[0][x] += 30
            elif x == 0 or x == 2 or x == 3:
                self.stats[0][x] += 10
            else:
                self.stats[0][x] += 20

        # Secondary Stats
        sec = []
        # Attacks
        sec.append(1)
        # Wounds
        sec.append(roulette([8, 9, 10, 11], [3, 3, 3, 1]))
        # SB & TB
        sec.append(self.stats[0][2] // 10)
        sec.append(self.stats[0][3] // 10)
        # M, Mag, IP
        sec.extend([4, 0, 0])
        # FP
        sec.append(roulette([2, 3], [7, 3]))
        self.stats.append(sec)

        # Height
        if self.sex == "M":
            potato = 40 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"
        else:
            potato = 38 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"

        # Weight
        self.weight = roulette(
            [75, 75, 80, 80, 85, 85, 90, 90, 95, 100, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145],
            [1, 2, 2, 3, 4, 5, 5, 7, 8, 12, 15, 7, 7, 5, 5, 4, 3, 2, 2, 1])

        # HairColor
        self.hairColor = random.choice(["Ash Blonde", "Corn", "Yellow", "Yellow", "Red", "Copper", "Light Brown",
                                        "Brown", "Dark Brown", "Black"])

        # Eye Color
        self.eyeColor = random.choice(["Blue", "Hazel", "Hazel", "Light Brown", "Light Brown", "Brown", "Brown",
                                       "Dark Brown", "Dark Brown", "Dark Brown"])

        # Siblings
        self.siblings = roulette([1, 2, 3, 4, 5, 6], [1, 2, 2, 2, 2, 1])

        # Age
        age = []
        for x in range(20):
            age.append(20 + (x * 2))
        self.age = random.choice(age)

        # Birthplace
        self.birthPlace = random.choice(["Human", "The Moot"])
        if self.birthPlace == "Human":
            self.birthPlace = genHumanBirthplace()

    # TODO: Human Careers and Names
    def genHuman(self):
        self.skills.extend(["Common Knowledge(The Empire)", "Gossip", "Speak Language(Reikspiel)"])
        a = genHumanRandomTalent()
        b = genHumanRandomTalent()
        while b == a:
            b = genHumanRandomTalent()
        self.talents.extend([a, b])

        # Main Stats
        for x in range(8):
            self.stats[0][x] += 20

        # Secondary Stats
        sec = []
        # Attacks
        sec.append(1)
        # Wounds
        sec.append(roulette([10, 11, 12, 13], [3, 3, 3, 1]))
        # SB & TB
        sec.append(self.stats[0][2] // 10)
        sec.append(self.stats[0][3] // 10)
        # M, Mag, IP
        sec.extend([4, 0, 0])
        # FP
        sec.append(roulette([2, 3], [4, 6]))
        self.stats.append(sec)

        # Height
        if self.sex == "M":
            potato = 64 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"
        else:
            potato = 61 + d10()
            self.height = str(potato // 12) + "'" + str(potato % 12) + "''"

        # Weight
        lbs = []
        for x in range(20):
            lbs.append(105 + (x * 5))
        self.weight = roulette(lbs, [1, 2, 2, 3, 4, 5, 5, 7, 8, 12, 15, 7, 7, 5, 5, 4, 3, 2, 2, 1])

        # HairColor
        self.hairColor = random.choice(["Ash Blonde", "Corn", "Yellow", "Red", "Copper", "Light Brown",
                                        "Brown", "Brown", "Dark Brown", "Black"])

        # Eye Color
        self.eyeColor = random.choice(["Pale Grey", "Grey Blue", "Blue", "Green", "Copper", "Light Brown", "Brown",
                                      "Dark Brown", "Purple", "Black"])

        # Siblings
        self.siblings = roulette([0, 1, 2, 3, 4, 5], [1, 2, 2, 2, 2, 1])

        # Age
        age = []
        for x in range(20):
            age.append(16 + x)
        self.age = random.choice(age)

        # Birthplace
        self.birthPlace = genHumanBirthplace()

    def genCharacter(self):
        # The only non-Racial stuff
        self.starSign = genStarSign()
        self.distMarks = genDistinguisingMark()
        #Random Sexing
        self.sex = random.choice(["M", "F"])

        # The Racial Stuff
        race = ["Dwarf", "Elf", "Halfling", "Human"]
        self.race = random.choice(race)
        if self.race == "Dwarf":
            self.genDwarf()
        elif self.race == "Elf":
            self.genElf()
        elif self.race == "Halfling":
            self.genHalfling()
        elif self.race == "Human":
            self.genHuman()

    def printChar(self):
        print(self.sex, " ", self.race, " ", self.career, '\n')
        a = ["WS", "BS", "S", "T", "Ag", "Int", "WP", "Fel"]
        for x in range(8):
            print(a[x], ":", self.stats[0][x])
        a = ["A", "W", "SB", "TB", "M", "Mag",  "IP", "FP"]
        for x in range(8):
            print(a[x], ":", self.stats[1][x])
        print('\n',"Skills",'\n')
        for x in self.skills:
            print(x, " ")
        print('\n',"Talents",'\n')
        for x in self.talents:
            print(x," ")
        print()

def main():
    for x in range(100):
        #if a == "":
            #test.genCharacter()
        #else:
            #test.genCharacter(a)
        test = wFRPChar()
        test.genCharacter()
        test.printChar()


if __name__ == "__main__":
    main()
