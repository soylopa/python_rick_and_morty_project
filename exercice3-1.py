import turtle
import random
#Exercice 1.1 print the following lines in a print:
# 5-6, 8*9, 6/2, 5%2, 2*(10+3), 2**4
operations = 5-6
#print(operations)
#aquí deberá cambiar el valor por la nueva operación.
operations = 8*9
#print(operations)

operations_new_list = [5, 6, 8, 9, 6, 2, 5.0, 2, 2, 10, 3, 2, 4]
def cleaningOne():    
    for number in operations_new_list:
        #el -1 interpreta como verdadero el booleano y deberá eliminar todos los números repetidos. 
        # Al usar el método remove, solo eliminará el primer par de duplicados, por eso al imprimir, 
        # muestra el valor del 2 dos veces, porque está 4 veces en la lista.
        if operations_new_list.count(number) > 1:
            #luego de reconocerlos, los elimina.
            operations_new_list.remove(number)
    #print(operations_new_list)
cleaningOne()
#Si cambio el if por el while, el código se repite más de una vez hasta que deje de ser verdadero (1) 
# y para hasta que quede un solo valor de cada número (en este caso son números pero también deberá aplicar para strings)

def cleaningAll():
    for number in operations_new_list:
        while operations_new_list.count(number) > 1:
            operations_new_list.remove(number)
        
cleaningAll()

#print(operations_new_list[-2]**operations_new_list[-1])
cat = 'Cat '
title_variable = 'the lord of the rings'
#print(title_variable.title())
#print(cat.lower() *3)

#Exercice 1.4, create a program that calculates how many cans of cat food you need to feed 10 cats.
# i will need a variable for the cats, another for the can of food per day, and a print.
def feedingPotichat():
    potichat = 5
    cans = potichat * 1.5
    days = 7
    if potichat >= 1:
        cans * 1.5
        total_cans = days * cans
    print('you will need {} cans to feed {} cats during {} days'.format(total_cans, potichat, days))
#feedingPotichat()

#Session 2 Exercice 2.1
#Write a program that asks two questions with input() then prints the values that were entered, you can choose any questions you want
def pizzaFriends():
    friends = int(input('How many people are we?'))
    pizzas = friends * 0.5
    print('you will need {} pizzas for {} friends'.format(pizzas, friends))

def triangleTurtle():
    sides = int(input('Number of sides: '))
    angle = 360/sides
    side_lengt= 60
    for i in range(sides): #aquí no funcionó con la variable side pero sí con la variable i
        turtle.forward(100)
        turtle.left(120)
    turtle.forward(side_lengt)
    turtle.right(angle)
    turtle.done()
#triangleTurtle()

def spiralTurtle(a, b):
    t = turtle.Turtle()
    r=a #tamaño de origen
    for i in range(b): #tamaño total
        t.circle(r + i, 20) #espacio entre líneas
 
#spiralTurtle(10, 100)

def circleFill():
    turtle.color("#a0c8f0", "#285078")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
#circleFill()

def circleArea(r):
    area = 3.14 * (r ** 2)
    return turtle.circle(area)

#circle_large= circleArea(16)
#print(circle_large)

#Session 3: booleans
price = float(input('The burguer price is: '))
vegetarian = float(input('This restaurant is vegetarian? 1 for yes, 2 for no'))
meal_price = float(input('How much did the meal cost?'))
discount_choice = input('Do you have a discount? y/n')
discount_aplicable = discount_choice == 'y'
new_total_price_with_discount = price - (price * 0.10) 
#if price <= 10 and vegetarian == 1:
    #print('This restaurant is a great choice')
#elif not vegetarian == 1:
    #print('This restaurant is not a good choice')
#else:
    #print('Probably not a good idea')
    
#if meal_price >=20:
    #print('Congrats! you have 10 porcent of discount, your new total is: {}'.format(new_total_price_with_discount))
#else:
    #print('your are not elegible for a discount, do you want to add something more to your menu?')
    
bet = float(input('How much you want to bet?'))
color_bet = input('black or red?')
select_your_number = float(input('Which number you select your bet?'))
reward = []

def colour():
    random_number = random.randint(1,2)
    if random_number == 1:
        colour = 'red'
    else:
        colour= 'black'
    return colour

def number():
    random_number=random.randint(1,100)