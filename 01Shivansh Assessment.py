Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #PSET-1
... user_input=input()
... find_pin=user_input.find("pin")    #This line finds whether pin present or not
... output_result=user_input[find_pin:find_pin+(len("pin"))] #gives the ouput
... print(output_result)
... 
... 
... #PSET-2
... main_string=input()
... sub_string=input()
... a=main_string.find(sub_string)
... output=main_string[a:a+(len(sub_string))]
... print(output)
... 
... #PSET-3
... string_one=input()
... whitespace=string_one.find(" ")
... first_name=string_one[:whitespace]
... last_name=string_one[whitespace+1:]
... index_last_name=whitespace+1
... index_first_name=whitespace-1
... print(index_last_name)
... print(index_first_name)
... 
... #PSET-4
... #total_apple = 10
... #apple_eaten = 4
... #print('There are ' + total_apple - apple_eaten + ' left in the basket.' )
... #In the above code bug is present I mean its a TypeError: can only concatenate str (not "int") to str
... #Hence we are converting int to string and the correct code is given below:
... 
... #The code mentioned below gives actual result.
... total_apple = 10
... apple_eaten = 4
... print('There are ' +str(total_apple - apple_eaten) + ' left in the basket.' )
... 
#PSET-5
total_apple = 10
apple_eaten = 4
print(f'There are {total_apple - apple_eaten} left in the basket.' )  #Using f-string

#PSET-6
user_input_script=input()
output_script=user_input_script.replace('piranha','fish',1)
print(output_script)
