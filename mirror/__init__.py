import check50

@check50.check()
def exists():
    """File mirror.py exists"""
    check50.exists("mirror.py")

# test(mirror("good") == "gooddoog")
@check50.check()
def good():
    check50.run("python3 mirror.py"
    ).stdin("good", prompt=False
    ).stdout("gooddoog", regex=False
    ).exit()

#test(mirror("Python") == "PythonnohtyP")
@check50.check()
def python():
    check50.run("python3 mirror.py"
    ).stdin("Python", prompt=False
    ).stdout("PythonnohtyP", regex=False
    ).exit()

#test(mirror("") == "")
@check50.check()
def empty():
    check50.run("python3 mirror.py"
    ).stdout('Word? '
    ).stdin("", prompt=True
    ).stdout("", regex=False
    ).exit()

#test(mirror("a") == "aa")
@check50.check()
def single():
    check50.run("python3 mirror.py"
    ).stdin("a", prompt=False
    ).stdout("aa", regex=False
    ).exit()