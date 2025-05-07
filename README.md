# **Email-Project**  

## **Species Email Processing Script**  
## 📑 Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Phase 1: Sorting and Compiling](#phase-1-sorting-and-compiling-species-data)
- [Phase 2: Mass Emailing Program](#phase-2-mass-emailing-program-)
- [Email Template Example](#email-template-example)
- [Output](#output)

### **Description**  
The `Sort_Compile_Species.py` script processes species reference data and email lists by sorting, filtering, and compiling structured datasets for further analysis. This is **Phase 1** of the project. **Phase 2** will focus on a **Mass Emailing Program** (currently in progress).  

---

## **Requirements**  
- Python **3.x**  
- `pandas` library  

Install dependencies if needed:  
```bash
pip install pandas
```

---

## **Setup Instructions**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/SQFOXY/Email-Project
cd your-repo
```

### **2. Place Your Data Files**  
Ensure your dataset is in the `Email-Project/data/` directory:  
- **`Email_list.csv`** → Contains reference numbers and emails  
- **`ref# Specie.xlsx`** → Contains species reference data  

⚠ **Note:** The actual data files are not included in this repository for privacy reasons. Please provide your own dataset before running the script.  

### **3. Run the Script**  
```bash
python Sort_Compile_Species.py
```

### **4. Check the Output Files**  
Processed files will be saved in `Email-Project/data/output/`.  

---

## **Phase 1: Sorting and Compiling Species Data**  

### **Overview**  
The `Sort_Compile_Species.py` script processes and structures species reference data and email lists through the following steps:  

1️⃣ **Counts the number of species** per reference number and merges the count with the email list.  
2️⃣ **Filters species counts** to include only references with **1 to 5 species** (These are the numbers I am using, you can change to align with your needs).  
3️⃣ **Removes entries with missing email addresses** to maintain a clean dataset.  
4️⃣ **Merges the filtered species data with emails** for efficient data handling.  

### **Key Features**  
✅ Reads and processes **CSV & Excel files**  
✅ Filters data based on **species count**  
✅ Cleans the dataset by **removing invalid email entries**  
✅ Saves **structured and compiled outputs** for further use  

### **Generated Output Files**  
📂 `output.csv` → Merged species count with email data  
📂 `filtered_output.csv` → Filtered species count (1–5)  
📂 `filtered_email_list.csv` → Cleaned list with valid emails  
📂 `species_email_output.csv` → Final dataset with species & emails  

---

## **Phase 2: Mass Emailing Program** 🚀  

### **Overview**  
`Mass_Emailing.py` is the second phase of the Email-Project. It automates the process of emailing contributors who are associated with one or more species references. Each person receives **one personalized email** listing all species they are linked to, along with a request to upload photographs via a **Google Form**.

---

### **Key Features**  
✅ Sends **one email per unique reference number** (instead of one per species)  
✅ Each email includes:
  - A personalized **subject line** (`Photo Request for Species - Reference {ref#}`)  
  - A formatted list of species  
  - A direct link to a **Google Form** for submitting photos  

✅ Uses a `.env` file to keep **credentials secure**  
✅ Includes a **test mode** toggle to preview outputs without sending emails  
✅ Skips invalid/missing email addresses  
✅ Logs email send status and prints a clean **summary** at the end  

---

### **Email Template Example**

```text
Dear contributor,

We hope this message finds you well. Our team is currently working to enhance a public reference dataset and we are reaching out for community support.

According to our records, you are associated with the following entries:

Reference #: [ref#]
 - Entry A
 - Entry B
 - Entry C

If you are able to contribute photographs or additional information related to these entries, we would greatly appreciate your input.

Please submit your contributions using the form below:
[Google Form Link]

Thank you for your time and support.

Best regards,  
[Your Project Team or Name]  
[Contact Email]
```

---

### **Setup Instructions**

#### **1. Add Your Final Species Dataset**  
Make sure the following file is available in the `data/output/` directory:
- `species_email_output.csv`

#### **2. Install Dependencies**  
```bash
pip install pandas yagmail python-dotenv
```

#### **3. Add a `.env` File with Your Email Credentials**  
In the project root, create a `.env` file with:
```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password  # Use an app password if you use Gmail with 2FA
```
💡 A `.env.example` file is included to show the format.  
Make a copy and rename it to `.env` before running the script:
```bash
cp .env.example .env
```

✅ Make sure to add `.env` to `.gitignore` so you don’t commit credentials.

#### **4. Run the Email Script**
```bash
python src/Mass_Emailing.py
```

- Set `test_mode = True` to simulate without sending  
- Set `test_mode = False` to send real emails  

---

### **Output**
- Emails are sent via SMTP using `yagmail`  
- A summary of emails sent, failed, and skipped is printed  
- Screenshots of email summary and sample emails can be found in the `report/images/` folder
