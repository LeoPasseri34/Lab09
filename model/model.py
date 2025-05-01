import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._aeroporti = DAO.getAllAeroporti()
        self._rotte = DAO.getRotte()
        self._grafo = nx.DiGraph()
        self._idMap = {}

    def buildGraph(self, distance):
        # aggiungo i nodi
        #self._grafo.add_nodes_from(self._aeroporti)
        #self.addEdges()
        self._grafo.clear()
        distance = float(distance)
        self._rotteGiuste = []

        for i in self._rotte:
            print(i)
            if i.distanza*i.numVoli > distance:
                self._rotteGiuste.append(i)
                a1 = self._aeroporti[i.aeroporto1]
                a2 = self._aeroporti[i.aeroporto2]
                dist_tot = i.distanza*i.numVoli
                self._grafo.add_node(a1)
                self._grafo.add_node(a2)
                self._grafo.add_edge(a1, a2, weight=dist_tot)

    def getRotte(self):
        return self._rotteGiuste


    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()