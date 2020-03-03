import notebook


def testing():
    """Class Note testing"""

    # attribute testing
    print("-----------------\nattribute testing\n-----------------")
    test_note = notebook.Note("My notebook", "test")
    print(test_note.memo)
    print(test_note.tags)
    print(test_note.__getattribute__)
    print(type(test_note.memo))

    # object testing
    print("--------------\nobject testing\n--------------")
    test_note = notebook.Note
    print(test_note.__doc__)
    print(isinstance(test_note, object))
    print(type(test_note))
    print(dir(test_note))

    # __init__ method
    print("---------------\n__init__ method\n---------------")
    test_note = notebook.Note("My notebook", "test")
    print(test_note.__init__)
    print(test_note)

    # class methods testing
    print("-------------\nclass methods\n-------------")
    test_note = notebook.Note("My notebook", "test")
    print(test_note.match)
    print(test_note.match("test"))
    print(test_note.match("false_test"))
    print(type(test_note.match("test")))

if __name__ == "__main__":
    testing()
