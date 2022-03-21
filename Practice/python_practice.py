from cgi import print_directory
from itertools import count

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#print(f"I received {percentage_votes}% of the total votes")
message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in this election was {total_votes:,}. "
    f"You received {percentage_votes:.2f}% of the total vote."
)
print(message_to_candidate)




#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys():
#    print(county)
#for voters in counties_dict.values():
#    print(voters)
#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(county + " County has " + str(voters) + " registered voters")

#for county, voters in counties_dict.items():
#    print(f"{county} has {voters} registered voters.")


#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#for county_dict in voting_data:
#    print(county_dict['county'])

