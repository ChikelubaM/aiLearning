# 1. poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
# Solution

with open("poem.txt", "r") as f:
    word_stats = {}

    for line in f:
        words = line.split()
        for word in words:
            if word not in word_stats:
                word_stats[word] = 1
            else:
                word_stats[word] = word_stats[word] + 1
max_word = ""
max_count = 0

for word, count in word_stats.items():
    if count > max_count:
        max_count = count
        max_word = word

print(f"The word with most occurrences is: {max_word} (appears {max_count} times.)")

# 2. stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# Your input format (stocks.csv) is,
#
# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
#
# Output.csv should look like this,
#
# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68

# Solution
with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(f)

    for line in f:
        tokens = line.strip().split(",")
        stock_name = tokens[0]
        price = float(tokens[1])
        earnings = float(tokens[2])
        book_value = float(tokens[3])

        pe_ratio = price / earnings
        pb_ratio = price / book_value

        out.write(f"{stock_name}, {pe_ratio:.2f}, {pb_ratio:.2f}\n")
