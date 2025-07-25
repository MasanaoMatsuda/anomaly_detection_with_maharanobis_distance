from dataloader import AssignmentData
from plot_drawer import plot_scatter_with_index


path = "./data/students_height_and_sitting_height.csv"
data = AssignmentData(path)
df = data.get_data()
df.columns = ["height", "sitting height"]

print(df.head(10))
plot_scatter_with_index(df, "height vs sitting-height", fontsize=12)

