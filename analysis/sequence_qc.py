from Bio import SeqIO

record = SeqIO.read("data/input_sequence.fasta", "fasta")

# Extract basic information
sequence_id = record.id
sequence_length = len(record.seq)

# Print results (to verify)
print("Sequence ID:", sequence_id)
print("Sequence Length:", sequence_length)

# Writing QC summary to file
with open("results/qc_summary.txt", "w") as file:
    file.write("SEQUENCE QUALITY CHECK SUMMARY\n")
    file.write("-------------------------------\n")
    file.write(f"Sequence ID: {sequence_id}\n")
    file.write(f"Sequence Length: {sequence_length} amino acids\n")


    # Simple validation logic

    if sequence_length < 100:
        file.write("QC Decision: Sequence is too short for downstream analysis.\n")
    else:
        file.write("QC Decision: Sequence length is sufficient for downstream analysis.\n")
