import pandas as pd
import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

# Load the dataset
df = pd.read_csv('../Email-Project/data/output/Test_email.csv')

# Email credentials (Update your .env file)
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASS)


# Google Form link
FORM_LINK = "https://docs.google.com/forms/" 

# Test mode flag: No emails are sent. You just get stats.
test_mode = True  # Change to False to send emails

# Group species by ref#
ref_emails = df[['ref#', 'email_final']].drop_duplicates().set_index('ref#')
grouped_species = df.groupby('ref#')['species'].apply(list)

# Email template
EMAIL_TEMPLATE = """
Dear colleague,

I hope this message finds you well. I’m reaching out as part of the Dr. Uetz Reptile Project, which aims to compile and verify reptile species references and enhance our records with updated photographs.

According to our records, you are associated with the following species:

{species_list}

We are currently collecting high-quality photos to support and improve our reference database. If you are able to contribute photos of any of the above species, we would greatly appreciate your help.

Please submit your photo(s) through the following form:
{form_link}

Thank you so much for your time and contribution!

Best regards,  
Yousra Hamidou  
Virginia Commonwealth University  
hamidouy@vcu.edu
"""

# Loop through each unique ref#
# Initialize counts
sent_count = 0
fail_count = 0
missing_email_refs = set()
missing_email_species = []

# Loop through each group
for ref, species_list in grouped_species.items():
    if ref not in ref_emails.index or pd.isna(ref_emails.loc[ref, 'email_final']) or ref_emails.loc[ref, 'email_final'].strip() == '':
        missing_email_refs.add(ref)
        missing_email_species.extend(species_list)
        continue

    email = ref_emails.loc[ref, 'email_final']
    species_text = '\n'.join(f" - {sp}" for sp in species_list)

    try:
        message = EMAIL_TEMPLATE.format(species_list=species_text, form_link=FORM_LINK, ref_number=ref)
        if not test_mode:
            subject = f"Photo Request for Species - Reference {ref}"
            yag.send(to=email, subject=subject, contents=message)
        print(f"Email prepared for {email}") ###
        sent_count += 1
    except Exception as e:
        print(f"Failed to send email to {email}: {e}") ###
        fail_count += 1

print("\n Summary of Execution:")
print(f" Emails Sent: {sent_count}")
print(f" Failed to Send: {fail_count}")
print(f" Ref#s Without Email: {len(missing_email_refs)}")
print(f" Species Without Email: {len(missing_email_species)}")