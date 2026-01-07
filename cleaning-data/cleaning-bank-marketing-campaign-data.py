import pandas as pd
import numpy as np

# Load the dataset
bank_df = pd.read_csv("bank_marketing.csv")

# Debug: Print column names to verify
print("Available columns:", bank_df.columns.tolist())

# Create a mapping dictionary for all column variations
col_lower = {col.lower().strip(): col for col in bank_df.columns}

# Function to find column by multiple possible names
def get_col(possible_names):
    for name in possible_names:
        if name.lower() in col_lower:
            return col_lower[name.lower()]
    return None

# Map all required columns
columns_map = {
    'client_id': get_col(['client_id', 'id', 'clientid']),
    'age': get_col(['age']),
    'job': get_col(['job']),
    'marital': get_col(['marital', 'marital_status']),
    'education': get_col(['education']),
    'default': get_col(['default', 'credit_default']),
    'housing': get_col(['housing', 'mortgage']),
    'campaign': get_col(['campaign', 'number_contacts']),
    'duration': get_col(['duration', 'contact_duration']),
    'previous': get_col(['previous', 'previous_campaign_contacts']),
    'poutcome': get_col(['poutcome', 'previous_outcome']),
    'y': get_col(['y', 'campaign_outcome', 'outcome']),
    'day': get_col(['day', 'day_of_month']),
    'month': get_col(['month']),
    'cons_price_idx': get_col(['cons_price_idx', 'cons.price.idx', 'consumer_price_index']),
    'euribor3m': get_col(['euribor3m', 'euribor_three_months', 'euribor'])
}

# Check for missing columns
missing = [k for k, v in columns_map.items() if v is None]
if missing:
    print(f"\nMissing columns: {missing}")
    print("\nPlease verify your CSV has these columns.")
    exit()

print("\nColumn mapping successful!")

# --- 1. Create client_df (client.csv) ---
client_df = bank_df[[
    columns_map['client_id'],
    columns_map['age'],
    columns_map['job'],
    columns_map['marital'],
    columns_map['education'],
    columns_map['default'],
    columns_map['housing']
]].copy()

# Rename columns to match required output
client_df.columns = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']

# Clean job: Change "." to "_"
client_df['job'] = client_df['job'].str.replace('.', '_', regex=False)

# Clean education: Change "." to "_", and "unknown" to np.NaN
client_df['education'] = client_df['education'].str.replace('.', '_', regex=False).replace('unknown', np.nan)

# Convert to boolean
client_df['credit_default'] = (client_df['credit_default'] == 'yes')
client_df['mortgage'] = (client_df['mortgage'] == 'yes')

# Set data types
client_df['client_id'] = client_df['client_id'].astype(int)
client_df['age'] = client_df['age'].astype(int)


# --- 2. Create campaign_df (campaign.csv) ---
campaign_df = bank_df[[
    columns_map['client_id'],
    columns_map['campaign'],
    columns_map['duration'],
    columns_map['previous'],
    columns_map['poutcome'],
    columns_map['y'],
    columns_map['day'],
    columns_map['month']
]].copy()

# Rename columns
campaign_df.columns = ['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts',
                       'previous_outcome', 'campaign_outcome', 'day', 'month']

# Convert to boolean
campaign_df['previous_outcome'] = (campaign_df['previous_outcome'] == 'success')
campaign_df['campaign_outcome'] = (campaign_df['campaign_outcome'] == 'yes')

# Create last_contact_date
campaign_df['last_contact_date'] = pd.to_datetime(
    '2022-' + campaign_df['month'].astype(str) + '-' + campaign_df['day'].astype(str),
    format='%Y-%b-%d',
    errors='coerce'
)

# Final selection and data types
campaign_df = campaign_df[[
    'client_id', 'number_contacts', 'contact_duration',
    'previous_campaign_contacts', 'previous_outcome',
    'campaign_outcome', 'last_contact_date'
]]
campaign_df['client_id'] = campaign_df['client_id'].astype(int)
campaign_df['number_contacts'] = campaign_df['number_contacts'].astype(int)
campaign_df['contact_duration'] = campaign_df['contact_duration'].astype(int)
campaign_df['previous_campaign_contacts'] = campaign_df['previous_campaign_contacts'].astype(int)


# --- 3. Create economics_df (economics.csv) ---
economics_df = bank_df[[
    columns_map['client_id'],
    columns_map['cons_price_idx'],
    columns_map['euribor3m']
]].copy()

# Rename columns
economics_df.columns = ['client_id', 'cons_price_idx', 'euribor_three_months']

# Set data types
economics_df['client_id'] = economics_df['client_id'].astype(int)
economics_df['cons_price_idx'] = economics_df['cons_price_idx'].astype(float)
economics_df['euribor_three_months'] = economics_df['euribor_three_months'].astype(float)


# --- 4. Save the DataFrames to CSV files ---
client_df.to_csv('client.csv', index=False)
campaign_df.to_csv('campaign.csv', index=False)
economics_df.to_csv('economics.csv', index=False)

print("Data cleaning complete!")
print(f"Created files: client.csv ({len(client_df)} rows), campaign.csv ({len(campaign_df)} rows), economics.csv ({len(economics_df)} rows)")