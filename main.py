# ============================= #
#    HIBISCUS ENCRYPTION TOOL   #
#       Made by ivey#6760       #
# ============================= #
import sys

from string import ascii_letters
from random import randint
import time
from os import system,name
# ============================= #
def clearcmd():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# ============================= #

# ============================= #
placeholder = " "
numberlist = ["1","2","3"]
unencrypted = "PLACEHOLDER"
encrypted = "PLACEHOLDER"
# ============================= #
clearcmd()
a1 = ",--.  ,--.,--.,--.   ,--.                             "
a2 = "|  '--'  |`--'|  |-. `--' ,---.  ,---.,--.,--. ,---.  "
a3 = "|  .--.  |,--.| .-. ',--.(  .-' | .--'|  ||  |(  .-'  "
a4 = "|  |  |  ||  || `-' ||  |.-'  `)\ `--.'  ''  '.-'  `) "
a5= "`--'  `--'`--' `---' `--'`----'  `---' `----' `----'  "
a6 = "                  Made by ivey#6760                   "
print(a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6)
print(placeholder)
print("──────────────────────────────────────────────────────")
print(placeholder)
print("1. Hibiscus Text Encryption")
print("2. Hibiscus Text Decryption")
print("3. Random Text Generator")
print(placeholder)
print("──────────────────────────────────────────────────────")
print(placeholder)
choiceinlist = input("Option > ")
print(placeholder)
print("──────────────────────────────────────────────────────")

if choiceinlist in numberlist:
    if choiceinlist == "1":
        print("Choice 1 Selected, initializing...")
        time.sleep(3)
        clearcmd()
        print(a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6)
        print(placeholder)
        print("──────────────────────────────────────────────────────")
        print(placeholder)
        print("Encryption Menu")
        print(placeholder)
        print("──────────────────────────────────────────────────────")
        print(placeholder)
        unencrypted = str(input("(HIBISCUS): Input String: "))
        print(placeholder)
        print("──────────────────────────────────────────────────────")
        print(placeholder)
        # LETTER ENCRYPTION PHASE (DONE)
        s1 = unencrypted.replace("a","✿")
        s2 = s1.replace("b", "❀")
        s3 = s2.replace("c", "❁")
        s4 = s3.replace("d", "✾")
        s5 = s4.replace("e", "✪")
        s6 = s5.replace("f", "♥")
        s7 = s6.replace("g", "❄")
        s8 = s7.replace("h", "☮")
        s9 = s8.replace("i", "☺")
        s10 = s9.replace("j", "∞")
        s11 = s10.replace("k", "⌀")
        s12 = s11.replace("l", "⍟")
        s13 = s12.replace("m", "◎")
        s14 = s13.replace("n", "꙰")
        s15 = s14.replace("o", "≛")
        s16 = s15.replace("p", "✳")
        s17 = s16.replace("q", "✯")
        s18 = s17.replace("r", "✡")
        s19 = s18.replace("s", "↺")
        s20 = s19.replace("t", "♣")
        s21 = s20.replace("u", "✦")
        s22 = s21.replace("v", "♩")
        s23 = s22.replace("w", "♛")
        s24 = s23.replace("x", "➳")
        s25 = s24.replace("y", "☾")
        s26 = s25.replace("z", "↜")
        s27 = s26.replace(" ", "hibis")
        # REPEAT ENCRYPTION PHASE (DONE)
        m1 = s27.replace("✪✪","✉")
        m2 = m1.replace("≛≛", "☀")
        m3 = m2.replace("⍟⍟", "☄")
        m4 = m3.replace("♣♣", "☣")
        m5 = m4.replace("↺↺", "⊹")
        m6 = m5.replace("♥♥", "⊶")
        # DIGRAPH ENCRYPTION PHASE (DONE)
        d1 = m5.replace("✡✿","@")
        d2 = d1.replace("✪✡", "|")
        d3 = d2.replace("♥❀", "`")
        d4 = d3.replace("≛✡", "(")
        d5 = d4.replace("◎❀", "#")
        d6 = d5.replace("☾✪", "<")
        # PRINT END STRING
        print("Encrypted String: "+d5)
        time.sleep(10)
        exit()

    elif choiceinlist == "2":
        print("Choice 2 Selected, initializing...")
        time.sleep(3)
        clearcmd()
        print(a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6)
        print(placeholder)
        print("──────────────────────────────────────────────────────")
        print(placeholder)
        encrypted = str(input("(HIBISCUS): Input String: "))
        # DIGRAPH DECRYPTION PHASE (DONE)
        d1 = encrypted.replace("@", "✡✿")
        d2 = d1.replace("|", "✪✡")
        d3 = d2.replace("`", "♥❀")
        d4 = d3.replace("(", "≛✡")
        d5 = d4.replace("#", "◎❀")
        d6 = d5.replace("<", "☾✪")
        # REPEAT DECRYPTION PHASE (DONE)
        m1 = d5.replace("✉", "✪✪")
        m2 = m1.replace("☀", "≛≛")
        m3 = m2.replace("☄", "⍟⍟")
        m4 = m3.replace("☣", "♣♣")
        m5 = m4.replace("⊹", "↺↺")
        m6 = m5.replace("⊶", "♥♥")
        # LETTER DECRYPTION PHASE
        s0 = m5.replace("hibis", " ")
        s1 = s0.replace("✿", "a")
        s2 = s1.replace("❀", "b")
        s3 = s2.replace("❁", "c")
        s4 = s3.replace("✾", "d")
        s5 = s4.replace("✪", "e")
        s6 = s5.replace("♥", "f")
        s7 = s6.replace("❄", "g")
        s8 = s7.replace("☮", "h")
        s9 = s8.replace("☺", "i")
        s10 = s9.replace("∞", "j")
        s11 = s10.replace("⌀", "k")
        s12 = s11.replace("⍟", "l")
        s13 = s12.replace("◎", "m")
        s14 = s13.replace("꙰", "n")
        s15 = s14.replace("≛", "o")
        s16 = s15.replace("✳", "p")
        s17 = s16.replace("✯", "q")
        s18 = s17.replace("✡", "r")
        s19 = s18.replace("↺", "s")
        s20 = s19.replace("♣", "t")
        s21 = s20.replace("✦", "u")
        s22 = s21.replace("♩", "v")
        s23 = s22.replace("♛", "w")
        s24 = s23.replace("➳", "x")
        s25 = s24.replace("☾", "y")
        s26 = s25.replace("↜", "z")
        # PRINT END STRING
        print("Decrypted String: "+s26)
        time.sleep(10)
        exit()

    elif choiceinlist == "3":
        print("Choice 3 Selected, initializing...")
        time.sleep(3)
        clearcmd()
        print(a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6)
        print(placeholder)
        print("──────────────────────────────────────────────────────")
        print(placeholder)
        print("UNFINISHED, RESTART PROGRAM")

else:
    print("Invalid Choice! Exiting...")
    exit()





