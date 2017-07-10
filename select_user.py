import sys, os
from itertools import islice
from datetime import datetime


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#write file reversed
start=datetime.now()

with open('all_messages.txt') as fin,  open('messages_reversed_el.txt', 'w') as fout:
    fout.writelines(reversed(fin.readlines()))
fin.close()
fout.close()

print
print "Time taken to write the file reversed: ", datetime.now()-start
print


#remove all empty lines
start=datetime.now()

with open('messages_reversed_el.txt') as fin,  open('messages_reversed.txt', 'w') as fout:
    for line in fin:
        if line.isspace():
            continue
        else:
            fout.write(line)
fin.close()
fout.close()

os.remove('messages_reversed_el.txt')

print
print "Time taken to remove empty spaces: ", datetime.now()-start
print

#remove lines containing group conversation ids
start=datetime.now()

with open('messages_reversed.txt') as fin, open('messages_reversed_fixed.txt', 'w') as fout:
    for lines in fin:
        if lines.count("@facebook.com") >= 2:
            continue
        else:
            fout.write(lines)
fin.close()
fout.close()

os.remove('messages_reversed.txt')

print
print "Time taken to amend group conversation IDs: ", datetime.now()-start
print

#remove messages from bad years (OPTIONAL)
#if you would like to keep all years, rename "swapped_all_certain.txt" -> 'swapped_all.txt' in the next block and delete the current block
bad_years = ["2008 at", "2009 at", "2010 at", "2011 at", "2012 at", "2013 at", "2014 at", "2015 at", "2017 at"]
flag = False
with open('messages_reversed_fixed.txt') as fin, open('messages_reversed_pure.txt', 'w') as fout:
    for lines in fin:
        if flag == True:
            flag = False
            continue
        if any(bad_y in lines for bad_y in bad_years):
            flag = True
            continue
        else:
            fout.write(lines)
fin.close()
fout.close()
os.remove("messages_reversed_fixed.txt")
#sys.exit()


#copy only line containing target user conversations

start=datetime.now()
good_words = ["Ida Suninen", "1424892921@facebook","Hugo Bertello", "569847884@facebook"]
with open('messages_reversed_pure.txt') as fin, open('messages_ida.txt', 'w') as fout:
    fn=fin.readlines()
    i=0
    length = file_len("messages_reversed_pure.txt")
    while i < length:
        """if i % 5000 == 0 or (i-1) % 5000 == 0:
            print i, " steps completed out of ", length"""
        if any(goodw in fn[i] for goodw in good_words) and any(goodw in fn[i+1] for goodw in good_words):
            i+=1
            continue
        if good_words[0] in fn[i] or good_words[1] in fn[i]:
            k=0
            while i+k < length and (good_words[0] in fn[i+k] or good_words[1] in fn[i+k]):
                try:
                    fout.write(fn[i+k])
                    fout.write(fn[i+k+1])                 
                    k+=2
                except IndexError:
                    k+=2
                    continue
            i+=k
            if i < length and (good_words[2] in fn[i] or good_words[3] in fn[i]):      
                h=0              
                while i+h < length and (good_words[2] in fn[i+h] or good_words[3] in fn[i+h]):
                        try:
                            fout.write(fn[i+h])
                            fout.write(fn[i+h+1])                
                            h+=2
                        except IndexError:
                            h+=0
                            continue        
                i+=h                  
            else:
                i+=2
                continue
        else:
            i+=1
fin.close()
fout.close()

with open('messages_reversed_pure.txt') as fin:
    n = 0
    for lines in fin:
        if "Ida Suninen" in lines and "2016" in lines:
            n+=1
        else:
            continue
fin.close()
os.remove("messages_reversed_pure.txt")

print
print "Time taken to copy target user conversations: ", datetime.now()-start
print


with open('messages_ida.txt') as fin:
    k = 0
    for lines in fin:
        if "Ida Suninen" in lines and "2016" in lines:
            k+=1
        else:
            continue
fin.close()

print "You missed", n-k, "Ida lines."

"""
other options:
iterable = iter(xrange(100))
>>> for i in iterable:
        if i % 10 == 0:
            [iterable.next() for x in range(10)]
"""
