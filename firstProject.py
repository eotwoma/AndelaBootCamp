def make_cofee(water,milk):
	coffee = ''
	print('Take a cup')
	print('pour coffee in to cup')
	print('add sugar')
	#print('pour milk')
	if milk:
		print('pour milk')
		coffee += 'with milk'
	elif water:
		print('pour water')
		coffee += 'with water'
	print('stir')
	return "cup of coffee"
	

def serve_coffee(person_name,water = True, Milk = False):
	coffee = make_cofee(water,milk)
	print(coffee,'for', person_name)



serve_coffee('peter', True, False)
#serve_coffee('Beatrice')
#serve_coffee('Einstein')


#def coffee_type(water = True, milk = True):






