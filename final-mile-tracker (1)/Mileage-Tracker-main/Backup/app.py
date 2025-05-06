import tkinter as tk
import csv
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyALYC2hBTuwMVw3yXoGrSV_8MTwoIqdEZ0')

from datetime import datetime

def add_trip():
    # Retrieve the values from the input fields
    departure_address = departure_entry.get()
    arrival_address = arrival_entry.get()
    reason = reason_entry.get()
    odometer_start = float(odometer_start_entry.get())
    odometer_end_text = odometer_end_entry.get()
    odometer_end = float(odometer_end_text) if odometer_end_text else 0
    tolls = float(tolls_entry.get() or "0")
    parking = float(parking_entry.get() or "0")

    # Calculate the total miles
    total_miles = calculate_miles(departure_address, arrival_address)

    # Update the miles display label
    miles_display.config(text=f"{total_miles:.2f}")

    # Calculate the total expenses
    expenses = (total_miles * 0.59) + tolls + parking

    # add trip data to dictionary
    date = datetime.now().strftime("%Y-%m-%d")
    trips[date] = {
        "departure_address": departure_address,
        "arrival_address": arrival_address,
        "odometer_start": odometer_start,
        "odometer_end": odometer_end,
        "miles": total_miles,
        "tolls": tolls,
        "parking": parking,
        "reason": reason,
        "expenses": expenses
    }

    # update trip data display
    row = len(trips) + 1
    date_label = tk.Label(middle_frame, text=date)
    date_label.grid(row=row, column=0)

    departure_label = tk.Label(middle_frame, text=departure_address)
    departure_label.grid(row=row, column=1)

    arrival_label = tk.Label(middle_frame, text=arrival_address)
    arrival_label.grid(row=row, column=2)

    odometer_start_label = tk.Label(middle_frame, text=odometer_start)
    odometer_start_label.grid(row=row, column=3)

    odometer_end_label = tk.Label(middle_frame, text=odometer_end)
    odometer_end_label.grid(row=row, column=4)

    miles_label = tk.Label(middle_frame, text=miles)
    miles_label.grid(row=row, column=5)

    tolls_label = tk.Label(middle_frame, text=tolls)
    tolls_label.grid(row=row, column=6)

    parking_label = tk.Label(middle_frame, text=parking)
    parking_label.grid(row=row, column=7)

    reason_label = tk.Label(middle_frame, text=reason)
    reason_label.grid(row=row, column=8)

    expenses_label = tk.Label(middle_frame, text=expenses)
    expenses_label.grid(row=row, column=9)

    # update total miles driven display
    total_miles = sum(trip['miles'] for trip in trips.values())
    miles_display.config(text=total_miles)

    # clear input fields
    date_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    arrival_entry.delete(0, tk.END)
    odometer_start_entry.delete(0, tk.END)
    odometer_end_entry.delete(0, tk.END)
    tolls_entry.delete(0, tk.END)
    parking_entry.delete(0, tk.END)
    reason_entry.delete(0, tk.END)

def export_to_excel():
    import pandas as pd

    # create pandas DataFrame from trips dictionary
    df = pd.DataFrame.from_dict(trips, orient='index', columns=['departure_address', 'arrival_address', 'odometer_start', 'odometer_end', 'miles', 'tolls', 'parking', 'reason', 'expenses'])

    # save DataFrame to Excel file
    df.to_excel('mileage_expenses.xlsx', index_label='date')

    # update status message
    status_message.config(text="Data exported to mileage_expenses.xlsx")

def calculate_miles(departure_address, arrival_address):
    # Use the Google Maps Distance Matrix API to retrieve the distance between the departure and arrival addresses
    directions_result = gmaps.directions(departure_address, arrival_address, mode="driving")

    # Extract the distance value from the API response
    total_distance_meters = directions_result[0]['legs'][0]['distance']['value']

    # Convert the distance from meters to miles
    total_miles = total_distance_meters * 0.000621371

    # Return the total miles
    return total_miles


# create main window
root = tk.Tk()
root.title("Mileage Tracker")

# create header frame
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

header_label = tk.Label(header_frame, text="Mileage Tracker", font=("Arial", 24))
header_label.pack()

# create input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

date_label = tk.Label(input_frame, text="Date (MM/DD/YYYY):", font=("Arial", 12))
date_label.grid(row=0, column=0)

