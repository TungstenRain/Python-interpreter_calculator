"""
    This module contains code from
    Think Python by Allen B. Downey
    http://thinkpython.com

    Copyright 2012 Allen B. Downey
    License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
    
    This is to use the interpreter as a calculator
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
"""

# How many seconds are there in 42 minutes and 42 seconds?
>>> (42*60)+42
# 2562

# How many miles are there in 10 kilometers? Note: there are 1.60934 km in a mile
>>> 10/1.60934
# 6.213727366498068

"""
    If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
    mile in minutes and seconds)? What is your average speed in miles per hour?
"""
>>> (10*60*60)/(((42*60)+42)*1.60934)
# 8.731232833486747

"""
    The volume of a sphere with radius r is 4/3pir**3. What is the volume of a sphere with radius 5?
"""
# Import math library
>>> import math
>>> radius = 5
>>> sphere_volume = (4/3)*math.pi*(radius**3)
>>> print(sphere_volume)
# 523.5987755982989

"""
    Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
    Shipping costs $3 for the first copy and 75 cents for each additional copy.
    What is the total wholesale cost for 60 copies?
"""
>>> cover_price = 24.95
>>> discount = .40
>>> cover_price = 24.95
>>> discount = .40
>>> discount_price = cover_price * (1 - discount)
>>> book_volume = 60
>>> shipping_cost = 3 + ((book_volume - 1) * .75)
>>> total_cost = (book_volume * discount_price) + shipping_cost
>>> print(total_cost)
# 945.4499999999999


"""
    If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
    tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""
>>> time_0_hour = 6
>>> time_0_min = 52
>>> distance_1 = 1
>>> distance_2 = 3
>>> distance_3 = 1
>>> pace_easy = (8 * 60) +15 # Convert the pace to seconds
>>> pace_fast = (7 * 60) + 12 # Convert the pace to seconds
>>> time_run_1 = distance_1 * pace_easy # Get the time for the first distance at the easy pace
>>> time_run_2 = distance_2 * pace_fast # Get the time for the second distance at the faster pace
>>> time_run_3 = distance_3 * pace_easy # Get the time for the third distance at the easy pace
>>> time_run_total = time_run_1 + time_run_2 + time_run_3 # total time ran
>>> time_run_total_sec = time_run_total % 60 # The remaining amount of seconds ran
>>> time_run_total_min = time_run_total // 60 # The remaining number of minutes from the run
>>> time_min_2 = time_0_min + time_run_total_min # The initial minutes added to the remaining minutes ran
>>> time_hour_2 = time_min_2 // 60 # If the minutes ran are over 60 this will get the number of hours
>>> time_min_2 = time_min_2 % 60 # This will get the remaining amount of minutes from the run
>>> time_final_hour = time_0_hour + time_hour_2 # Add the starting hour to the number of hours it took
>>> time_final_min = time_min_2 # This is for ease of reading and is not strictly necessary
>>> print("The time you get home to eat breakfast is: " + str(time_final_hour) + ":" + str(time_final_min) + ":" + str(time_run_total_sec) + " AM")
# The time you get home to eat breakfast is: 7:30:6 AM