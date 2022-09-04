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

    if selected_option == 1:
        print("The names of the passengers are...")
        for record in records:
            passenger_name = record[3]
            print(f" {passenger_name}")

    elif selected_option == 2:
        num_survived=0
        for record in records:
            survival_status = int(record[1])
            if survival_status == 1:
                num_survived += 1
        print(f"{num_survived} passengers survived")

    elif selected_option == 3:
        females = 0
        males = 0
        for record in records:
            sex = record[4]
            if sex.lower() == "male":
                males += 1
            else:
                females += 1
        print(f"females: {females}, males: {males}")

    elif selected_option == 4:
        children = adults = elderly = 0

        for record in records:
            survived = int(record[1])
            if record[5] != "":
                age = float(record[5])
                if age < 18:
                    children += 1
                elif age < 65:
                    adults += 1
                else:
                    elderly += 1
        print(f"children: {children}, adults: {adults}, elderly: {elderly}")







except IOError:

    print("file not read")
