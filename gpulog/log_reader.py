import csv

# 🔹 Set your default CSV file path here
DEFAULT_CSV_FILE = "gpu_data.csv"

# 🔹 These will be populated when the module loads
HEADERS = []
DATA = []


def load_csv(filepath: str):
    """
    Load a CSV file into memory.
    Returns (headers, data).
    """
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            data = [row for row in reader]
        return headers, data
    except Exception as e:
        raise RuntimeError(f"Failed to load CSV file '{filepath}': {e}")


def get_all(data=None):
    """Return all rows (list of dicts)."""
    return data if data is not None else DATA


def get_headers(headers=None):
    """Return the column headers."""
    return headers if headers is not None else HEADERS


def get_column(data=None, headers=None, column_name: str = ""):
    """Return all values from a given column."""
    headers = headers if headers is not None else HEADERS
    data = data if data is not None else DATA
    if column_name not in headers:
        raise KeyError(f"Column '{column_name}' not found in CSV.")
    return [row[column_name] for row in data]


def get_row(data=None, index: int = 0):
    """Return a single row by index."""
    data = data if data is not None else DATA
    if 0 <= index < len(data):
        return data[index]
    else:
        raise IndexError(f"Index {index} out of range.")


def find_rows(data=None, headers=None, column_name: str = "", value: str = ""):
    """Return all rows where column_name matches the given string value."""
    headers = headers if headers is not None else HEADERS
    data = data if data is not None else DATA
    if column_name not in headers:
        raise KeyError(f"Column '{column_name}' not found in CSV.")
    return [row for row in data if row[column_name] == value]

def inv(data=None, headers=None):
    """
    Build a dict using the first column as keys and the second column as values.
    Example: {row[first_col]: row[second_col]}
    """
    headers = headers if headers is not None else HEADERS
    data = data if data is not None else DATA

    if len(headers) < 2:
        raise ValueError("CSV must have at least two columns to create key-value pairs.")

    key_col, value_col = headers[0], headers[1]
    return {row[key_col]: row[value_col] for row in data}


# 🔹 Auto-load default CSV on module import
try:
    HEADERS, DATA = load_csv(DEFAULT_CSV_FILE)
except Exception as e:
    print(f"Warning: Could not auto-load default CSV '{DEFAULT_CSV_FILE}': {e}")

# Uses default file (data.csv) loaded on import
#print(get_headers())           # → headers list
#print(get_row(index=0))        # → first row
#print(inv())
