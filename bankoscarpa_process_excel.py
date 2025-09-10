"""
Process an Excel file to count occurrences of a specific number in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import pandas as pd
import pathlib
from loguru import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed"

#####################################
# Define Functions
#####################################

def count_number_in_column(file_path: pathlib.Path, sheet_name: str, column_letter: str, number: float) -> int:
    """Count the occurrences of a specific number in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook["EggsPcc"]
        count = 0
        for cell in sheet[column_letter]:
            if cell.value is not None and isinstance(cell.value, (int, float)):
                if round(cell.value) == number:
                    count += 1
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of a certain number in a specific column, and save the result."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "eggs.xlsx")
    sheet_name = "EggsPcc"
    column_to_check = "B"  
    number_to_count = 314
    
    number_count = count_number_in_column(input_file, sheet_name, column_to_check, number_to_count)

    output_file = pathlib.Path(PROCESSED_DIR, "eggs_number_count.txt")
    
    # Write the results to the output file    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write(f"Occurrences of '{number_to_count}' in column {column_to_check}: {number_count}\n")
    
    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}, Number count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")