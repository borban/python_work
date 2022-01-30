rivers = {'nile':'egypt', 'mississippi':'usa', 'orinoco':'colombia'}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}")