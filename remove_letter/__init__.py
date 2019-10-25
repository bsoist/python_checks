import check50

@check50.check()
def Removes_a_from_apple():
    """Removes a from apple"""
    check50.run("python3 remove_letter.py").stdin("apple\na", prompt=False).stdout("pple", regex=False).exit()

@check50.check()
def Removes_a_from_banana():
    """Removes a from banana"""
    check50.run("python3 remove_letter.py").stdin("banana\na", prompt=False).stdout("bnn", regex=False).exit()

@check50.check()
def Prints_banana_when_removing_z_from_banana():
    """Prints banana when removing z from banana"""
    check50.run("python3 remove_letter.py").stdin("banana\nz", prompt=False).stdout("banana", regex=False).exit()

@check50.check()
def Removes_i_from_Mississippi():
    """Removes i from Mississippi"""
    check50.run("python3 remove_letter.py").stdin("Mississippi\ni", prompt=False).stdout("Msssspp", regex=False).exit()

@check50.check()
def Prints_empty_string_when_trying_to_remove_b():
    """Prints empty string when trying to remove b"""
    check50.run("python3 remove_letter.py").stdin("None\nb", prompt=False).stdout("None", regex=False).exit()

@check50.check()
def Prints_single_letter_string_when_trying_to_remove_non_existent_char():
    """Prints single letter string when trying to remove non-existent char"""
    check50.run("python3 remove_letter.py").stdin("c\nb", prompt=False).stdout("c", regex=False).exit()