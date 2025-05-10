from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from excel_handler import Excel_process

app = FastAPI(title="Excel Sheet API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

excel = Excel_process("C:/Users/manoj/OneDrive/Desktop/Assignment/IRIS_Public_Assignment/Data/capbudg.xls")

@app.get("/tables")
def list_sheets():
    return {"sheets": excel.list_sheet_names()}

@app.get("/table")
def get_table_rows(table: str = Query(...)):
    try:
        row_names = excel.get_first_column_values(table)
        return {"sheet": table, "rows": row_names}
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))

@app.get("/sum")
def get_row_sum(table: str = Query(...), row: str = Query(...)):
    try:
        total = excel.sum_row(table, row)
        return {"sheet": table, "row": row, "total": total}
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))
