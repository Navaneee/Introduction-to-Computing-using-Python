#!/usr/bin/env python
# coding: utf-8

# #### Chapter 3

# In[ ]:


#3.1
question=eval(input("temperature in fahrenheit: "))
print(question)
cel=(5/9)*(question-32)
print("temp in degree celsius is",cel)


# In[ ]:


#3.2
age=eval(input("Age: "))
if age>62:
    print("You can get your pension benefits")


# In[ ]:


#3.3 (a)
year=eval(input("Year: "))
if year%4==0:
    print(year,"could be a leap year")
else:
    print(year,"Definitely not a leap year")


# In[ ]:


#3.3 (b)
ticket=[1,2,3,4]
lottery=eval(input("Lottery number: "))
if lottery in ticket:
    print("You won")
else:
    print("Better luck next time")


# In[ ]:


#3.4
names= ['joe', 'sue','hani', 'sophie']
loginid=input("Login id : ")
if loginid in names:
    print("Login :",loginid)
    print("You are in")
else:
    print("User unknown")
print("Done")


# In[ ]:


#3.5
words=eval(input("Word list : "))
for word in words:
    if len(word)==4:
        print(word)


# In[ ]:


#3.6
for i in range(10):
    print(i)
for l in range(2):
    print(l)


# In[4]:


#3.7
a= range(3, 13)
b=range(0, 10,2) 
c=range(0, 24,3) 
d=range(3,12,5)


# In[ ]:


#3.8
import math
def perimeter(peri):
    return 2*peri*math.pi
perimeter(2)


# In[ ]:


#3.9
def average(x,y):
    return (x+y)/2
average(2,3)


# In[5]:


#3.10
def novowel(word):
    for i in word:
        if i in "aeiouAEIOU":
            return False
    return True
novowel("car")    


# In[8]:


#3.11
def allEven(numList):
    for num in numList:
        if num%2 != 0:
            return False
    return True
allEven([1,2,3,4])


# In[ ]:





# #### Chapter 4

# In[26]:


#4.1
s = '0123456789'
print(s[2:5])
print(s[-3:-1])
print(s[1:8])
print(s[:4])
print(s[7:])


# In[ ]:


#4.2
forecast = 'It will be a sunny day today'

# (a) Assign to variable count the number of occurrences of 'day' in forecast
count = forecast.count('day')

# (b) Assign to variable weather the index where 'sunny' starts
weather = forecast.find('sunny')

# (c) Assign to variable change a copy of forecast where 'sunny' is replaced by 'cloudy'
change = forecast.replace('sunny', 'cloudy')


# In[ ]:


#4.3
firstname=input("name: ")
lastname=input("name: ")
print("hello",firstname+" "+lastname+"!","You just delved into python.")


def greet(firstname,lastname):
    return("hello"+" "+firstname+" "+lastname+"! You just delved into python.")
firstname=input("name: ")
lastname=input("name: ")
print(greet(firstname,lastname))


# In[ ]:


#4.4
def even(n):
    result = []
    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            result.append(str(i))
    print(", ".join(result))
even(17)


# In[12]:


#4.6
students=[]
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])
students


# In[211]:


def numcharacters(infile):
    infile=open("C:/Users/ANAVADYA/Downloads/hello navani.txt")
    content=infile.read()
    count=len(content)
    infile.close()
    return count


# In[212]:


numcharacters(infile)


# In[1]:


#4.8
def stringCount(file_name,string):
    file=open(file_name,"r")
    content=file.read()
    string_count=content.count(string)
    file.close()
    return string_count    


# In[3]:


file_name="C:/Users/ANAVADYA/Downloads/hello navani.txt"
stringCount(file_name,"l")


# In[3]:


def words(file):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt")
    content=file.read()
    word=content.split()
    file.close()
    return word
words("C:/Users/ANAVADYA/Downloads/hello navani.txt",)


# In[4]:


def numlines(file):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt")
    content=file.readlines()
    file.close()
    print(len(content))
    return content
numlines("C:/Users/ANAVADYA/Downloads/hello navani.txt",)


# In[81]:


#4.9
punct=[".",",","?","!",":",";"]
def  words(file):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt",'r')
    content=file.read()
    for pun in punct:
        if pun in content:
            content=content.replace(pun,"")
    file.close()
    print(content)
words("C:/Users/ANAVADYA/Downloads/hello navani.txt")
    


# In[21]:


#4.9
pun=[".",",","?","!"]
def  words(file):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt",'r')
    content=file.read()
    con=content.split()
    print(con)
    output_list=[]
    for word in con:
        for letter in word:
            if letter in pun:
                print(letter,word)
                word=word.replace(letter,"")
                output_list.append(word)
            
        output_list.append(word)
    print(output_list)
words("C:/Users/ANAVADYA/Downloads/hello navani.txt")  


# In[30]:


pun=[".",",","?","!"]
def  words(file_path):
    file=open(file_path,'r')
    content=file.read()
    for i in pun:
        content=content.replace(i,"")
    return content.split()
word_list=words("C:/Users/ANAVADYA/Downloads/hello navani.txt")
print(word_list)


# In[109]:


#4.9
def words(file):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt",'r')
    content=file.read()
    table = str.maketrans('!,.:;?', 6*' ')
    content=content.translate(table)
    file.close()
    print(content)
    


 
words("C:/Users/ANAVADYA/Downloads/hello navani.txt")


# In[10]:


file=open("C:/Users/ANAVADYA/Downloads/u r welcome.txt","w")
file.write("hello\nnavanii")
file.write("where are you?")


# In[9]:


#4.10
def  myGrep(file,target_string):
    file=open("C:/Users/ANAVADYA/Downloads/hello navani.txt",'r')
    content=file.readlines()
    for line in content:
        if target_string in line:
            print(line)
        file.close()
    
   
myGrep("C:/Users/ANAVADYA/Downloads/hello navani.txt","hello")   


# In[3]:


#4.12
s = 'abcdefghijklmnopqrstuvwxyz'#'abc', 'defghijklmnopqrstuvwx', 'wxy', and 'wxyz'
s[:3]
s[3:]

expr1 = s[1:4] 


expr2 = s[:3]  


expr3 = s[3:23]  


expr4 = s[22:25]  


expr5 = s[22:]  


print(expr1, expr2, expr3, expr4, expr5)


# In[2]:


#4.13
s = 'abcdefghijklmnopqrstuvwxyz'
a = s[1:3] == 'bc'


b = s[:14] == 'abcdefghijklmn'


c = s[14:] == 'opqrstuvwxyz'

d = s[1:-1] == 'bcdefghijklmnopqrstuvw'

print(a, b, c, d)

