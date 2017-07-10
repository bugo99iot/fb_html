import sys, os
from itertools import islice
from datetime import datetime

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


#delete first line
with open('messages_ida.txt') as fin, open('messages_ida_cut.txt', 'w') as fout:
    fn=fin.readlines()
    for i in range(1,file_len('messages_ida.txt')):
        fout.write(fn[i])
fin.close()

#split into odd and even lines
with open('messages_ida_cut.txt') as fin, open('odd.txt', 'w') as fout:
    for line in islice(fin, 0, None, 2):
        try:
            fout.write(line)
        except IndexError:
            continue

with open('messages_ida_cut.txt') as fin, open('even.txt', 'w') as fout:
    for line in islice(fin, 1, None, 2):
        try:
            fout.write(line)
        except IndexError:
            continue
fin.close()
fout.close()

#merge even and odd

with open('odd.txt') as fin2, open("even.txt") as fin1, open('messages_ida_final.txt', 'w') as fout:
    f1=fin1.readlines()
    f2=fin2.readlines()
    for i in range(2*file_len("odd.txt")):
        try:
            if i % 2 == 0:
             fout.write(f1[i/2])
            else:
                fout.write(f2[(i-1)/2])
        except IndexError:
            continue
fin1.close()
fin2.close()
fout.close()

os.remove('messages_ida_cut.txt')
os.remove('even.txt')
os.remove('odd.txt')


"""
#remove double data lines
start=datetime.now()
good_words = ["Ida Suninen", "1424892921@facebook","Hugo Bertello", "569847884@facebook"]

with open('messages_reversed_fixed.txt') as fin, open('messages_reversed_pure.txt', 'w') as fout:
    fn=fin.readlines()
    length = file_len("messages_reversed_fixed.txt")
    #you cannot increment an iterable in a for loop (faster)
    #use while loop (slower) or for + islice + next)
    #for the above, look: https://stackoverflow.com/questions/17837316/how-do-i-skip-a-few-iterations-in-a-for-loop
    i=0    
    while i < length:
        try:
            if i % 5000 == 0:
                print i, " steps completed out of ", length
            if any(goodw in fn[i] for goodw in good_words) and any(goodw in fn[i+1] for goodw in good_words) and any(goodw in fn[i+2] for goodw in good_words):
                fout.write(fn[i+2])
                i+=3
                continue
            if any(goodw in fn[i] for goodw in good_words) and any(goodw in fn[i+1] for goodw in good_words):
                fout.write(fn[i+1])
                i+=2
                continue
            else:
                fout.write(fn[i])
                i+=1
        except IndexError:
            i+=1
            continue


print
print "Time taken to amend double data lines: ", datetime.now()-start
print

os.remove('messages_reversed_fixed.txt')
"""
