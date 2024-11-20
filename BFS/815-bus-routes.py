class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 1 edge cases
        # 2 stop_to_routes - stop -> routes that get to the stop
        # 3 visited_stops, visited_routes
        # 4 add to visited in handling neighbors
        # 5 q -> (stop, moves)
        # 6 logic to append nei in q: for what if what for what if what
        if source == target:
            return 0
        
        # Create a map of stop to routes
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        # BFS
        visited_stops = set([source])
        visited_routes = set()
        q = deque([(source, 0)])  # (current stop, number of buses taken)

        while q:
            stop, buses = q.popleft()
            if stop == target:
                return buses
            for route in stop_to_routes[stop]:
                if route not in visited_routes:
                    visited_routes.add(route)
                    for nxt_stop in routes[route]:
                        if nxt_stop not in visited_stops:
                            visited_stops.add(nxt_stop)
                            q.append((nxt_stop, buses + 1))
        return -1