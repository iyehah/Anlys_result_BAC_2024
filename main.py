import pandas as pd
from components.serie_diagram import SerieDiagram
from components.lregf_diagram import LregfDiagram
from components.max_min import MaxMinMoybac
from components.search_personel import SearchPersonel

class DataVisualizer:
    def __init__(self, excel_file):
        self.data = pd.read_excel(excel_file)
        self.serie_diagram = SerieDiagram(self.data)
        self.lregf_diagram = LregfDiagram(self.data)
        self.max_min_moybac = MaxMinMoybac(self.data)

    def create_serie_diagram(self):
        return self.serie_diagram.create_serie_diagram()

    def create_lregf_diagram(self):
        return self.lregf_diagram.create_lregf_diagram()

    def calculate_max_min(self):
        return self.max_min_moybac.calculate_max_min()
