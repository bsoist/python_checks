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
        ).stdin("banana", prompt=True
        ).stdin("an", prompt=True
        ).stdout("bana", regex=False
        ).exit()

#remove("cyc", "bicycle") == "bile"
@check50.check()
def cyc_bicycle():
    """Removes cyc from bicycle"""
    check50.run("python3 remove.py"
        ).stdin("bicycle", prompt=True
        ).stdin("cyc", prompt=True
        ).stdout("bile", regex=False
        ).exit()

#remove("iss", "Mississippi") == "Missippi"
@check50.check()
def iss_missississippi():
    """Removes iss from Mississippi"""
    check50.run("python3 remove.py"
        ).stdin("Mississippi", prompt=True
        ).stdin("iss", prompt=True
        ).stdout("Missippi", regex=False
        ).exit()

test(remove("eggs", "bicycle") == "bicycle")
@check50.check()
def substring_not_exists():
    """Prints original word when substring not present"""
    check50.run("python3 remove.py"
        ).stdin("bicycle", prompt=True
        ).stdin("eggs", prompt=True
        ).stdout("bicycle", regex=False
        ).exit()
