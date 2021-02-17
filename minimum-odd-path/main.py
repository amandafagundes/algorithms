#!/usr/bin/env python3

import csv
import sys
import math
import copy
import heapq as hq

class MinimumOddPath(object):
    nodeCount = 0
    edgesCount = 0
    nodes = []
    queue = []

    def main(self):
        if len(sys.argv) > 1:
            self.readFile(sys.argv[1])
        else:
            self.inputData()
        distance = self.customDijkstra()
        if bool(distance) and distance != 99999:
            print(distance)
        else:
            print(':(')

    def readFile(self, filePath):
        with open(filePath) as csv_file:
            csvReader = csv.reader(csv_file, delimiter=' ')
            firstRow = next(csvReader)

            self.nodeCount = int(firstRow[0])
            self.edgesCount = int(firstRow[1])

            self.nodes = [{'node': '1',
                           'paths': {'odd': {'cost': 0, 'pathSize': 1}, 'even': {'cost': 99999, 'pathSize': 1}},
                           'neighbors': []}]

            self.nodes.extend([{'node': f'{el}',
                                'paths': {'odd': {'cost': 99999, 'pathSize': 1}, 'even': {'cost': 99999, 'pathSize': 1}},
                                'neighbors': []}
                               for el in list(range(2, self.nodeCount+1))])

            for row in csvReader:  
                self.nodes[int(row[0]) -
                           1]['neighbors'].append({'node': row[1], 'cost': int(row[2])})
                self.nodes[int(row[1]) -
                           1]['neighbors'].append({'node': row[0], 'cost': int(row[2])})

    def inputData(self):
        graphInfo = input().split(' ')

        self.nodeCount = int(graphInfo[0])
        self.edgesCount = int(graphInfo[1])

        self.nodes = [{'node': '1',
                           'paths': {'odd': {'cost': 0, 'pathSize': 1}, 'even': {'cost': 99999, 'pathSize': 1}},
                           'neighbors': []}]

        self.nodes.extend([{'node': f'{el}',
                                'paths': {'odd': {'cost': 99999, 'pathSize': 1}, 'even': {'cost': 99999, 'pathSize': 1}},
                                'neighbors': []}
                               for el in list(range(2, self.nodeCount+1))])

        lineCount = 0

        while lineCount < self.edgesCount:
            egdeInfo = input().split(' ')

            self.nodes[int(egdeInfo[0]) -
                       1]['neighbors'].append({'node': egdeInfo[1], 'cost': int(egdeInfo[2])})
            self.nodes[int(egdeInfo[1]) -
                       1]['neighbors'].append({'node': egdeInfo[0], 'cost': int(egdeInfo[2])})

            lineCount += 1

    def customDijkstra(self):

        self.queue = [(0, '1')]

        while len(self.queue) > 0:
            u = hq.heappop(self.queue)
            u = self.nodes[int(u[1])-1]
            for node in u['neighbors']:
                w = node['cost']
                v = self.nodes[int(node['node']) - 1]
                self.relax(u, v, w)

        return self.nodes[self.nodeCount-1]['paths']['even']['cost']

    def relax(self, u, v, w):
        if (u['paths']['even']['pathSize'] + 1) % 2 != 0 and u['paths']['even']['cost'] + w < v['paths']['odd']['cost']:
            v['paths']['odd']['pathSize'] = u['paths']['even']['pathSize'] + 1
            v['paths']['odd']['cost'] = u['paths']['even']['cost'] + w
            hq.heappush(self.queue, (v['paths']['odd']['cost'], v['node']))


        elif (u['paths']['odd']['pathSize'] + 1) % 2 == 0 and u['paths']['odd']['cost'] + w < v['paths']['even']['cost']:
            v['paths']['even']['pathSize'] = u['paths']['odd']['pathSize'] + 1
            v['paths']['even']['cost'] = u['paths']['odd']['cost'] + w
            hq.heappush(self.queue, (v['paths']['even']['cost'], v['node']))


if __name__ == '__main__':
    MinimumOddPath().main()
