# Start with some designs that need to be printed.   
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def models(unprinted, completed):
    # Simulate printing each design, until none are left.
    # Move each design to completed_models after printing.
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)
    # Display all completed models.
    print("\nThe following models have been printed:")
    for complete in completed:
        print(complete)

models(unprinted_designs, completed_models)