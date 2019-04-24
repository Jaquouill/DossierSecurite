import sys
import time


def bruteforcefaible():
    temps = time.time()
    l1 = chr(96)
    l2 = chr(96)
    l3 = chr(96)
    l4 = chr(96)
    l5 = chr(96)
    passw = sys.argv[2]
    c1 = 1
    c2 = 1
    c3 = 1
    c4 = 1
    c5 = 1
    while c1 < 26:
        l1 = 96+c1
        c1 += 1
        while c2 < 26:
            l2 = 96 + c1
            c2 += 1
            while c3 < 26:
                l3 = 96 + c1
                c3 += 1
                while c4 < 26:
                    l4 = 96 + c1
                    c4 += 1
                    while c5 < 26:
                        l5 = 96 + c1
                        c5 += 1
                        if str(l1+l2+l3+l4+l5) == passw:
                            totaltemps = time.time() - temps
                            print(totaltemps)


def bruteforcemediumsaignant():
    temps = time.time()
    l1 = chr(96)
    l2 = chr(96)
    l3 = chr(96)
    l4 = chr(96)
    l5 = chr(96)
    passw = sys.argv[2]
    c1 = 1
    c2 = 1
    c3 = 1
    c4 = 1
    c5 = 1
    while c1 < 52:
        if c1 <= 26:
            l1 = 96+c1
            c1 += 1
        if c1 >= 27:
            c11 = 1
            l1 = 64 + c11
            c1 += 1
            c11 += 1
        while c2 < 52:
            if c2 <= 26:
                l2 = 96 + c2
                c2 += 1
            if c2 >= 27:
                c22 = 1
                l2 = 64 + c22
                c2 += 1
                c22 += 1
            while c3 < 52:
                if c3 <= 26:
                    l3 = 96 + c3
                    c3 += 1
                if c3 >= 27:
                    c33 = 1
                    l3 = 64 + c33
                    c3 += 1
                    c3 += 1
                while c4 < 52:
                    if c4 <= 26:
                        l4 = 96 + c4
                        c4 += 1
                    if c4 >= 27:
                        c44 = 1
                        l4 = 64 + c44
                        c4 += 1
                        c44 += 1
                    while c5 < 52:
                        if c5 <= 26:
                            l5 = 96 + c5
                            c5 += 1
                        if c5 >= 27:
                            c55 = 1
                            l5 = 64 + c55
                            c5 += 1
                            c55 += 1
                        if str(l1+l2+l3+l4+l5) == passw:
                            totaltemps = time.time() - temps
                            print(totaltemps)


def bruteforcefort():
    temps = time.time()
    l1 = chr(96)
    l2 = chr(96)
    l3 = chr(96)
    l4 = chr(96)
    l5 = chr(96)
    passw = sys.argv[2]
    c1 = 1
    c2 = 1
    c3 = 1
    c4 = 1
    c5 = 1
    while c1 < 62:
        if c1 <= 26:
            l1 = 96+c1
            c1 += 1
        if c1 >= 27 & c1 <= 52:
            c11 = 1
            l1 = 64 + c11
            c1 += 1
            c11 += 1
        if c1 > 52 & c1 <= 62:
            c11 = 1
            l1 = 47 + c11
            c1 += 1
            c11 += 1
        while c2 < 62:
            if c2 <= 26:
                l2 = 96 + c2
                c2 += 1
            if c2 >= 27 & c2 <= 52:
                c22 = 1
                l2 = 64 + c22
                c2 += 1
                c22 += 1
            if c2 > 52 & c2 <= 62:
                c22 = 1
                l2 = 47 + c22
                c2 += 1
                c22 += 1
            while c3 < 62:
                if c3 <= 26:
                    l3 = 96 + c3
                    c3 += 1
                if c3 >= 27 & c3 <= 52:
                    c33 = 1
                    l3 = 64 + c33
                    c3 += 1
                    c33 += 1
                if c3 > 52 & c3 <= 62:
                    c33 = 1
                    l3 = 47 + c33
                    c3 += 1
                    c33 += 1
                while c4 < 62:
                    if c4 <= 26:
                        l4 = 96 + c4
                        c4 += 1
                    if c4 >= 27 & c4 <= 52:
                        c44 = 1
                        l4 = 64 + c44
                        c4 += 1
                        c44 += 1
                    if c4 > 52 & c4 <= 62:
                        c44 = 1
                        l4 = 47 + c44
                        c4 += 1
                        c44 += 1
                    while c5 < 62:
                        if c5 <= 26:
                            l5 = 96 + c5
                            c5 += 1
                        if c5 >= 27 & c5 <= 52:
                            c55 = 1
                            l5 = 64 + c55
                            c5 += 1
                            c55 += 1
                        if c5 > 52 & c5 <= 62:
                            c55 = 1
                            l5 = 47 + c55
                            c5 += 1
                            c55 += 1
                        if str(l1+l2+l3+l4+l5) == passw:
                            totaltemps = time.time() - temps
                            print(totaltemps)


if sys.argv[1] == "faible":
    bruteforcefaible()
    print(sys.argv[2])
if sys.argv[1] == "moyen":
    bruteforcemediumsaignant()
    print(sys.argv[2])
if sys.argv[1] == "fort":
    bruteforcefort()
    print(sys.argv[2])
