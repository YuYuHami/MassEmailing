import pandas as pd
import os

# Helper function to check if a file exists
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        exit(1)  # Exit the script if a file is missing

# Part 1: Calculating the number of species
# -----------------------------------------

# Define file paths
email_file = '../Email-Project/data/Email_list.csv'
species_file = '../Email-Project/data/ref# Specie.xlsx'

# Check if files exist
check_file_exists(email_file)
check_file_exists(species_file)

# Read the input files
email_data = pd.read_csv(email_file)
species_data = pd.read_excel(species_file, header=None, names=['ref#', 'species'])

# Debug: Print column names
print("Email file columns:", email_data.columns.tolist())
print("Species file columns:", species_data.columns.tolist())

# Calculate the number of species per reference number
species_count = species_data['ref#'].value_counts().reset_index()
species_count.columns = ['ref#', 'species_count']

# Merge the species count with the email data
merged_data = email_data.merge(species_count, on='ref#', how='left')

# Fill NaN values with 0 (for ref# that do not appear in the species data)
merged_data['species_count'] = merged_data['species_count'].fillna(0).astype(int)

# Debug: Print a sample of merged data
print("Sample of merged data:\n", merged_data.head())

# Save the merged data to a CSV file
output_file = '../Email-Project/data/output/output.csv'
merged_data.to_csv(output_file, index=False)
print(f'The merged file with species count has been saved as {output_file}.')

# Part 2: Filtering species count between 1 and 5
# -----------------------------------------------

# Check if output file exists before reading
check_file_exists(output_file)

# Read the output file from Part 1
output_data = pd.read_csv(output_file)

# Debug: Check for missing columns
if 'species_count' not in output_data.columns:
    print("ERROR: 'species_count' column is missing in the output file!")
    exit(1)

# Filter rows where species_count is between 1 and 5 (inclusive)
filtered_output = output_data[(output_data['species_count'] >= 1) & (output_data['species_count'] <= 5)]

# Debug: Print number of rows after filtering
print(f"Rows after filtering species_count between 1 and 5: {len(filtered_output)}")

# Save the filtered data to a new CSV file
filtered_output_file = '../Email-Project/data/output/filtered_output.csv'
filtered_output.to_csv(filtered_output_file, index=False)
print(f'The filtered file has been saved as {filtered_output_file}.')

# Part 3: Removing rows with empty email addresses
# -------------------------------------------------

# Debug: Check for email column
if 'email_final' not in email_data.columns:
    print("ERROR: 'email_final' column is missing in the email data!")
    exit(1)

# Remove rows with missing emails
filtered_email_data = email_data.dropna(subset=['email_final'])

# Debug: Print number of rows after filtering
print(f"Rows after removing empty emails: {len(filtered_email_data)}")

# Save the filtered email data to a new CSV file
filtered_email_file = '../Email-Project/data/output/filtered_email_list.csv'
filtered_email_data.to_csv(filtered_email_file, index=False)
print(f"Filtered email list saved as '{filtered_email_file}'.")

# Part 4: Merging filtered data with species information
# -------------------------------------------------------

# Check if filtered output file exists before reading
check_file_exists(filtered_output_file)

# Read the filtered output and species data
filtered_output = pd.read_csv(filtered_output_file)

# Select only relevant columns for merging
if 'ref#' not in filtered_output.columns or 'email_final' not in filtered_output.columns:
    print("ERROR: Required columns missing in filtered output file!")
    exit(1)

filtered_ref_email = filtered_output[['ref#', 'email_final']]

# Merge the species data with the filtered reference and email data
final_merged_data = species_data.merge(filtered_ref_email, on='ref#', how='inner')

# Debug: Print final merged data sample
print("Sample of final merged data:\n", final_merged_data.head())

# Save the final merged data to a new CSV file
final_output_file = '../Email-Project/data/output/species_email_output.csv'
final_merged_data.to_csv(final_output_file, index=False)
print(f'The species-email association file has been saved as {final_output_file}.')
