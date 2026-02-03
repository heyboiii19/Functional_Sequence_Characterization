#Homology search using BLAST via Biopython

from Bio.Blast import NCBIWWW
from Bio import SeqIO

# Read protein sequence from FASTA file

record = SeqIO.read("data/input_sequence.fasta", format="fasta")

print("Submitting BLASTp request to NCBI...")
print("Sequence ID:", record.id)

# Run BLASTp using Biopython

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
)

# Save BLAST output in XML format

with open("results/blast_output.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

print("BLAST search completed.")
print("Results saved in results/blast_output.xml")
