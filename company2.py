import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
import matplotlib.pyplot as plt

def update_file(filename, id, name, product, unit, price, comm):
    new_entry = {
        'ID': id,
        'Name': name,
        'Product': product,
        'Unit': unit,
        'Price': price,
        'Total': unit * price,
        'Percentage': comm,
        'Commission': (unit * price) * (comm * 0.01)
    }
    if os.path.exists(filename):
        df = pd.read_excel(filename, engine='openpyxl')
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])
    df.to_excel(filename, index=False)

def delete_update(filename, id):
    if os.path.exists(filename):
        df = pd.read_excel(filename, engine='openpyxl')
        existing_index = df[df['ID'] == id].index
        if not existing_index.empty:
            df = df[df['ID'] != id]
            df.reset_index(drop=True, inplace=True)
        else:
            print("Employee is not in the list")
        df.to_excel(filename, index=False)
        print(df)
    else:
        print("File path doesn't exist")

def update(filename):
    entries = int(input("How many entries you want: "))
    while entries:
        entries -= 1
        id = int(input("Enter the ID: "))
        name = input("Enter the Name: ")
        product = input("Enter the Product: ")
        unit = int(input("Enter the No. of Units Sold: "))
        price = int(input("Enter the Price per Unit: "))
        comm = int(input("Enter the Commission (%): "))
        update_file(filename, id, name, product, unit, price, comm)
        sheet = input("Do you want to see the Excel Sheet? (Y/N): ").lower()
        if sheet == 'y':
            df = pd.read_excel(filename, engine='openpyxl')
            print(df)

    delete = input("Do you want to delete an entry? (Y/N): ").lower()
    if delete == 'y':
        del_count = int(input("How many entries to delete: "))
        while del_count:
            del_count -= 1
            id = int(input("Enter the ID to delete: "))
            delete_update(filename, id)

def process_six_months_data():
    months = ['jan.xlsx', 'feb.xlsx', 'march.xlsx', 'april.xlsx', 'may.xlsx', 'june.xlsx']
    combined_df = pd.DataFrame()

    for file in months:
        if os.path.exists(file):
            df = pd.read_excel(file, engine='openpyxl')
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        else:
            print(f"File {file} not found. Skipping...")

    combined_df.to_excel('merged_all_months.xlsx', index=False)

    summary_df = combined_df.groupby('Name').agg(
        Total_Units_Sold=('Unit', 'sum'),
        Total_Cost=('Total', 'sum'),
        Total_Commission=('Commission', 'sum')
    ).reset_index()

    summary_df.to_excel('summary.xlsx', index=False)

  
    performance_df = summary_df.sort_values(by='Total_Units_Sold', ascending=False).reset_index(drop=True)
    performance_df.to_excel('performance.xlsx', index=False)


    plt.figure(figsize=(10, 6))
    plt.bar(performance_df['Name'], performance_df['Total_Units_Sold'], color='orange')
    plt.title('Employee Performance (Units Sold)')
    plt.xlabel('Employee Name')
    plt.ylabel('Total Units Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_file = 'performance_chart.png'
    plt.savefig(chart_file)
    plt.close()

    book = load_workbook('performance.xlsx')
    sheet = book.active
    img = XLImage(chart_file)
    img.anchor = 'F2'  
    sheet.add_image(img)
    book.save('performance.xlsx')

month = input("Enter the month (Jan/Feb/March/April/May/June): ").lower()
month_map = {
    'jan': 'jan.xlsx',
    'feb': 'feb.xlsx',
    'march': 'march.xlsx',
    'april': 'april.xlsx',
    'may': 'may.xlsx',
    'june': 'june.xlsx'
}

if month in month_map:
    filename = month_map[month]
    update(filename)
    final = input("Do you want to process 6-month summary and performance? (Y/N): ").lower()
    if final == 'y':
        process_six_months_data()
        print("Summary and performance report generated successfully.")
else:
    print("Invalid month entered. Please try again.")
