print("\n Problem 1 -> \n")

                                ###Problem 1:> Print a list of your favorite foods by using a for loop.
##Creating a list of favourite foods
My_Food_list = ["\n" "\t" "\t" "\t" "\t" "MOMO", "\n" "\t" "\t" "\t" "\t" "CHOWMEIN",
                "\n" "\t" "\t" "\t" "\t" "CHATPATE", "\n" "\t" "\t" "\t" "\t" "CHOILA",
                "\n" "\t" "\t" "\t" "\t" "CHICKEN CURRY (RICE)"]
##Printing my food
print("My Favourite Nepali Food's are : ")
##Using a loop to call all my list
for list in range(0, len(My_Food_list)):
##Printing my favourite food list in order.
   print(My_Food_list[list])

"end of code"

print('Question no 2 -> \n')


            ### Write a program that prompts for the users first name and stores it in a variable named first_name.//
            ##  Do the same  for  the  last  name,  using  the  variable  name  last_name.//
            ##  Then,  use  string  concatenation  (see  section  2.3)  to  greet  them with their full name/

##Defining a function here
def Greeting():
   ##making user to input his/her first name here
   FIRST_NAME=input("What is your first name? \n" )
   ## making user to input his/her last name here
   LAST_NAME = input("What is your last name? \n")
   #merging the first and last name of the given input by user
   FULL_NAME = FIRST_NAME+' '+LAST_NAME
##Printing
#Greets him/her
   print("Hello, ",FULL_NAME,"!")
##Calling main function
   #calling the main function
if __name__ == "__main__":
       Greeting()
##Code ends

print("Question no 3 -> \n")


                #### Write a program that displays the batting average for a baseball play

# Python program that prompts user to enter player name
# and number of hits and number of at-bats and then
# display the players batting average value.
# and then display the name on console.

##Defining a function here
def baseball():

   ##Asking for first name
   BatS_man = input ("What Is The Player's Name?\n ")
   ##Asking for user to input how many boundries scored
   Hits = float(input("How Many Hits?\n "))
   ## Asking for user how manny runs made
   _at_bats = float(input("How Many _At-Bats?\n "))
    ## calculate batting average
   ##Average formula given in question
   avg_batting = Hits/_at_bats
   ## as given in the question (hits) divided by (at-bats)
        #display name and average batting
    ##Printing
   print( BatS_man+ "'s Average Batting is\n  " +str (avg_batting))

#calling a main function
if __name__ == "__main__":
   baseball()


print("Question no 4 -> \n")
        ### Problem 4. Write a program that prompts for four parts of speech, and use those to generate a funny sentence
print(" Give input [ Fancy, Pillow, Whril, STADIUM ")
###Asking user to input pronoun word for printing a sentence
Noun = input( " Enter A Pronoun : \n")
###Asking user to input noun word for printing a sentence
Pronoun = input( "Enter A NOUN: \n")
###Asking user to input adjective word for printing a sentence
Adjective = input( "Enter An Adjective: \n")
###Asking user to input place word for printing a sentence
Location = input( "Enter A Location: \n")
##Printing a full sentenge using users input
print( "Take your {} {} and {}  in at the {}!\n".format(Noun, Pronoun,Adjective,Location))
##Printing


print("Question no 5-> \n")


        ##Problem 5.The Mars Curiosity rover takes photos of the Mars surface, and //
        ## then transmits them to NASA at the speed of light. Light  travels  at  about  186,000  miles  per  second.//
        ## Write  a  program  to  calculate  how  long  it  takes  a  photo //
        ## from  Curiosity to reach NASA when Mars is at its closest orbit to Earth, a distance of about 34 million mile.
import math
##Defining a function
def math():

    ##value of light per sconds
    Speed_light = 186000
    ##Total distance from Mars to Earth
    ## given 34 million
    Distance_MARS = 34000000
    ## Formula: we know speed = distance/time taken
    ## given time equals to distance covered upon time taken

    ## time taken for photos to travel from mars to surface of earth.
    ##Formula used
    Taken_TIme = Distance_MARS / Speed_light
    ##Printing the statement
    print("Time taken by Curiosity to send photos from Mars to NASA")
    ##printing a string variable with the given formula outputs in second's.
    print(str(Taken_TIme) + " second's")


##calling a main function
if __name__ == "__main__":
    math()
##End of the Assignment
print("End of Assignment 1")