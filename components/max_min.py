class MaxMinMoybac:
    def __init__(self, data):
        self.data = data

    def calculate_max_min(self):
        max_value = self.data['Moybac'].max()
        min_value = self.data['Moybac'].min()
        max_name = self.data.loc[self.data['Moybac'].idxmax(), 'NOMPL']
        min_name = self.data.loc[self.data['Moybac'].idxmin(), 'NOMPL']
        return max_value, min_value, max_name, min_name
