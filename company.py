import pandas as pd

# 1. Create a new Excel file for the Sales department with 5 employees
sales_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "ID": [101, 102, 103, 104, 105],
    "Department": ["Sales", "Sales", "Sales", "Sales", "Sales"],
    "Salary": [50000, 55000, 48000, 62000, 47000]
}

# Convert the data to a pandas DataFrame
sales_df = pd.DataFrame(sales_data)

# Write the DataFrame to a new Excel file
sales_df.to_excel("sales_department.xlsx", index=False)

# 2. Add a new row (6th employee) to the sales department file without overwriting
new_employee = {
    "Name": "Frank",
    "ID": 106,
    "Department": "Sales",
    "Salary": 54000
}

# Append the new row to the existing dataframe and save it back
sales_df = pd.read_excel("sales_department.xlsx")
new_row_df = pd.DataFrame([new_employee])
sales_df = pd.concat([sales_df, new_row_df], ignore_index=True)

# Save the updated dataframe back to the Excel file
sales_df.to_excel("sales_department.xlsx", index=False)

# 3. Read and print the data from the Sales department Excel sheet
print("\nSales Department Data:")
print(sales_df)

# 4. Print employee name and ID whose salary is above 50k
print("\nEmployees with salary above 50k:")
high_salary_employees = sales_df[sales_df["Salary"] > 50000][["Name", "ID"]]
print(high_salary_employees)

# 5. Change the salary of employee with ID 101 from 50k to 75k
sales_df.loc[sales_df["ID"] == 101, "Salary"] = 75000

# Save the updated data back to the Excel file
sales_df.to_excel("sales_department.xlsx", index=False)

# 6. Delete the employee with ID 105 from the Sales department
sales_df = sales_df[sales_df["ID"] != 105]

# Save the updated data back to the Excel file
sales_df.to_excel("sales_department.xlsx", index=False)

# 7. Create a new Excel file for the Marketing department
marketing_data = {
    "Name": ["Grace", "Heidi", "Ivan", "Judy", "Ken"],
    "ID": [201, 202, 203, 204, 205],
    "Department": ["Marketing", "Marketing", "Marketing", "Marketing", "Marketing"],
    "Salary": [60000, 55000, 63000, 49000, 72000]
}

# Convert the data to a pandas DataFrame
marketing_df = pd.DataFrame(marketing_data)

# Write the DataFrame to a new Excel file
marketing_df.to_excel("marketing_department.xlsx", index=False)

# 8. Merge the Sales and Marketing data and save it to a new sheet named 'Company Assets'
with pd.ExcelWriter("company_assets.xlsx") as writer:
    # Write both sales and marketing data to the new Excel file
    sales_df.to_excel(writer, sheet_name='Sales Department', index=False)
    marketing_df.to_excel(writer, sheet_name='Marketing Department', index=False)
    
    # Merge both DataFrames (concatenate them)
    company_assets = pd.concat([sales_df, marketing_df], ignore_index=True)
    
    # Write the merged data to a new sheet
    company_assets.to_excel(writer, sheet_name='Company Assets', index=False)

# Read and print the final merged data from the 'Company Assets' sheet
company_assets_df = pd.read_excel("company_assets.xlsx", sheet_name="Company Assets")
print("\nMerged Company Assets:")
print(company_assets_df)
