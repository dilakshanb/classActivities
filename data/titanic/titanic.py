import csv

file_path = "titanic.csv"

records = []

print("Loading data...", end="")

try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for data in csv_reader:
            records.append(data)

    print("Done!")
    print(f"Successfully loaded {len(records)} records.")

    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per sex
    [4] Display the number of passengers per age group
    [5] Display the number of passengers that survived per age group
    """)

    selected_option = int(input("Enter Your option :"))

    print(f"You have selected option: {selected_option}\n")







except IOError:

    print("file not read")
