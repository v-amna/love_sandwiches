# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS =Credentials.from_service_account_file('creds.json')  
SCOPE_CREDS=CREDS.with_scopes(SCOPE) 
GSPREAD_CLIENT=gspread.authorize(SCOPE_CREDS)
SHEET=GSPREAD_CLIENT.open_by_key('15ZMCWXMQcZWfeWlCeiC2rAQXWoEtFCUgOU-qeNPibtM')

#sales=SHEET.worksheet('sales')
#data=sales.get_all_values()
#print(data)

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("please enter sales data from the last market.")
    print("data should be six numbers, seperated by commas.")
    print("Example:10,20,30,40,50,60\n")

    data_str=input("enter your data here: ")
    #print(f"The data provided is{data_str}")
    sales_data=data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try ,converts all string values into integers.
    Raises valueerror if strings can not be converted into int,
    or there aren't exactly 6 values
    """
    try:
        if len(values)!=6:
            raise ValueError(
                f"Exactly 6 values required, you provided{len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")        


   #print(values)


get_sales_data()    