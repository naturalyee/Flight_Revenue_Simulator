# Flight_Revenue_Simulator (FRS)

There are 4 scenarios. 
1) 100 day 100 ticket
2) 14 day 50 ticket
3) 2 day 20 ticket
1) 1 day 3 ticket

We are trying to optimize the pricing function
We are given a demand and the number of tickets left each day.

The number of tickets sold is = demand - price = # tickets sold

The folders labeled 'line#' have a csv and matplotlib graphs of the 
distributions of the coefficients by scenario. 

Questions:
-Line 121 of FRS.py when does that else ever get hit?
-I think think the most influential line of code for the 100 day simulation is the boolean on line 104 of FRS.py this line assumes that before 12 days left a demand of 186 should sell 8 tickets.
    -What if demand is 199 shouldn't we sell more than 8 tickets? I believe the 'demand - 8' on line 106 of FRS.py should be looked into further.
-Consider the assumption that every case where days_left > 12 should all be considered the same way. This would eliminate the possibility of our perfect case which is  200 == demand every day and selling 1 ticket every day. While this situation is extremely improbable other more probable situations may be left. 

Main thoughts:
-Running this monte carlo may not turn up anything new. 
-The author of this pricing function may have already optimized every boolean coefficient. 
