def get_counts(seq):
    """
        Counts the number of bases in the sequence.
    """

    counts = dict()
    for base in seq:
        if base not in counts:
            counts[base] = 1
        else:
            counts[base] += 1
    return counts

def print_percent(counts):
    """
        Converts base counts to frequencies and prints. 
    """

    print('Frequencies:')

    total = sum(counts.values())
    for base in counts.keys():
        print(f"{base}: {counts[base]/total}")

print_percent(get_counts('ATCTGACGCGCGCCGC'))
