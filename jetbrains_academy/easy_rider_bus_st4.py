# The string containing the data in JSON format is passed to standard input.
# Make sure each bus line has exactly one starting point (S) and one final stop (F).
# If a bus line does not meet this condition, stop checking and print a message about it.
# Do not continue checking the other bus lines.
# If all bus lines meet the condition, count how many starting points and final stops there are.
# Print their unique names in alphabetical order.
# Count the transfer stops and print their unique names in alphabetical order.
# A transfer stop is a stop shared by at least two bus lines.


import json
import sys


class StopInfo:
    def __init__(self, stop_id=0, stop_name='', stop_type=''):
        self.id = stop_id
        self.name = stop_name
        self.type = stop_type


class BusInfo:
    def __init__(self):
        self.start = StopInfo()
        self.finish = StopInfo()
        self.stops = []


class RoutesHandler:
    def __init__(self):
        self.buses = {}

    def parse_buses(self, stops):
        def parse_stop_info(s):
            return StopInfo(s['stop_id'], s['stop_name'], s['stop_type'])

        for stop in stops:
            bus_id = stop['bus_id']
            if bus_id not in self.buses:
                self.buses[bus_id] = BusInfo()
            if stop['stop_type'] == 'S':
                self.buses[bus_id].start = parse_stop_info(stop)
            if stop['stop_type'] == 'F':
                self.buses[bus_id].finish = parse_stop_info(stop)
            self.buses[bus_id].stops.append(parse_stop_info(stop))

    def is_valid(self):
        for bus_id, bus in self.buses.items():
            if bus.start.name == '' or bus.finish.name == '':
                return False, bus_id
        return True, ''

    def transfers(self):
        all_stops = {}
        result = []

        for _, bus in self.buses.items():
            for stop in bus.stops:
                if stop.name not in all_stops:
                    all_stops[stop.name] = 1
                else:
                    all_stops[stop.name] += 1

        for key, value in all_stops.items():
            if value > 1:
                result.append(key)
        result.sort()
        return result

    def starts(self):
        result = set()
        for _, bus in self.buses.items():
            result.add(bus.start.name)
        return sorted(result)

    def finishes(self):
        result = set()
        for _, bus in self.buses.items():
            result.add(bus.finish.name)
        return sorted(result)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            input_str = file.read()
    else:
        input_str = input()

    routes = json.loads(input_str)

    handler = RoutesHandler()
    handler.parse_buses(routes)
    is_valid, bus = handler.is_valid()
    if not is_valid:
        print(f'There is no start or end stop for the line: {bus}.')
        return
    starts = handler.starts()
    transfers = handler.transfers()
    finishes = handler.finishes()
    if len(starts) > 0:
        print(f'Start stops: {len(starts)} {starts}')
    if len(handler.transfers()) > 0:
        print(f'Transfer stops: {len(transfers)} {transfers}')
    if len(handler.finishes()) > 0:
        print(f'Finish stops: {len(finishes)} {finishes}')


if __name__ == '__main__':
    main()
