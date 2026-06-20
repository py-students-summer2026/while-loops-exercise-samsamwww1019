def get_starting_number():
    num = ""

    while not num.isnumeric() or int(num) < 1:
        num = input("How many bottles of beer on the wall? ")

    return int(num)


def sing(starting_number):
    bottles = starting_number
    keep_singing = True

    while keep_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False
        else:
            next_bottles = bottles - 1

            if next_bottles == 1:
                next_phrase = "1 bottle"
            else:
                next_phrase = str(next_bottles) + " bottles"

            print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
            print("Take one down, pass it around, " + next_phrase + " of beer on the wall.")
            print()

            bottles = bottles - 1