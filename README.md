**FastAPI Excel Processor Assignment**. It's structured and easy for reviewers to understand.

---

````markdown
# FastAPI Excel Processor

A lightweight and efficient API built using FastAPI that allows users to read, explore, and compute values from an Excel sheet. This project was developed as part of an assessment to demonstrate practical API development skills.

---

##  Project Objective

The goal of this application is to process an Excel workbook (`capbudg.xls`) and expose RESTful endpoints that let users:

- List available tables (sheets) in the Excel file
- Retrieve row labels from a selected table
- Calculate the sum of numerical values from a specific row

---
##  Project Structure

```
.
├── IRIS_Public_Assignment/
│   ├── main.py                 
│   ├── excel_handler.py       
│── └── Data/
│       └── capbudg.xls
├── requirements.txt
├── README.md
└── postman collection json
```
##  Getting Started

### Prerequisites

Make sure Python 3.13+ is installed. Then, clone this repository and set up a virtual environment.

```bash
git clone https://github.com/yourusername/fastapi-excel-api.git
cd IRIS_Public_Assignment
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install -r requirements.txt
````

### Run the API

```bash
uvicorn IRIS_Public_Assignment.main:app --reload
```

Visit the interactive docs at:
 `http://127.0.0.1:8000/docs`

---



---

## API Endpoints

### 1. `GET  http://127.0.0.1:8000/tables`

Returns a list of all available sheet names  in the Excel file.

#### Example Response

```json
{
  "tables": ["CapBudgWS"]
}
```

---

### 2. `GET http://127.0.0.1:8000/table`

Returns the row names from a specified sheet.

#### Query Parameter

* `table` – Name of the sheet

#### Example Request

`GET http://127.0.0.1:8000/table?table=CapBudgWS`

#### Example Response

```json
{
  "sheet": "CapBudgWS",
  "rows": [
    "Initial Investment=",
    "Tax Credit (if any )=",
    ...
  ]
}
```

---

### 3. `GET http://127.0.0.1:8000/sum`

Calculates the sum of numeric values in a specified row of a given table.

#### Query Parameters

* `table` – Sheet name
* `row` – Label of the row

#### Example Request

`GET http://127.0.0.1:8000 /sum?table=CapBudgWS&row=Tax Credit (if any )=`

#### Example Response

```json
{
  "sheet": "CapBudgWS",
  "row": "Tax Credit (if any )=",
  "total": 0.4
}
```

---

## Testing with Postman

A Postman collection is included in this repo:
 `Postman json file`
To use:

1. Open Postman.
2. Click **Import** → Upload the `.json` file.
3. Send requests using the saved collection.

---

##  Insights

### Potential Improvements

* Add a file upload endpoint to support dynamic Excel uploads.
* Extend support for `.xlsx` and `.csv` formats.
* Implement pagination and sorting for large sheets.
* Include a simple frontend UI for non-technical users.

### Edge Cases Not Covered

* Completely empty sheets or rows.
* Mixed data types in a row (strings and numbers).
* Sheets with merged cells or complex formatting.

---

## Dependencies

* fastapi
* uvicorn
* pandas
* openpyxl
* xlrd

Install via:

```bash
pip install -r requirements.txt
```

---

##  Author

**Your Name**
GitHub: [ manoj234-byte ](https://github.com/manoj234-byte)
Email: [manojvenkata234@gmail.com]

---
