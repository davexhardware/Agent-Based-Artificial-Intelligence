from search.Node import Node


class GraphSearch:
    """
    A class able to find a solution with a given search strategy
    """

    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []
        self.visited = []  # <- The list containing the visited states

    def __repr__(self):
        return 'Graph Search'

    def run(self):
        """
        Run the search
        :return: a path or a failure
        """

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        # search loop
        while True:
            # check if the node passes the goal test
            if self.problem.goal_test(node.state):
                return 'Ok', node

            # add visited for the graph search
            self.visited.append(node.state)

            # expand the node
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=self.problem.cost(node.state, a)) for s, a in new_states]

            # we retain the states not already visited!
            new_nodes = [n for n in new_nodes if n.state not in self.visited]
            self.fringe = [n for n in self.fringe if n.state not in self.visited]

            # a solution was not found, update the fringe and pick the next node coherently with the search strategy
            self.fringe, node = self.strategy.select(self.fringe, new_nodes)

            # Check if the search fails (empty fringe)
            if len(self.fringe) == 0:
                if self.problem.goal_test(node.state):
                    return 'Ok', node
                return 'Fail', []
