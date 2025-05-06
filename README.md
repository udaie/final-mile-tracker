# Mileage Tracker

Mileage Tracker is a simple desktop application designed to help individuals and businesses track their driving mileage for expense reporting and reimbursement. This tool allows users to input trip details, calculates mileage using the Google Maps API, and exports the data to an Excel spreadsheet for easy tracking and reporting.

![Mileage Tracker Screenshot](https://i.imgur.com/AZIJI2e.png)

## Features

- **Trip Logging:** Enter details about each trip, including departure and arrival addresses, odometer readings, tolls, and parking expenses.
- **Mileage Calculation:** Automatically calculate the distance between the departure and arrival locations using the Google Maps API.
- **Expense Calculation:** Calculate total expenses based on mileage, tolls, and parking fees.
- **Data Export:** Export trip data and calculated expenses to an Excel file for reporting or reimbursement purposes.

## Installation

To use Mileage Tracker, follow these steps:

1. Ensure you have Python installed on your system. The application is compatible with Python 3.6 and above.
2. Clone this repository or download the source code to your local machine.
3. Install the required dependencies by running the following command in your terminal or command prompt:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up a Google Maps API key (see Configuration section below).

5. Run the application:

    ```sh
    python app.py
    ```

## Configuration

Before running Mileage Tracker, you need to configure your Google Maps API key:

1. Obtain a Google Maps API key by following the instructions [here](https://developers.google.com/maps/gmp-get-started).
2. Create a `.env` file in the root directory of the project.
3. Add your Google Maps API key to the `.env` file as follows:

    ```plaintext
    GOOGLE_MAPS_API_KEY=YourGoogleMapsAPIKeyHere
    ```

## Usage

Once the application is running:

1. Enter trip details in the provided fields.
2. Click on "Add Trip" to calculate the trip mileage and expenses.
3. To export the trip data, click on "Export to Excel." The application will generate an Excel file containing all entered trips and their associated expenses.

## Contributing

Contributions to the Mileage Tracker project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

Mileage Tracker is released under the MIT License. See the LICENSE file for more details.
