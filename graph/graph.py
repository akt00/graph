from typing import Optional


class InvalidGraphAttribute(BaseException):
    pass


class BaseGraph:
    def __init__(self, weighted: bool = False):
        self._weighted = weighted
        self._nodes: dict[int, set[int]] = {}
        self._edges: dict[tuple[int, int], int] = {}

    def __len__(self):
        return len(self._nodes.keys())

    def _edge(self, node_pair: tuple[int, int]) -> Optional[int]:
        if node_pair not in self._edges.keys():
            return None
        else:
            return self._edges[node_pair]

    def add(self, key: int, relations: Optional[dict[int, int]] = None) -> None:
        raise NotImplementedError('BaseGraph.add not implemented')

    def remove(self, key: int) -> bool:
        raise NotImplementedError('BaseGraph.remove not implemented')

    def depth_first_search(self):
        pass

    def breath_first_search(self):
        pass


class DirectedGraph(BaseGraph):
    def __init__(self, weighted: bool = False):
        super(DirectedGraph, self).__init__(weighted=weighted)

    def add(self, key: int, relations: Optional[dict[int, int]] = None) -> None:
        if key not in self._nodes.keys():
            self._nodes[key] = set()

        if relations is not None:
            for k, w in relations.items():
                if k not in self._nodes.keys():
                    self._nodes[k] = set()
                self._nodes[key].add(k)
                self._edges[(key, k)] = w

    def remove(self, key) -> None:
        if key in self._nodes.keys():
            self._nodes.pop(key)
            for k in self._nodes.keys():
                try:
                    self._nodes[k].remove(key)
                except KeyError:
                    pass


class UGraph(BaseGraph):
    def __init__(self, weighted: bool = False):
        super(UGraph, self).__init__(weighted)

    def add(self, key: int, relations: Optional[dict[int, int]] = None) -> None:
        if key not in self._nodes.keys():
            self._nodes[key] = set()

        if relations is not None:
            for k, w in relations.items():
                if k not in self._nodes.keys():
                    self._nodes[k] = set()
                self._nodes[key].add(k)
                self._nodes[k].add(key)
                self._edges[(key, k)] = w
                self._edges[(k, key)] = w

    def remove(self, key) -> None:
        if key in self._nodes.keys():
            nodes = [i for i in self._nodes[key]]
            self._nodes.pop(key)
            for i in nodes:
                self._nodes[i].remove(key)
