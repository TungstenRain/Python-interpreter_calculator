"""
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