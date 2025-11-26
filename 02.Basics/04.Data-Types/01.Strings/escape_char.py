# -----------------------------------------
# SECTION: ESCAPE CHARACTERS IN PYTHON STRINGS
# -----------------------------------------

def escape_characters_demo():
    print("=== Escape Characters Demo ===")

    # Newline
    print("Newline:\\nLine2 ->")
    print("Hello\nWorld")

    # Tab
    print("\nTab:\\t ->")
    print("Name:\tPython")

    # Backslash
    print("\nBackslash: \\\\ ->")
    print("This is a backslash: \\")

    # Single quote inside single quoted string
    print("\nSingle quote: \\' ->")
    print('It\'s a sunny day')


    # Double quote inside double quoted string
    print("\nDouble quote: \\\" ->")
    print("He said: \"Python is awesome!\"")

    # Bell sound (may not work everywhere)
    print("\nBell sound (\\a):")
    print("Beep!\a")

    # Carriage return
    print("\nCarriage return (\\r):")
    print("Hello World\rCR")

    # Backspace
    print("\nBackspace (\\b):")
    print("Python\b3")

    # Form feed
    print("\nForm feed (\\f):")
    print("Hello\fWorld")

    # Unicode characters
    print("\nUnicode examples:")
    print("Heart: \\u2764 ->", "\u2764")
    print("Smiley: \\U0001F600 ->", "\U0001F600")

    # Raw string (no escape processing)
    print("\nRaw strings:")
    print(r"Raw string example: C:\newfolder\test")
