Age Calculator & Birthday Insights CLI Tool

A command-line interface (CLI) application built with Python to parse user data, validate biological dates, compute exact ages relative to a reference point, and extract chronological insights from group data.

Features

Robust Input Parsing: Automatically splits and cleans inputs formatted as Name, dd-mm-yyyy.

Strict Date Validation: Prevents logical bugs by handling invalid dates (e.g., 31-02-2020), negative digits, empty names, and future birth dates.

Dynamic Age Calculation: Computes exact age in full years, correctly accounting for whether the birthday has already occurred in the current reference year.

Data Analytics & Insights:

Identifies the oldest and youngest members of a group.

Sorts the entire group from oldest to youngest.

Filters and lists individuals born on a specific day of the week (e.g., Sunday).

Displays original inputs in reverse chronological order.

How it Works

The tool loops to accept inputs until you type done.

Expected Input Format

Name, Day-Month-Year


Example: Khalid, 1-2-1989

Logic Breakdown

Validation: Checks for data integrity using Python’s native datetime.date.

Day of Week Extraction: Utilizes strftime("%A") to calculate the exact weekday of birth.

Reference Point: Uses date.today() as the default reference point, easily configurable to any historical date (e.g., date(2021, 1, 1)).

How to Run

Prerequisites

Make sure you have Python 3.x installed.

Steps

Save the code in a file named age_calculator.py.

Open your terminal.

Run the script:

python age_calculator.py
