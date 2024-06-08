from csp.containers_problem import Containers
from csp.backtracking import *

problem=Containers(4,6)
initial_state={}
backtrack=BackTracking(problem,var_criterion=random_variable,value_criterion=random_assignment)
print(f'{backtrack}, Random strategies')
print(backtrack.run(initial_state))

backtrack=BackTracking(problem,var_criterion=minimum_remaining_values,value_criterion=least_constraining_value)
print(f'{backtrack}, Minimum Remaining Values, Least Constraining Values')
print(backtrack.run(initial_state))

backtrack=BackTracking(problem,var_criterion=degree_heuristic,value_criterion=least_constraining_value)
print(f'{backtrack}, Degree Heuristic, Least Constraining Values')
print(backtrack.run(initial_state))

print('With forward checking')
print(backtrack.run_with_forward_checking(initial_state,problem.domains))