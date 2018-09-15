
def drawSpaceMan(i):
    if i != 6:
        if i >= 0:
            print("   .")
            print("   _")
            print("  ___")
            print(" _____")
        if i >= 1:
            print("|  o  | ")
        if i >= 2:
            print("| \|/ | ")
        if i >= 3:
            print("|  |  | ")
        if i >= 4:
            print("| / \ | ")
        if i >= 5:
            print(" _____  ")
    else:
        print("   .")
        print("   _")
        print("  ___")
        print(" _____")
        print("|  o  |  ")
        print("| \|/ |")
        print("|  |  |")
        print("| / \ |")
        print(" _____ ")
        print(" ^^^^^")
        print("/ \ / \ ")
