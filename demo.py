## Prit function ## 

print("Start small. Ship something.")
print('Hello brother')
print('heloo sunny',1,'what happens')
print('hello sunny',12,'good things',sep='$') ## comma separator delimiter which can replace , to any separator 

## for print with multiline 
## prinnt("Hello ritesh patil. what is the issue you are 
## facing") ## SyntaxError: unterminated string literal (detected at line 7)

print("""Hello 'ritesh' patil. what is the issue you are? 
facing""") ## SyntaxError: unterminated string literal (detected at line 7) 
## we need to tackle escape character because we need to know what is the starting and ending point.

print("Hello 'ritesh' patil. what is the issue you are")
## backslash is escaping the character 
print('Hello \'ritesh\' patil. what is the issue you are')

## VARIABLES ## IS JUST LIKE A CONTAINER WHICH CAN HOLD DATA

my_var = 'ritesh'
print (my_var)

x=10
print(my_var,x)

y=5 

print(x+y) ## arithmetic operation 

last_name = 'patil'

print (my_var+last_name)

## print(x+my_var) if x is int then it will run only if str then not 
## multiple variable 

x,y,z=10,20,30 ## multiple assignments
x=y=z=25 ## 

print(x+y+z)

total_sum = (10+20
            +15+15+20+50)
print(total_sum)

## backslash is allow to write code in multiple line otherwise it will give an error () is also working same

## INDENTATION ## c++ NOT REQUIRE, IT PROMOTES READIBILITY , we need to follow parent and child relation
X=1

if(X==1):
    print('WOW')
print('WOW')

## TYPE CASTING \ explicite type cast 
a= 10

b= "20"

b_new = int(b)
    
print(type(b_new))

## IMPLICITE TYPE CAST \ numeric + float implicit 

a= 10

b= 20.57 

print(a+b) 

## str is like an array means like group of values \ always counting is start from 0 

x = 'ritesh patil'
x=['r','i','t','e','s','h']

print(x[2])
print(x[0:3]) ## this will always n-1
print(x[:]) ## start = 0 end = n n is length 0:5
print(x[0:len(x)])

## string methodes ## not waste your time to remember this things 

x = 'ritesh'
print(x.upper()) ## upper \ lower \count \ capitalize

print(x.replace("r","H"))

## List  

x = "ritesh patil really changes needs"

my_list= x.split(" ") ## put the delimeter in py space is also delimeter

print(my_list) 

## ends with or starts with 

file = "raw_data.csv"

if (file.endswith(".csv")):
    print("CSV FILE")
    
if (file.startswith("raw")):
    print("RAW FILE")

print(file.count("a")) ## counts

## is function like to check things 

demo_str = "hello" 

demo_var = "10abc" 

print(demo_var.isalnum()) ## isnumeric \ isalnum

## IF ELSE STATEMENT ## 

x=2000

if (x==20):
    print("x is 20")
elif(x>100):
    if((x>100) & (x<1000)):
        print("Between 100 and 1000")
    else:
        print("greater than 1000")
else:
    print("x is not 20")
    
## == if we check the condition then == used else is end of the condition \ elif \ nested if 

## LOOPS ## are basically used for iterations # for loop 80% while loop 20% 

my_list = ['orders','products','customers']
for i in my_list:
    print(i)
    
for i in range(1,200):  ## rnage function 
    print(i)


table_list = ['orders','products','customers']

for i in table_list:
    if(i.lower() == 'orders'):
        print('table oreder')
    else:
        print('NO Table Orders')

table_list = ['orders','products','customers']

for i in table_list:
    print(i)
    for x in i:
        print(x)
        
## while loop we need to use break statements \ continue statements

table_list = ['products','orders','customers']

for i in table_list:
    print(i)
    if(i.lower() == 'orders'):
            break

table_list = ['products','orders','customers']

for i in table_list:
    if(i.lower() == 'orders'):
        continue  ## this will skip the orders
    print(i)
    
x=1
while(x<11): 
    print(x)
    x=x+1

x=1

while(1==1):
    print("hello")
    x=x+1
    if(x>10):
        break
    
## List ## data structure ## similar to the array  ## list operation 

my_list = [1,2,3,'ritesh','patil',[0,1,'abc']]
        ## 0........................-1,-2,-3

print(my_list[-3:])
print(my_list[::2]) ## skip the values slicing and indexing

my_list.insert(2,'hero')
print(my_list)

my_list.append("mostly")
print(my_list)

my_list.pop() ## autmatically delete the data from last
print(my_list)

my_list=[1,2,3,4,5,6,7]

for i in reversed(my_list):
    print(i)
    
my_list.reverse()
print(my_list)

print(my_list[::-1])

## -3 ## this will starts from end up to the given value and print that much vakues 
my_list=[1,2,3,4,5,6,7]

print(my_list[-3:])
print(my_list[::-1])


my_list=[1,2,3,4,5,6,7] 

# new_list=[]

# for i in my_list:
#     new_list.append(i*i)
    
#     print(new_list) ## list comprehension 

new_list=[i*i for i in my_list if (i%2) == 0 if (i!=2)]

print(new_list)

###### DICTIONARY ####

my_dict = {'x':10,'y':20,'z':30}

my_dict['x'] = 5
    
# my_dict.pop('y')

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict = {'x':10,'y':20,'z':30, 'Demo':{'a':10,'b':20,'c':30}}

print(my_dict['Demo']['c'])

##### SETS ######

# IN A SETS IF VALUES ARE REPETING THEN IT WILL AUTOMATICALLY DELETED 

my_set={2,20,30,40,50,41,41,41}
my_setb={2,20,30,60,70}

print(type(my_set))
print(my_set)
print(my_set.union(my_setb))
print(my_set.intersection(my_setb))

###### TUPLE ####### WE WILL EASILY CONVERT THIS INTO LIST 

MY_TUP = (1,2,3,4,5)
print(MY_TUP)

MY_TUplist = list(MY_TUP)

MY_TUplist.append(6)

print(MY_TUplist)

MY_TUP = tuple(MY_TUplist)

print(MY_TUP)

#### FUNCTIONS #####  INSTEAD OF REWRITING A CODE AGAIN AND AGAIN WE CAN REUSE THE FUNCTION FOR THE SAME 

x=10 

if(x>10):
    print(" x is > 10") 
else: 
    print("iDK")
    
x=20

if(x>10):
    print(" x is > 10") 
else: 
    print("iDK")
    
    
## how to creeate fun 

x=10
def my_addition():
    if(x>10):
        print(" x is > 10") 
    else: 
        print("iDK")

my_addition()

x=20
my_addition() ## adding a prameter inside this function 

def my_addition(value_x):
    if(value_x > 10):
        print(" value is > 10") 
    else: 
        print("iDK")
        
        return value_x

return_value = my_addition(9)
print(return_value)

## default value 
def my_addition(value_x,value_y = 50):
        print(value_x,value_y)

my_addition(20)  ## it will work for default if we not given value otherwise it will taken latest on which you given 

## IF Add * to the parameter it will taken so many values it works like an tuple 
## If we are using ** then it will convert this as dictionary like when we use keys in parameter 

def my_addition(**value_x):
        print(value_x)
my_addition(x=20,y=30,z=40)
