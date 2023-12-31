#weight of the package in pounds
weight = 5

"""Ground Shipping
Weight of Package	price per Pound	+ Flat Charge
2 lb or less=	$1.50	+ $20.00
Over 2 lb but less than or equal to 6 lb=	$3.00 +	$20.00
Over 6 lb but less than or equal to 10 lb=	$4.00	+ $20.00
Over 10 lb=	$4.75	+ $20.00"""

if weight <= 2:
  cost = weight * 1.5 + 20
elif weight <=6:
  cost = weight * 3 + 20
elif weight  <= 10:
  cost = weight * 4 + 20
else:
  cost = weight *4.75 +20
print("Ground shipping: ",+ cost)

#weight of new package in pounds being ground shipped
weight = 8.4
cost = weight * 4 +20
print('8.4lb package costs $', cost, 'to be ground shipped.')

"""Ground Shipping Premium
Flat charge: $125.00"""

premium_ground_shipping=125
print("Ground Shipping Premium: $"+str( premium_ground_shipping))

"""Drone Shipping
Weight of Package	Price per Pound	and Flat Charge
2 lb or less=	$4.50	+ $0.00
Over 2 lb but less than or equal to 6 lb=	$9.00	+ $0.00
Over 6 lb but less than or equal to 10 lb=	$12.00 +	$0.00
Over 10 lb=	$14.25 + $0.00"""

#weight of new package in pounds being drone shipped
weight = 7.14
if weight <= 2:
  cost = weight *2.5
elif weight <= 6:
  cost = weight *9
elif weight <= 10:
  cost = weight * 12
else:
  cost = weight * 12.25
print("Drone Shipping: ", cost)

weight = 1.5
cost =weight *4.5
print("Drone shipping: $", cost)

#looking at most cost effective shipping method for a 4.8lb package
weight = 4.8
cost_ground= weight * 3 + 20
cost_drone= weight * 9
cost_ground_premium = weight +125

cheapest_cost = (min(cost_ground, cost_drone, cost_ground_premium))

if cheapest_cost== cost_ground:
  print("The cheapest option is Ground shipping with a cost of $", cheapest_cost)
elif cheapest_cost== cost_drone:
  print("The cheapest option is Drone shipping with a cost of $", cheapest_cost)
else:
  print("The cheapest option is Ground Premium shipping with a cost of $", cheapest_cost)
