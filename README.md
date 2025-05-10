# FastAPI Excel Processor

This is a simple and practical API built using FastAPI. It lets you pull useful data from an Excel spreadsheet — things like listing sheets, grabbing row labels, and calculating row totals. I built this as part of a technical assignment to show practical backend skills using FastAPI and some basic data parsing with Pandas.

---

## Project Objective

The main idea here was to work with an Excel file (`capbudg.xls`) and expose a few useful endpoints to:

- List all sheet names in the Excel file
- Get the row labels (from the first column) in a specific sheet
- Calculate the total of numeric values in a particular row

---

## Project Structure

```
.
├── IRIS_Public_Assignment/
│   ├── main.py                 
│   ├── excel_handler.py        
│   └── Data/
│       └── capbudg.xls         
├── requirements.txt
├── README.md
└── postman collection.json
```

---

## Getting Started

### Requirements

You'll need Python 3.13 or you can choose intepreter from 3.0 versions . After cloning the repo, it's a good idea to use a virtual environment.

```bash
git clone https://github.com/yourusername/fastapi-excel-api.git
cd IRIS_Public_Assignment

python -m venv .venv
source .venv\Scripts\activate

pip install -r requirements.txt
```

---

### Run the API

Start the FastAPI server with:

```bash
uvicorn IRIS_Public_Assignment.main:app --reload
```

Once it’s up, you can check the auto-generated docs here:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. `GET /tables`

Returns a list of all sheet names from the Excel file.

**Example Response:**

```json
{
  "tables": ["CapBudgWS"]
}
```

---

### 2. `GET /table`

Returns the row names (first column values) from a specific sheet.

**Query Parameter:**

- `table` – Name of the sheet

**Example Request:**

```
GET /table?table=CapBudgWS
```

**Example Response:**

```json
{
  "sheet": "CapBudgWS",
  "rows": [
    "Initial Investment=",
    "Tax Credit (if any )="
  ]
}
```

---

### 3. `GET /sum`

Returns the total of all numeric values in a specified row.

**Query Parameters:**

- `table` – Name of the sheet
- `row` – Label of the row

**Example Request:**

```
GET /sum?table=CapBudgWS&row=Tax Credit (if any )=
```

**Example Response:**

```json
{
  "sheet": "CapBudgWS",
  "row": "Tax Credit (if any )=",
  "total": 0.4
}
```

---

## Testing with Postman

There’s a Postman collection included so you can test the endpoints quickly:

1. Open Postman.
2. Click **Import** and upload the `.json` file.
3. Send test requests using the collection.

---

## Notes & Improvements

### Things I’d Like to Add Later

- An endpoint for uploading Excel files, so users aren’t stuck with the default one.
- Support for `.xlsx` and maybe even `.csv`.
- Pagination for larger sheets.
- A small frontend to let non-devs interact with the data.

### Known Limitations

- It doesn’t handle empty or merged rows well.
- Rows with mixed data (like numbers and text) might not sum cleanly.
- Fancy formatting in Excel isn’t handled — it expects plain, simple data.

---

## Dependencies

- fastapi
- uvicorn
- pandas
- openpyxl
- xlrd

Install them all via:

```bash
pip install -r requirements.txt
```

---

## Author

GitHub: [manoj234-byte](https://github.com/manoj234-byte)  
Email: manojvenkata234@gmail.com
