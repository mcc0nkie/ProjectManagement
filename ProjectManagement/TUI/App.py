import os
from rich.console import Console
from rich.table import Table as RichTable
from sqlalchemy import create_engine, text

# Replace this with your SQLite connection string
database_url = "sqlite:///ProjectManagement.db"
engine = create_engine(database_url)

console = Console()

table = RichTable(title="Master View")

# Define the table headers
headers = [
    "Project ID",
    "Project Name",
    "Project Description",
    "UCRA",
    "Model Name",
    "Channel Level 1",
    "Channel Level 2",
    "Channel Level 3",
    "Campaign Name",
    "Offer Code",
    "Task Name",
    "Task Category Name",
    "Task Flow Name",
    "Task Status Name",
]

for header in headers:
    table.add_column(header, justify="left")

# Query the master_view
query = text("SELECT * FROM master_view")
with engine.connect() as connection:
    results = connection.execute(query).fetchall()

# Add the results to the table
for row in results:
    table.add_row(*[str(item) for item in row])

# Clear the terminal and display the table
os.system("cls" if os.name == "nt" else "clear")
console.print(table)

