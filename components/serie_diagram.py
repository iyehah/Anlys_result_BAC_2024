import matplotlib.pyplot as plt

class SerieDiagram:
    def __init__(self, data):
        self.data = data

    def create_serie_diagram(self):
        if 'SERIE' not in self.data.columns:
            raise ValueError("Column 'SERIE' not found in the data.")

        serie_counts = self.data['SERIE'].value_counts(normalize=True) * 100

        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, autotexts = ax.pie(
            serie_counts.values,
            labels=serie_counts.index,
            autopct='%1.1f%%',
            colors=plt.cm.Paired.colors,
            startangle=140
        )

        plt.setp(autotexts, size=10, weight="bold")
        ax.set_title('Distribution of Series', fontsize=14)
        ax.legend(wedges, serie_counts.index, title="Series", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        return fig
