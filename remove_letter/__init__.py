import check50

@check50.check()
def exists():
    """File remove_letter.py exists"""
    check50.exists("remove_letter.py")

#remove_letter("a", "apple") == "pple"
@check50.check()
def Removes_a_from_apple():
    """Removes a from apple"""
    check50.run("python3 remove_letter.py"
        ).stdin("apple", prompt=True
        ).stdin("a", prompt=True
        ).stdout("pple", regex=False
        ).exit()

#remove_letter("a", "banana") == "bnn"
@check50.check()
def Removes_a_from_banana():
    """Removes a from banana"""
    check50.run("python3 remove_letter.py"
        ).stdin("banana", prompt=True
        ).stdin("a", prompt=True
        ).stdout("bnn", regex=False
        ).exit()

#remove_letter("z", "banana") == "banana"
@check50.check()
def Prints_banana_when_removing_z_from_banana():
    """Prints banana when removing z from banana"""
    check50.run("python3 remove_letter.py"
        ).stdin("banana", prompt=True
        ).stdin("z", prompt=True
        ).stdout("banana", regex=False
        ).exit()

#remove_letter("i", "Mississippi") == "Msssspp"
@check50.check()
def Removes_i_from_Mississippi():
    """Removes i from Mississippi"""
    check50.run("python3 remove_letter.py"
        ).stdin("Mississippi", prompt=True
        ).stdin("i", prompt=True
        ).stdout("Msssspp", regex=False
        ).exit()

#remove_letter("b", "") = ""
@check50.check()
def Prints_empty_string_when_trying_to_remove_b():
    """Prints empty string when trying to remove b"""
    check50.run("python3 remove_letter.py"
        ).stdin("None", prompt=True
        ).stdin("b", prompt=True
        ).stdout("None", regex=False
        ).exit()

#remove_letter("b", "c") = "c"
@check50.check()
def Prints_single_letter_string_when_trying_to_remove_non_existent_char():
    """Prints single letter string when trying to remove non-existent char"""
    check50.run("python3 remove_letter.py"
        ).stdin("c", prompt=True
        ).stdin("b", prompt=True
        ).stdout("c", regex=False
        ).exit()