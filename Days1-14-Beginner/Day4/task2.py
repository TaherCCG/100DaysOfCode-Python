# Lists

# List of states in America
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",]

# Print the first state in the list
print(states_of_america[0])

# Print states from index 1 to 3
print(states_of_america[1:4])

# Print the last three states in the list
print(states_of_america[-3:])

# Print states from index 2 to the end
print(states_of_america[2:])

# Print the first four states in the list
print(states_of_america[:4])

# Print every second state in the list
print(states_of_america[::2])

# Print the list of states in reverse order
print(states_of_america[::-1])

# Print the number of states in the list
print(len(states_of_america))

# Add a new state to the end of the list
states_of_america.append("Georgia")
print(states_of_america)

# Insert a new state at index 1
states_of_america.insert(1, "New York")
print(states_of_america)

# Remove "Alaska" from the list
states_of_america.remove("Alaska")
print(states_of_america)

# Remove the last state from the list
states_of_america.pop()
print(states_of_america)

# Clear all states from the list
states_of_america.clear()
print(states_of_america)
