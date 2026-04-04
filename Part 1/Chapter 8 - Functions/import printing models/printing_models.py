print()

import printing_functions as pf

unprinted_designs_origin = ['phone case', 'robot pendant', 'dodecahedron']
unprinted_designs = unprinted_designs_origin[:]
completed_models = []

pf.printing_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

print()
print(unprinted_designs_origin)