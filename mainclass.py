import pandas as pd

class EmployeeAnalysis:
    def __init__(self, file_path):
        """Load CSV data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def calculate_salary_level(self):
        """Create a new column 'Salary_Level' based on the salary values."""
        self.df['Salary_Level'] = self.df['Salary'].apply(
            lambda x: 'High' if x > 60000 else ('Medium' if x > 30000 else 'Low')
        )

    def export_updated_csv(self, output_file="updated_employee_data.csv"):
        """Save the updated DataFrame to a new CSV file."""
        self.df.to_csv(output_file, index=False)
