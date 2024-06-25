#path to file name
fpath = "C:/Users/jcper/OneDrive/Desktop/Programming and Continued Education/PY4E/sample_data/words.txt"
#opens file for reding and printing
fh = open(fpath)
#Strips blanks at end of file line, prints line by line in all Upper Case
for line in fh: 
    line = line.rstrip()
    print(line.upper())

testing edit function

print("testing")

x = 5
y = 3
print(x+y)
