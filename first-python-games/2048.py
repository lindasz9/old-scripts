import random

def start():
    print("w : up")
    print("s : down")
    print("a : left")
    print("d : right")
    print()
    game()

def game():
    global swaps
    two_or_four()
    printing_rows()
    is_game_over()
    while True:
        move = input("- ")
        if move == "s":
            down()
            break
        elif move == "a":
            left()
            break
        elif move == "d":
            right()
            break
        elif move == "w":
            up()
            break
        else:
            continue
    swaps += 1
    game()

def two_or_four():
    random_row = random.choice(rows)
    random_column = random.randint(1, 4) - 1
    while random_row[random_column] != 0:
        random_row = random.choice(rows)
        random_column = random.randint(1, 4) - 1
    options = [2, 4]
    new_number = random.choices(options, weights=(9, 1), k=1)
    random_row[random_column] = new_number[0]

def printing_rows():
    for first in first_row:
        print(first, end=" ")
    print()
    for second in second_row:
        print(second, end=" ")
    print()
    for third in third_row:
        print(third, end=" ")
    print()
    for fourth in fourth_row:
        print(fourth, end=" ")
    print()
    print()

def right():
    for i in range(4):
        right_row = rows[i]
        right_order.clear()
        for a in right_row:
            if a != 0:
                right_order.append(a)
        if len(right_order) > 1:
            times_to_check = len(right_order) - 1
            change = 0
            for b in range(times_to_check):
                b += 1
                if b + change > times_to_check + 1:
                    break
                if right_order[-b] == right_order[-b-1]:
                    double = right_order[-b] * 2
                    right_order[-b] = 3
                    right_order[-b - 1] = 5
                    right_order.remove(3)
                    right_order.remove(5)
                    right_order.insert(times_to_check-change-b, double)
                    times_to_check -= 1
                    change += 1
        while len(right_order) != 4:
            right_order.insert(0,0)
        right_row.clear()
        for a in right_order:
            right_row.append(a)

def left():
    for i in range(4):
        left_row = rows[i]
        left_order.clear()
        for a in left_row:
            if a != 0:
                left_order.append(a)
        if len(left_order) > 1:
            times_to_check = len(left_order) - 1
            #global change
            change = 0
            for b in range(times_to_check):
                if b + change > times_to_check:
                    break
                if left_order[b] == left_order[b+1]:
                    double = left_order[b] * 2
                    left_order[b] = 3
                    left_order[b+1] = 5
                    left_order.remove(3)
                    left_order.remove(5)
                    left_order.insert(b,double)
                    times_to_check -= 1
                    change += 1
        while len(left_order) != 4:
            left_order.append(0)
        left_row.clear()
        for a in left_order:
            left_row.append(a)

def down():
    for i in range(4):
        down_column = columns[i]
        down_column.clear()
        down_column.append(first_row[i])
        down_column.append(second_row[i])
        down_column.append(third_row[i])
        down_column.append(fourth_row[i])
        down_order.clear()
        for a in down_column:
            if a != 0:
                down_order.append(a)
        if len(down_order) > 1:
            times_to_check = len(down_order) - 1
            change = 0
            for b in range(times_to_check):
                b += 1
                if b + change > times_to_check + 1:
                    break
                if down_order[-b] == down_order[-b-1]:
                    double = down_order[-b] * 2
                    down_order[-b] = 3
                    down_order[-b - 1] = 5
                    down_order.remove(3)
                    down_order.remove(5)
                    down_order.insert(times_to_check-change-b, double)
                    times_to_check -= 1
                    change += 1
        while len(down_order) != 4:
            down_order.insert(0,0)
        down_column.clear()
        for a in down_order:
            down_column.append(a)
        down_ordered_columns.append(down_column)
    first_row.clear()
    second_row.clear()
    third_row.clear()
    fourth_row.clear()
    for i in down_ordered_columns:
        first_row.append(i[0])
        second_row.append(i[1])
        third_row.append(i[2])
        fourth_row.append(i[3])
    down_ordered_columns.clear()

def up():
    for i in range(4):
        up_column = columns[i]
        up_column.clear()
        up_column.append(first_row[i])
        up_column.append(second_row[i])
        up_column.append(third_row[i])
        up_column.append(fourth_row[i])
        up_order.clear()
        for a in up_column:
            if a != 0:
                up_order.append(a)
        if len(up_order) > 1:
            times_to_check = len(up_order) - 1
            change = 0
            for b in range(times_to_check):
                if b + change > times_to_check:
                    break
                if up_order[b] == up_order[b+1]:
                    double = up_order[b] * 2
                    up_order[b] = 3
                    up_order[b+1] = 5
                    up_order.remove(3)
                    up_order.remove(5)
                    up_order.insert(b,double)
                    times_to_check -= 1
                    change += 1
        while len(up_order) != 4:
            up_order.append(0)
        up_column.clear()
        for a in up_order:
            up_column.append(a)
        up_ordered_columns.append(up_column)
    first_row.clear()
    second_row.clear()
    third_row.clear()
    fourth_row.clear()
    for i in up_ordered_columns:
        first_row.append(i[0])
        second_row.append(i[1])
        third_row.append(i[2])
        fourth_row.append(i[3])
    up_ordered_columns.clear()
        
def is_game_over():
    global trues
    zeros.clear()
    for i in rows:
        for j in i:
            if j == 0:
                zeros.append(j)
    if len(zeros) == 0:
        trues = 0
        check_rows()
        check_columns()
        if trues == 2:
            game_over()

def check_rows():
    global trues
    not_equal = 0
    for i in rows:
        for j in range(3):
            if i[j] != i[j+1]:
                not_equal += 1
    if not_equal == 12:
        trues += 1

def check_columns():
    global trues
    can_move = False
    for i in range(4):
        check_column = [first_row[i], second_row[i], third_row[i], fourth_row[i]]
        for j in range(3):
            if check_column[j] == check_column[j+1]:
                can_move = True
    if not can_move:
        trues += 1

def game_over():
    global record
    sum_of_numbers = 0
    for i in rows:
        for j in i:
            sum_of_numbers += j
    if sum_of_numbers > record:
        record = sum_of_numbers
    print()
    print("GAME OVER")
    print("--------------------------")
    print(f"swaps: {swaps}")
    print(f"score: {sum_of_numbers}")
    print(f"record: {record}")
    print("--------------------------")
    play_again()

def play_again():
    global swaps
    again = input("Do you want to play again (yes/no) ? ").lower()
    if again != "yes":
        print("Thanks for playing")
        exit()
    for i in rows:
        i.clear()
        for j in range(4):
            i.append(0)
    swaps = 0
    print()
    two_or_four()
    game()

first_row = [0, 0, 0, 0]
second_row = [0, 0, 0, 0]
third_row = [0, 0, 0, 0]
fourth_row = [0, 0, 0, 0]
rows = [first_row, second_row, third_row, fourth_row]
first_column = []
second_column = []
third_column = []
fourth_column = []
columns = [first_column, second_column, third_column, fourth_column]
right_order = []
left_order = []
down_order = []
down_ordered_columns = []
up_order = []
up_ordered_columns = []
zeros = []
swaps = 0
record = 0
trues = 0

two_or_four()
start()