def outer():
    print("Outer function")

    def innter():
        print("Inner function")

    innter()


outer()
