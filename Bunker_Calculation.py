# Alieu Sanneh
# Section 05

#CONSTANTS --Information given by 'Safty In Bunkers'
WALL_T = 1.5 # wall thickness of the bunker in meters
DEN_C = 2500 #density of concrete used in kilogram per cubic meter
LABOR_C = 90.64 # cost of labor per square meter of surface area in dollars

#INPUT

name = input( 'Hello there, please enter your name:')

print('Good day ' + name +', welcome to \'Safty in Bunkers\'. I would be' \
      + ' happy to provide you \nwith a quote today!')
      
hint = 'Length is the distance from the right to the' \
       + ' left end of the bunker' \
       + ' in meters.\nPlease enter the desired length of your bunker:'

print()

length = l = float(input(hint))

hint = 'Width is the distance from the front to the back of your' \
       + ' bunker in meters. \nPlease enter the desired width of your bunker:'
width = w = float(input(hint))

hint = 'Height is the measure from the floor to the ceiling of' \
       + ' your bunker in meters.\nPlease enter the desired' \
       + ' height of your bunker.' 
height = h = float(input(hint))

#PROCESSING

ext_v = l * w * h #external volume of bunker in cubic meters

inter_v = ( l - 2 * WALL_T) \
          * ( w - 2 * WALL_T) \
          * ( h - 2 * WALL_T) # internal volmune of bunker in cubic meters

Area_window = 1.2 * 1.9 # area of window in square meters

X = 2 * l * w
Y = 2 * l * h
Z = 2 * h * w

ext_surf_area = ( (X + Y + Z) - Area_window)
# external surface area = (2lw + 2lh + 2hw) - Area of window

N = 2 * WALL_T
l1 = l - N
w1 = w - N
h1 = h - N

inter_surf_area = (2 * ( l1 * w1 + l1*h1 + h1*w1)) - Area_window
# internal surface area = 2(

volume_window = V1 = Area_window * WALL_T

volume_concrete_used = V = ext_v - inter_v - V1
# volume of concrete used = external volume - internal volume - volume of window

# Mass = density * volume (volume of concrete used V)

total_mass_bunker = DEN_C * V
# total mass of bunker in kilograms

total_labor_cost = (LABOR_C * (inter_surf_area + ext_surf_area))

#OUTPUT

print ()
print('Great job ' + name + '! here is your quotation:')
print()
print('Bunker length: ' + str(l) + 'm')
print('Bunker width: ' + str(w) + 'm')
print('Bunker height: ' + str(h) + 'm')

print('External Volume (cubic m): ' + str(ext_v ))
print('Internal Volume (cubic m): ' + str(inter_v))
print('External Surface Area (square m): ' + str(ext_surf_area))
print('Internal Surface Area (square m): ' + str(inter_surf_area))
print('Volume of Concrete (cubic m): ' + str(V))
print('Total mass of concrete: ' + str(total_mass_bunker)+ 'Kg')
print('Total Labor Cost: $' + format(total_labor_cost, '.2f'))
print()
print('Thank you ' + name + '! We look forward to constructing your bunker.')

#Documented tests
#The program was tested using a series of different inputs. below are
#two seperate input values and the out they produced.

# Test1 input values:
# length = 8m
# width = 7m
# height = 6m

#Test1 produced the following results:

#External volume (cubic m.): 336.0
#Internal volume (cubic m.): 60.0
#External surface area (square m.): 289.72
#Internal surface area (square m.): 91.72
#Volume of concrete (cubic m.): 272.58
#Total mass of concrete: 681450.0kg
#Labor cost: $34573.72

#Test2 input values:
# length = 20
# width = 15
# height = 10

#Test2 produced the following results:

#External volume (cubic m.): 3000.0
#Internal volume (cubic m.): 1428.0
#External surface area (square m.): 1297.72
#Internal surface area (square m.): 811.72
#Volume of concrete (cubic m.): 1568.58
#Total mass of concrete: 3921450.0kg
#Labor cost: $191199.64

# to make sure the program is free of logic errors, I made hand calculations
#using the test input values above and the results match with the program's
#output.




    
    
