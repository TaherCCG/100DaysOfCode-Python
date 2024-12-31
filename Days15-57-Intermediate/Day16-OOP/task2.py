from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Health", [45, 30, 50])
table.add_column("Speed", [35, 20, 25])
table.add_column("Defense", [25, 35, 10])
table.add_column("Total", [75, 55, 100])
table.align = "l"
table.border = True
print(table)