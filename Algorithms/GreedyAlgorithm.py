def setCoverage(stations, states_needed):
    coverage_set = set()
    selected_stations = []

    while coverage_set != states_needed:
        best_station = list(stations.keys())[0]
        for station in stations.keys():
            if len(coverage_set | stations[station]) > len(coverage_set | stations[best_station]):
                best_station = station
        coverage_set = coverage_set | stations[best_station]
        selected_stations.append(best_station)

    return selected_stations
