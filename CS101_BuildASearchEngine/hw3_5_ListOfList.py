def total_enrollment(unil):
    totPeople = 0
    totTuit =  0
    while unil:
        uni = unil.pop()
        totPeople = totPeople + uni[1]
        totTuit = totTuit + uni[1] * uni[2]
    return totPeople, totTuit

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

print total_enrollment(udacious_univs)
print total_enrollment(usa_univs)
