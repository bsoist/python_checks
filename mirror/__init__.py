import check50

@check50.check()
def exists():
    """File mirror.py exists"""
    check50.exists("mirror.py")

# test(mirror("good") == "gooddoog")
@check50.check()
def good():
    """Prints gooddoog for good"""
    check50.run("python3 mirror.py"
    ).stdout('Word? '
    ).stdin("good", prompt=True
    ).stdout("gooddoog", regex=False
    ).exit()

#test(mirror("Python") == "PythonnohtyP")
@check50.check()
def python():
    """Prints PythonnohtyP for Python"""
    check50.run("python3 mirror.py"
    ).stdout('Word? '
    ).stdin("Python", prompt=True
    ).stdout("PythonnohtyP", regex=False
    ).exit()

#test(mirror("") == "")
@check50.check()
def empty():
    """Prints empty string for empty string""" 
    check50.run("python3 mirror.py"
    ).stdout('Word? '
    ).stdin("", prompt=True
    ).stdout("", regex=False
    ).exit()

#test(mirror("a") == "aa")
@check50.check()
def single():
    """Handles a single char string"""
    check50.run("python3 mirror.py"
    ).stdout('Word? '
    ).stdin("a", prompt=True
    ).stdout("aa", regex=False
    ).exit()
