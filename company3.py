import pandas as pd
import os
import matplotlib.pyplot as plt

def process_six_months_data():
    # List of monthly filenames
    months = ['jan.xlsx', 'feb.xlsx', 'march.xlsx', 'april.xlsx', 'may.xlsx', 'june.xlsx']
    combined_df = pd.DataFrame()

    # Combine data from all months
    for file in months:
        if os.path.exists(file):
            df = pd.read_excel(file, engine='openpyxl')
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        else:
            print(f"File {file} not found. Skipping...")

    # Save the merged file (optional)
    combined_df.to_excel('merged_all_months.xlsx', index=False)

    # Summarize by employee
    summary_df = combined_df.groupby('Name').agg(
        Total_Units_Sold=('Unit', 'sum'),
        Total_Cost=('Total', 'sum'),
        Total_Commission=('Commission', 'sum')
    ).reset_index()

    # Save summary
    summary_df.to_excel('summary.xlsx', index=False)

    # Rank by performance (units sold)
    performance_df = summary_df.sort_values(by='Total_Units_Sold', ascending=False).reset_index(drop=True)
    performance_df.to_excel('performance.xlsx', index=False)

    # Plotting bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(performance_df['Name'], performance_df['Total_Units_Sold'], color='skyblue')
    plt.title('Employee Performance (Units Sold)')
    plt.xlabel('Employee Name')
    plt.ylabel('Total Units Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('performance_chart.png')
    plt.show()

# Call the function
process_six_months_data()
