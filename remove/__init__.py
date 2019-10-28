import check50

@check50.check()
def exists():
    """File remove.py exists"""
    check50.exists("remove.py")

#remove("an", "banana") == "bana"
@check50.check()
def an_banana():
    """Removes an from banana"""
    check50.run("python3 remove.py"
        ).stdout("Word? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("an", prompt=False
        ).stdout("bana", regex=False
        ).exit()

#remove("cyc", "bicycle") == "bile"
@check50.check()
def cyc_bicycle():
    """Removes cyc from bicycle"""
    check50.run("python3 remove.py"
        ).stdout("Word? ", regex=False
        ).stdin("bicycle", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("cyc", prompt=False
        ).stdout("bile", regex=False
        ).exit()

#remove("iss", "Mississippi") == "Missippi"
@check50.check()
def iss_missississippi():
    """Removes iss from Mississippi"""
    check50.run("python3 remove.py"
        ).stdout("Word? ", regex=False
        ).stdin("Mississippi", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("iss", prompt=False
        ).stdout("Missippi", regex=False
        ).exit()

test(remove("eggs", "bicycle") == "bicycle")
@check50.check()
def substring_not_exists():
    """Prints original word when substring not present"""
    check50.run("python3 remove.py"
        ).stdout("Word? ", regex=False
        ).stdin("bicycle", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("eggs", prompt=False
        ).stdout("bicycle", regex=False
        ).exit()
