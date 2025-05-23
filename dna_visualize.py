import matplotlib.pyplot as plt

# DNA sequence
dna_sequence = "AGCTTAGCTAAGGCT"

# Count bases
counts = {
    "A": dna_sequence.count("A"),
    "T": dna_sequence.count("T"),
    "C": dna_sequence.count("C"),
    "G": dna_sequence.count("G"),
}

# Prepare data for plotting
bases = list(counts.keys())
frequencies = list(counts.values())

# Create bar chart
plt.bar(bases, frequencies, color=['green', 'red', 'blue', 'yellow'])

plt.title("DNA Base Counts")
plt.xlabel("Base")
plt.ylabel("Count")

# Show the plot
plt.show()

