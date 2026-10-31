"""Extend your phone bill lab with premium membership and tiered pricing.
Im going to use libraries because I am bored and it sounds like an interesting concept
"""
overchargeRate = {
    "premium overuse": 1,
    "regular overuse/premium super-overuse": 2,
    "regular super-overuse": 3
}


def exceeds_data_limit(dataUsed):
    tempDataUsed = float(dataUsed) #i do not enjoy snake case, so i am going to change it as the planning document does not necessarily specify the use of it as being needed.
    
    if tempDataUsed<=10:
    #true if it is below limit, false if not
        return False
    elif tempDataUsed>10:
        return True
    """Return True when data_used exceeds 10 GB; otherwise return False.
    
    Reuse your lab's Boolean-returning function here.
    """


def get_overage_rate(dataUsed, hasPremium):
    dataOverused = 0
    if hasPremium == True:
        if dataUsed > 10 and dataUsed <= 20:
            dataOverused = (dataUsed - 10) * overchargeRate["premium overuse"]
            return dataOverused
        else:
            dataOverused = (dataUsed - 10) * overchargeRate["regular overuse/premium super-overuse"]
            return dataOverused
    else:
        if dataUsed > 10 and dataUsed <= 20:
            dataOverused = (dataUsed - 10) * overchargeRate["regular overuse/premium super-overuse"]
            return dataOverused
        else:
            dataOverused = (dataUsed - 10) * overchargeRate["regular super-overuse"]
            return dataOverused
        
    """Return the numeric rate for every overage GB.
    
    data_used is total usage in GB; has_premium is a Boolean.

    Total data used           Regular    Premium
    10 GB or less                0          0
    More than 10, up to 20       2          1
    More than 20                3          2

    Use if-elif-else for tiers and a nested decision for membership.
    Return the rate rather than printing it.
    """


# def main():
#     """Keep your lab's inputs, calculations, and messages together here.
    
#     Add the premium recommendation described in the README.
#     """
def main():
    dataUsed = float
    planCost = float
    premiumInput = ""
    hasPremium = False

    print("how much data did you use?")
    dataUsed = float(input())
    
    print("how much does your plan cost?")
    planCost = float(input())
    
    #premium input
    print("do you have premium? Input Y for yes or N for no") 
    premiumInput = input()
    #was going to implement recursion or try catch for errors, but it isn't in the planning doc, so it is unneeded (I do not like how the word unneeded is spelled, i feel as though it should be un-needed)
    if premiumInput.strip() == "Y": 
        hasPremium = True
    else:
        hasPremium = False    
    
    if exceeds_data_limit(dataUsed) == True:
        if dataUsed > 10 and dataUsed <= 20:
            print("You are over your data limit")
            print("Moderate extra usage")
            #Use get_overage_rate() instead of the fixed $2 rate.
            print("Your total bill is: " + (str(planCost + get_overage_rate(dataUsed, hasPremium))))
            if hasPremium == False:
                #Add the premium recommendation described in the README.
                print("I would recommend a premium membership to reduce your overage rate")
        elif dataUsed > 20:
            print("You are over your data limit")
            print("High extra usage")
            #Use get_overage_rate() instead of the fixed $2 rate.
            print("Your total bill is: " + (str(planCost + get_overage_rate(dataUsed, hasPremium))))
            if hasPremium == False:
                #Add the premium recommendation described in the README.
                print("I would recommend a premium membership to reduce your overage rate")
                
    else:
        print("You are within your data limit")
        print("Your total bill is: " + str(planCost))
        

# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()



""" Code from lab
dataUsed = 0

def overuse(dataUsed):
    tempDataUsed = float(dataUsed)
    if tempDataUsed<=10:
    #true if it is below limit, false if not
        return True
    elif tempDataUsed>10:
        return False
    
def main():
    print("how much data did you use?")
    amountOveruse = float
    tempData = float(input())
    print("how much does your plan cost?")
    tempCost = float(input())
    
    if overuse(tempData) == False:
        amountOveruse = tempData-10
        if tempData > 10 and tempData <= 15:
            print("You are over your data limit")
            print("Moderate extra usage")
            print("Your total bill is: " + (str(tempCost + amountOveruse * 2 )))
        elif tempData > 15:
            print("You are over your data limit")
            print("High extra usage")
            print("Your total bill is: " + (str((tempCost) + amountOveruse * 2 )))
    else:
        print("You are within your data limit")
        print("Your total bill is: " + str(tempCost))

main()
"""