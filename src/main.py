from ortools.constraint_solver import pywrapcp, routing_enums_pb2
def demo():
    manager=pywrapcp.RoutingIndexManager(6,2,0)
    routing=pywrapcp.RoutingModel(manager)
    dist=[[0,2,9,10,7,3],[2,0,6,4,3,8],[9,6,0,8,5,7],[10,4,8,0,6,4],[7,3,5,6,0,3],[3,8,7,4,3,0]]
    def cb(f,t):
        return dist[manager.IndexToNode(f)][manager.IndexToNode(t)]
    idx=routing.RegisterTransitCallback(cb)
    routing.SetArcCostEvaluatorOfAllVehicles(idx)
    search=pywrapcp.DefaultRoutingSearchParameters()
    search.first_solution_strategy=routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    sol=routing.SolveWithParameters(search)
    for v in range(2):
        i=routing.Start(v); route=[]
        while not routing.IsEnd(i): route.append(manager.IndexToNode(i)); i=sol.Value(routing.NextVar(i))
        route.append(manager.IndexToNode(i)); print("Vehicle",v,route)
if __name__=="__main__": demo()
