def treasure_map() :
    row1 = ["◻️", "◻️", "◻️"]
    row2 = ["◻️", "◻️", "◻️"]
    row3 = ["◻️", "◻️", "◻️"]

    map = [ row1, row2, row3]

    print("     1    2    3")
    print(f"1 {row1}\n2 {row2}\n3 {row3}")
    position = input("Where do you want to put the treasure?\n")
    position_num = position.split(', ')

    if (int(position_num[0]) > 3 or int(position_num[1]) > 3 ) :
        print("The numbers you have entered is out of the treasure map scope.\n")
    else :
        map[int(position_num[1])-1][int(position_num[0])-1] = '🟥'

        print("     1    2    3")
        print(f"1 {row1}\n2 {row2}\n3 {row3}")