date_entry = tk.Entry(input_frame, font=("Arial", 12))
date_entry.grid(row=0, column=1)

departure_label = tk.Label(input_frame, text="Departure Address:", font=("Arial", 12))
departure_label.grid(row=1, column=0)

departure_entry = tk.Entry(input_frame, font=("Arial", 12))
departure_entry.grid(row=1, column=1)

arrival_label = tk.Label(input_frame, text="Arrival Address:", font=("Arial", 12))
arrival_label.grid(row=2, column=0)

arrival_entry = tk.Entry(input_frame, font=("Arial", 12))
arrival_entry.grid(row=2, column=1)

odometer_start_label = tk.Label(input_frame, text="Odometer Start:", font=("Arial", 12))
odometer_start_label.grid(row=3, column=0)

odometer_start_entry = tk.Entry(input_frame, font=("Arial", 12))
odometer_start_entry.grid(row=3, column=1)

odometer_end_label = tk.Label(input_frame, text="Odometer End:", font=("Arial", 12))
odometer_end_label.grid(row=4, column=0)

odometer_end_entry = tk.Entry(input_frame, font=("Arial", 12))
odometer_end_entry.grid(row=4, column=1)

tolls_label = tk.Label(input_frame, text="Tolls:", font=("Arial", 12))
tolls_label.grid(row=5, column=0)

tolls_entry = tk.Entry(input_frame, font=("Arial", 12))
tolls_entry.grid(row=5, column=1)

parking_label = tk.Label(input_frame, text="Parking:", font=("Arial", 12))
parking_label.grid(row=6, column=0)

parking_entry = tk.Entry(input_frame, font=("Arial", 12))
parking_entry.grid(row=6, column=1)

reason_label = tk.Label(input_frame, text="Reason for Trip:", font=("Arial", 12))
reason_label.grid(row=7, column=0)

reason_entry = tk.Entry(input_frame, font=("Arial", 12))
reason_entry.grid(row=7, column=1)



add_button = tk.Button(input_frame, text="Add Trip", font=("Arial", 12), command=add_trip)
add_button.grid(row=8, column=1, pady=10)

# create middle frame
middle_frame = tk.Frame(root)
middle_frame.pack()

# create trip data labels
date_label = tk.Label(middle_frame, text="Date", font=("Arial", 12, "bold"))
date_label.grid(row=0, column=0)

departure_label = tk.Label(middle_frame, text="Departure Address", font=("Arial", 12, "bold"))
departure_label.grid(row=0, column=1)

arrival_label = tk.Label(middle_frame, text="Arrival Address", font=("Arial", 12, "bold"))
arrival_label.grid(row=0, column=2)

odometer_start_label = tk.Label(middle_frame, text="Odometer Start", font=("Arial", 12, "bold"))
odometer_start_label.grid(row=0, column=3)

odometer_end_label = tk.Label(middle_frame, text="Odometer End", font=("Arial", 12, "bold"))
odometer_end_label.grid(row=0, column=4)

miles_label = tk.Label(middle_frame, text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=5)

tolls_label = tk.Label(middle_frame, text="Tolls", font=("Arial", 12, "bold"))
tolls_label.grid(row=0, column=6)

parking_label = tk.Label(middle_frame, text="Parking", font=("Arial", 12, "bold"))
parking_label.grid(row=0, column=7)

reason_label = tk.Label(middle_frame, text="Reason", font=("Arial", 12, "bold"))
reason_label.grid(row=0, column=8)

expenses_label = tk.Label(middle_frame, text="Expenses", font=("Arial", 12, "bold"))
expenses_label.grid(row=0, column=9)

# create footer frame
footer_frame = tk.Frame(root)
footer_frame.pack(pady=10)

total_miles_label = tk.Label(footer_frame, text="Total Miles Driven:", font=("Arial", 12))
total_miles_label.pack(side=tk.LEFT)

miles_display = tk.Label(footer_frame, text="0", font=("Arial", 12))
miles_display.pack(side=tk.LEFT, padx=10)

export_button = tk.Button(footer_frame, text="Export to Excel", font=("Arial", 12), command=export_to_excel)
export_button.pack(side=tk.LEFT)

status_message = tk.Label(footer_frame, text="", font=("Arial", 12))
status_message.pack(side=tk.LEFT, padx=10)

# create dictionary to hold trip data
trips = {}

# start main loop
root.mainloop()
