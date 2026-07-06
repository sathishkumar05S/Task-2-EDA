import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("books.csv")

# Remove unwanted characters and convert to float
data["Price"] = data["Price"].str.replace(r"[^0-9.]", "", regex=True)
data["Price"] = data["Price"].astype(float)

# Plot first 10 books
plt.figure(figsize=(10,5))
plt.bar(data["Book Name"][:10], data["Price"][:10])

plt.title("Book Prices")
plt.xlabel("Book Name")
plt.ylabel("Price (£)")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
