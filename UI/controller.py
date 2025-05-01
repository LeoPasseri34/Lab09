import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_flights(self, e):
        dist = self._view.txt_distance.value
        self._view.txt_result.controls.clear()
        if dist is None or dist == "":
            self._view.create_alert("Inserire la distanza percorsa")
            return
        self._view.txt_result.controls.append(ft.Text(f"La distanza minima percorsa è {dist} miglia"))
        self._model.buildGraph(dist)
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumArchi()} archi"))
        edges = self._model.getRotte()
        for edge in edges:
            self._view.txt_result.controls.append(ft.Text(edge))
        self._view.update_page()
