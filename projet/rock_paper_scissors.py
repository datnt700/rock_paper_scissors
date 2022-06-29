import random


def jeu():
    user = input()
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's tie"
    if qui_gagne(user, computer):
        return "User est gagne"
    return "User est Perdu"


def qui_gagne(p, o):
    if p == "r" and o == "p" or p == "p" and o == "s" or p == "s" and o == "r":
        return True


print(jeu())
print()
# helo chu bo doi cu ho
def jeu():
    user = input()
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's tie"
    if qui_gagne(user, computer):
        return "User est gagne"
    return "User est Perdu"


def qui_gagne(p, o):
    if p == "r" and o == "p" or p == "p" and o == "s" or p == "s" and o == "r":
        return True


print(jeu())
print()
