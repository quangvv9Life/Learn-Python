# a list of the states you want to cover

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# The list of stations that you're choosing from

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# something to hold the final set of stations you'll use
final_stations = set()

while states_needed:
    # You need to go through every station and pick the one that covers the most uncovered states
    best_station = None

    # a set of all the states this station covers that haven't been covered yet
    states_covered = set() 

# To loop over every station to see which one is the best station, i.e. a set intersection
    for station, states in stations.items():

        # the set of uncovered states that this station covers
        covered = states_needed & states

        # check whether this station covers more states than the current best_station
        if len(covered) > len(states_covered):
            best_station   = station # if so, this station is the new best_station
            states_covered = covered
    
    # because this station covers some states, those states aren't needed anymore
    states_needed -= states_covered
    # add best_station to the final list of stations in random order
    final_stations.add(best_station)

print(final_stations)

