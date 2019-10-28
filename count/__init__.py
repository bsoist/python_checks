import check50

@check50.check()
def exists():
    """File count.py exists"""
    check50.exists("count.py")

#count("is", "Mississippi") == 2
@check50.check()
def iss_missississippi():
    """Finds 2 is in Mississippi"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("Mississippi", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("is", prompt=False
        ).stdout("2", regex=False
        ).exit()

#count("an", "banana") == 2
@check50.check()
def an_banana():
    """Finds 2 an in banana"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("an", prompt=False
        ).stdout("2", regex=False
        ).exit()

#count("ana", "banana") == 2
@check50.check()
def ana_banana():
    """Finds 2 ana in banana"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("ana", prompt=False
        ).stdout("2", regex=False
        ).exit()

#count("nana", "banana") == 1
@check50.check()
def nana_banana():
    """Finds 1 nana in banana"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("nana", prompt=False
        ).stdout("1", regex=False
        ).exit()



#count("nanan", "banana") == 0
@check50.check()
def nanan_banana():
    """Finds 0 nanan in banana"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("nanan", prompt=False
        ).stdout("0", regex=False
        ).exit()


#count("aaa", "aaaaaa") == 4
@check50.check()
def aaa_banana():
    """Finds 0 aaa in banana"""
    check50.run("python3 count.py"
        ).stdout("Phrase? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("aaa", prompt=False
        ).stdout("0", regex=False
        ).exit()
