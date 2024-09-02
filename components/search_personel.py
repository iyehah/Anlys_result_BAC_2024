import tkinter as tk
import pandas as pd

class SearchPersonel:
    def __init__(self, root, data_file):
        self.root = root
        self.root.title("Search Personnel")

        # Load the data from Excel file
        self.data = pd.read_excel(data_file)

        # Create input label and entry field for NODOSS
        self.label_nodoss = tk.Label(root, text="Enter NODOSS:")
        self.label_nodoss.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nodoss = tk.Entry(root)
        self.entry_nodoss.grid(row=0, column=1, padx=10, pady=10)

        # Create search button
        self.search_button = tk.Button(root, text="Search", command=self.search_personel)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        # Create labels to display the results
        self.label_nompl = tk.Label(root, text="Name (NOMPL):")
        self.label_nompl.grid(row=1, column=0, padx=10, pady=10)

        self.result_nompl = tk.Label(root, text="")
        self.result_nompl.grid(row=1, column=1, padx=10, pady=10)

        self.label_moybac = tk.Label(root, text="Moyen (Moybac):")
        self.label_moybac.grid(row=2, column=0, padx=10, pady=10)

        self.result_moybac = tk.Label(root, text="")
        self.result_moybac.grid(row=2, column=1, padx=10, pady=10)

        self.label_decision = tk.Label(root, text="Decision:")
        self.label_decision.grid(row=3, column=0, padx=10, pady=10)

        self.result_decision = tk.Label(root, text="")
        self.result_decision.grid(row=3, column=1, padx=10, pady=10)

    def search_personel(self):
        nodoss = self.entry_nodoss.get()

        # Search for the row with the given NODOSS
        personel = self.data[self.data['NODOSS'] == nodoss]

        if not personel.empty:
            # Display the found data in the labels
            self.result_nompl.config(text=personel['NOMPL'].values[0])
            self.result_moybac.config(text=personel['Moybac'].values[0])
            self.result_decision.config(text=personel['Decision'].values[0])
        else:
            # If no result is found, display "Not Found"
            self.result_nompl.config(text="Not Found")
            self.result_moybac.config(text="Not Found")
            self.result_decision.config(text="Not Found")


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchPersonel(root, "BAC.xlsx")
    root.mainloop()
