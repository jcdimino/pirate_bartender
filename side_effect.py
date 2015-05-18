def side_effect_test(int):
    # Do something to modify the value
    int[1] = 1
    print "Inside the function, the value becomes {}".format(int)

if __name__ == "__main__":
    # Create the value
    int = [3, 5, 66]

    print "Outside the function, the value starts as {}".format(int)

    side_effect_test(int)

    print "Outside the function, the value is now {}".format(int)