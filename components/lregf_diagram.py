import matplotlib.pyplot as plt

class LregfDiagram:
    def __init__(self, data):
        self.data = data

    def create_lregf_diagram(self):
        if 'Lregf' not in self.data.columns:
            raise ValueError("Column 'Lregf' not found in the data.")

        fig, ax1 = plt.subplots(figsize=(8, 6))

        # Histogram (bar chart)
        lregf_counts = self.data['Lregf'].value_counts()
        bars = ax1.bar(lregf_counts.index, lregf_counts.values, color='skyblue', alpha=0.6)
        ax1.set_ylabel('Counts')
        ax1.set_xlabel('Lregf')
        ax1.set_title('Lregf Distribution and Trend')

        # Line plot (secondary axis)
        ax2 = ax1.twinx()
        line, = ax2.plot(lregf_counts.index, lregf_counts.values, color='gray', marker='o')
        ax2.set_ylabel('Trend Line')

        fig.tight_layout()
        return fig
