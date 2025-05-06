import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import googlemaps
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

class MileageTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mileage Tracker")
        
        # Initialize Google Maps client with API key from environment variable
        google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        if not google_maps_api_key:
            raise ValueError("Google Maps API key not found. Please check your .env file.")
        self.gmaps = googlemaps.Client(key=google_maps_api_key)

        # Initialize trip counter and trips dictionary, and UI setup
        self.trip_count = 0
        self.trips = {}
        self.create_widgets()

    
    def create_widgets(self):
        # Create and pack the widgets for the app
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)

        header_label = tk.Label(header_frame, text="Mileage Tracker", font=("Arial", 24))
        header_label.pack()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.setup_input_fields()

        middle_frame = tk.Frame(self.root)
        middle_frame.pack()

        footer_frame = tk.Frame(self.root)
        footer_frame.pack(pady=10)

        export_button = tk.Button(footer_frame, text="Export to Excel", font=("Arial", 12), command=self.export_to_excel)
        export_button.pack(side=tk.LEFT)

    def setup_input_fields(self):
        # Setup labels and entry fields for user input
        labels_text = ["Date (MM/DD/YYYY):", "Departure Address:", "Arrival Address:", "Odometer Start:",
                       "Odometer End:", "Tolls:", "Parking:", "Reason for Trip:"]
        self.entries = {}
        for idx, text in enumerate(labels_text):
            label = tk.Label(self.input_frame, text=text, font=("Arial", 12))
            label.grid(row=idx, column=0)
            entry = tk.Entry(self.input_frame, font=("Arial", 12))
            entry.grid(row=idx, column=1)
            self.entries[text] = entry

        add_button = tk.Button(self.input_frame, text="Add Trip", font=("Arial", 12), command=self.add_trip)
        add_button.grid(row=len(labels_text), column=1, pady=10)

    def add_trip(self):
        # Add a trip to the trips dictionary based on user input
        try:
            departure_address = self.entries["Departure Address:"].get()
            arrival_address = self.entries["Arrival Address:"].get()
            odometer_start = float(self.entries["Odometer Start:"].get())
            odometer_end = float(self.entries["Odometer End:"].get() or "0")
            tolls = float(self.entries["Tolls:"].get() or "0")
            parking = float(self.entries["Parking:"].get() or "0")
            reason = self.entries["Reason for Trip:"].get()

            total_miles = self.calculate_miles(departure_address, arrival_address)
            expenses = (total_miles * 0.59) + tolls + parking

            date = self.entries["Date (MM/DD/YYYY):"].get() or datetime.now().strftime("%Y-%m-%d")
            self.trips[date] = {
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

            messagebox.showinfo("Success", "Trip added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please check your inputs. Make sure numbers are entered where expected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def calculate_miles(self, departure_address, arrival_address):
        # Calculate miles between two addresses using Google Maps API
        try:
            directions_result = self.gmaps.directions(departure_address, arrival_address, mode="driving")
            total_distance_meters = directions_result[0]['legs'][0]['distance']['value']
            return total_distance_meters * 0.000621371
        except Exception as e:
            messagebox.showerror("Error", f"Could not calculate miles: {e}")
            return 0

    def export_to_excel(self):
        # Export trips data to Excel
        try:
            df = pd.DataFrame.from_dict(self.trips, orient='index')
            filename = f"Mileage_Report_{datetime.now().strftime('%m_%d_%Y')}.xlsx"
            df.to_excel(filename)
            messagebox.showinfo("Export Success", f"Data exported to {filename}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")

# Create the Tk root widget and pass it to our app
if __name__ == "__main__":
    root = tk.Tk()
    app = MileageTrackerApp(root)
    root.mainloop()
