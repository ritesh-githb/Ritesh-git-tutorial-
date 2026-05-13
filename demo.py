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





