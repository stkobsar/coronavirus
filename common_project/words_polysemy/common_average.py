
def average_freq(freq, average_yes):
    average = sum(freq) / float(len(freq))
    if average_yes:
        print(average)
