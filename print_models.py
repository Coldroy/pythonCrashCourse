def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design, until none are left.
	   Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		completed_models.append(current_design)

