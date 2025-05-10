import pandas as pd

class Excel_process:
    def __init__(self, path: str):
        self.path = path
        try:
            self.sheets = pd.read_excel(path, sheet_name=None)
        except Exception as e:
            raise ValueError(f"error loading excel file: {e}")
        
    def list_sheet_names(self):
        return list(self.sheets.keys())
    
    def get_first_column_values(self, sheet_name: str):
        if sheet_name not in self.sheets:
            raise ValueError(f"sheet '{sheet_name}' not found")
        
        df = self.sheets[sheet_name]
        return df.iloc[:, 0].dropna().astype(str).tolist()
    def sum_row(self, sheet_name: str, row_label: str):
        if sheet_name not in self.sheets:
            raise ValueError(f"sheet '{sheet_name}' not found") 
        
        df = self.sheets[sheet_name]
        for i, val in enumerate(df.iloc[:, 0]):
            if str(val).strip() == row_label.strip():
                row = df.iloc[i, 1:]
                return pd.to_numeric(row, errors='coerce').sum(skipna=True)
        raise ValueError(f"row '{row_label}' not found in sheet '{sheet_name}'")
