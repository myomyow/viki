import json


# Count and return the number of HD True and HD False
def count_hd(responses):
    
    hd_true = 0
    hd_false = 0

    # Loop through all the responses
    for response in responses:
        # Get the hd value in flags
        hd = response["flags"]["hd"]
        if hd == True:
            hd_true += 1
        else:
            hd_false += 1

    print("hd_true={0}".format(hd_true))
    print("hd_false={0}".format(hd_false))

    return (hd_true, hd_false)
