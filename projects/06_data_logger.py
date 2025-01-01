
# Data Logger
# Log events or data with timestamps to a file.

import datetime

# Step 1: Set the file where data will be logged
filename = "data_log.txt"

# Step 2: Continuously prompt the user to enter data to log
while True:
    data = input("Enter data to log (or type 'exit' to quit): ")
    if data.lower() == "exit":
        print("Logging stopped.")
        break
    # Step 3: Append the data with a timestamp to the file
    timestamp = datetime.datetime.now()
    with open(filename, "a") as file:
        file.write(f"{timestamp}: {data}\n")
    print("Data logged successfully.")
