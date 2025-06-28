import gspread
from oauth2client.service_account import ServiceAccountCredentials

def init_gsheet_connection(json_path, sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)

def log_to_sheet(sheet, tab_name, data):
    try:
        ws = sheet.worksheet(tab_name)
    except gspread.exceptions.WorksheetNotFound:
        ws = sheet.add_worksheet(title=tab_name, rows="100", cols="20")
    
    # Ensure clean format and safe update
    ws.clear()
    if not data.empty:
        header = [data.columns.tolist()]
        rows = data.astype(str).values.tolist()
        ws.update(header + rows)
