import check50

@check50.check()
def exists():
    """File palindrome.py exists"""
    check50.exists("palindrome.py")

#is_palindrome("abba")
@check50.check()
def yes_word():
    """Print YES for abba"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("abba", prompt=False
        ).stdout("YES", regex=False
        ).exit()


#not is_palindrome("abab")
@check50.check()
def no_word():
    """Print NO for abab"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("abab", prompt=False
        ).stdout("NO", regex=False
        ).exit()


#is_palindrome("tenet")
@check50.check()
def yes_word():
    """Print YES for tenet"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("tenet", prompt=False
        ).stdout("YES", regex=False
        ).exit()


#not is_palindrome("banana")
@check50.check()
def no_word():
    """Print NO for banana"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("banana", prompt=False
        ).stdout("NO", regex=False
        ).exit()

#is_palindrome("straw warts")
@check50.check()
def yes_word():
    """Print YES for straw warts"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("straw warts", prompt=False
        ).stdout("YES", regex=False
        ).exit()

#is_palindrome("a")
@check50.check()
def yes_word():
    """Print YES for a"""
    check50.run("python3 palindrome.py"
        ).stdout("Word? ", regex=False
        ).stdin("a", prompt=False
        ).stdout("YES", regex=False
        ).exit()


