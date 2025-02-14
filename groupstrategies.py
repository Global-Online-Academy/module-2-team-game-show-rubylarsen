# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING


# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# In this strategy the person will choose split for the first game if there has not been any prior to it, however if there has to take the percentage of times the player splits and if it is greater than or equal to .2 (20%), then it will steal

def LuckisEverything3(history):
    totalsplit = 0
    if len(history) == 0:
        return "split"
    else:
        for i in range (len(history)):
            (me, them) = history[i]
            if them == "split":
                totalsplit = totalsplit + 1
                if len(history) == 0:
                    return "steal"
                else:
                    percentagesplit = totalsplit/len(history)

                    if percentagesplit >= 0.20:
                        return "steal"
                    else:
                        return "split"

print(LuckisEverything3(history = hist3))

