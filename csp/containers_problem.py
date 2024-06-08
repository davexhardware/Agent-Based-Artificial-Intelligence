from csp.contraints import *
class CSP():
    def __init__(self,variables,domains,constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.initial_state= dict()

    def consistent(self,state):
        """
        A state is consistent if all variables respect their constraints in problem.
        """
        return all([const.check(state) for const in self.constraints])
    
    def complete(self,state):
        """
        A state is complete if is considers all the variables of the problem
        """
        return len(state)==len(self.variables)
    
    def goal_test(self,state):
        return self.consistent(state) and self.complete(state)
    
    def assign(self,state,variable,value):
        if(variable in self.variables) and (value in self.domains[variable]):
            new_state=dict(state)
            new_state[variable]=value
            return new_state
        raise ValueError

    def rollback(self,state,variable):
        if variable in self.variables:
            new_state=dict(state)
            del new_state[variable]
            return new_state
        raise ValueError
    
    def legal_moves(self,state,variable):
        """
        Returns all the possible values for variables that keep the state consistent
        """
        if(variable in self.variables):
            possible_values=self.domains[variable]
            #possible_values.pop(state[variable])
            legal_moves=[v for v in possible_values if self.consistent(self.assign(state,variable,v))]
            return legal_moves
        raise ValueError
    
    def count_constraints(self,var_1,var_2):
        """
        Count the constraints between 2 variables
        """
        return sum([1 for c in self.constraints if var_1 in c.variables and var_2 in c.variables])
    
    def remaining_constraints(self,state,variable):
        """
        return the number of remaining constraints that need to be satisfied for the remaining variables (to assign)
        """
        remaining_variables=[var for var in self.variables if var not in state and var!=variable]
        if remaining_variables:
            return sum([self.count_constraints(rv,variable) for rv in remaining_variables])
        else: return 0
    def assignable_variables(self,state):
        return [var for var in self.variables if var not in state]
        

class Containers(CSP):
    def __init__(self,num_containers,max_capacity):
        self.variables=['t1', 't2', 't3', 't4', 't5','f1', 'f2', 'f3','e1','e2','fz1','fz2','fz3','fs1']
        self.domains={var : ['C1','C2','C3','C4'] for var in self.variables}
        self.constraints= [
            DifferentValues(['e1', 'e2']),
                            DifferentValues(['t1', 'f1']),
                            DifferentValues(['t1', 'f2']),
                            DifferentValues(['t1', 'f3']),
                            DifferentValues(['t2', 'f1']),
                            DifferentValues(['t2', 'f2']),
                            DifferentValues(['t2', 'f3']),
                            DifferentValues(['t3', 'f1']),
                            DifferentValues(['t3', 'f2']),
                            DifferentValues(['t3', 'f3']),
                            DifferentValues(['t4', 'f1']),
                            DifferentValues(['t4', 'f2']),
                            DifferentValues(['t4', 'f3']),
                            DifferentValues(['t5', 'f1']),
                            DifferentValues(['t5', 'f2']),
                            DifferentValues(['t5', 'f3']),
                            EqualValues(['fz1', 'fz2', 'fz3']),
                            DifferentValues(['fs1', 'fz1']),
                            DifferentValues(['fs1', 'fz2']),
                            DifferentValues(['fs1', 'fz3']),
                            MaximumCapacity(self.variables, max_capacity)]