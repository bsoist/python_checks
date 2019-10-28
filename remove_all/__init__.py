import check50

@check50.check()
def exists():
    """File remove_all.py exists"""
    check50.exists("remove_all.py")

#remove_all("an", "banana") == "ba"
@check50.check()
def an_banana():
    """Removes an from banana"""
    check50.run("python3 remove_all.py"
        ).stdout("Word? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("an", prompt=False
        ).stdout("ba", regex=False
        ).exit()

#remove_all("cyc", "bicycle") == "bile"
@check50.check()
def cyc_bicycle():
    """Removes cyc from bicycle"""
    check50.run("python3 remove_all.py"
        ).stdout("Word? ", regex=False
        ).stdin("bicycle", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("cyc", prompt=False
        ).stdout("bile", regex=False
        ).exit()

#remove_all("iss", "Mississippi") == "Mippi"
@check50.check()
def iss_missississippi():
    """Removes iss from Mississippi"""
    check50.run("python3 remove_all.py"
        ).stdout("Word? ", regex=False
        ).stdin("Mississippi", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("iss", prompt=False
        ).stdout("Mippi", regex=False
        ).exit()

#remove_all("eggs", "bicycle") == "bicycle"
@check50.check()
def substring_not_exists():
    """Prints original word when substring not present"""
    check50.run("python3 remove_all.py"
        ).stdout("Word? ", regex=False
        ).stdin("bicycle", prompt=False
        ).stdout("Substring? ", regex=False
        ).stdin("eggs", prompt=False
        ).stdout("bicycle", regex=False
        ).exit()