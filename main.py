import random

MAX_LINES=5 #CHANGING THIS WILL CHANGE THE NO OF SLOT LINES THROUGHOUT THE CODE
MAX_BET=100
MIN_BET=1

ROWS=3
COLUMNS=3

symbol_count={"A":2,"B":4,"C":6,"D":8}
symbol_value_multiplier={"A":5,"B":4,"C":3,"D":2}

#GENERATE SLOT MACHINE
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):  #this means loop that statement as many times as needed without generating a variable.
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols =all_symbols[:]  #sliced since a copy of all_symbol is needed..any update to it may cause value change here
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

#PRINT THE SLOT MACHINE
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):         #enumerate gives index of column(here) as well as the item
            if i!= len(columns) -1:         #done to see if its last index of column
                print(column[row], end="|")     #end tells what the line ends with,default is new line
            else:
                print(column[row],end="")
        print()


#TAKE DEPOSITE FROM USER
def deposit():
    while True:
        amount=input("What would you like to deposit?")
        if amount.isdigit():                #no int() cause it throws error and does not let the prog continue
            amount=int(amount)
            if amount>0:
                break
            else:
                print("AMOUNT MUST BE GREATER THAN 0")
        else:
            print("PLEASE ENTER A NUMBER.")
    return amount

#GET NUMBER OF LINES USER WANTS TO BET ON
def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():                
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("ENTER VALID NUMBER OF LINES")
        else:
            print("PLEASE ENTER A NUMBER.")
    return lines

#GET BET BY THE USER
def get_bet():
    while True:
        amount=input("What would you like to bet on each line?")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"AMOUNT MUST BE{MIN_BET} - {MAX_BET}.")  #another way to put variable value in print statement
        else:
            print("PLEASE ENTER A NUMBER.")
    return amount

#CHECING THE WINNINGS
def check_winnings(columns,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol !=symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winnings_lines.append(line +1)

    return winnings,winnings_lines

#LOOPING THE GAME
def spin(balance):
    
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet =bet * lines
        if total_bet > balance:
            print(f"YOU DO NOT HAVE ENOUGH TO BET THAT AMOUNT,YOUR CURRENT BALANCE IS: {balance}.")
        else:
            break
    print(f"YOU ARE BETTING {bet} on {lines} lines. TOTAL BET IS : {total_bet}.")

    slots=get_slot_machine_spin(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winnings(slots,lines,bet,symbol_value_multiplier)
    print(f"YOU WON {winnings}.")
    print(f"YOU WON ON LINES: ", *winnings_lines) #* means all the lines will be printed that the user won on
    return winnings - total_bet


def main():
    balance=deposit()
    while True:
        print(f"CURRENT BALANCE IS {balance}")
        answer =input("PRESS ENTER TO PLAY OR Q TO QUIT.")
        if answer =="q":
            break
        balance += spin(balance)

    print(f"YOU ARE LEFT WITH {balance}")

    

main()