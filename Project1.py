import random
import sys

def get_key_from_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None

print("STONE-PAPER-SCISSOR")


choose = input("Enter your choice : ")
cha = choose.lower()


a={
    'stone':'s',
    'paper':'p',
    'scissor':'k'
}

if cha in a:
    ch = cha
else:
    print("Kindly choose only from stone , paper and scissor")
    sys.exit(0)

choices = ['s','p','k']
comp = random.choice(choices)


print(f"You choosed : {ch}")
print(f"Computer choosed : {get_key_from_value(a, comp)}")

user_input = a[ch]

if (user_input == comp):
    print("its a draw")
elif(user_input == 's'):
    if (comp =='p'):
        print("You Lost")
    else:
        print("You Won")
elif(user_input == 'p'):
    if (comp == 's'):
        print("You Won")
    else:
        print('You Lost')
elif(user_input == 'k'):
    if (comp == 'p'):
        print("You Won")
    else:
        print('You Lost')
