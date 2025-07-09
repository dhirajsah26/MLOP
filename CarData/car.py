import pandas as pd 
import numpy as np 

df = pd.read_csv("cardata.csv",low_memory=False)
df = df.ffill()
# print(df['Vehicle Identification Number'].value_counts())

# print(df.dtypes)

# df_correct_dtype = pd.to_numeric(df['Vehicle Identification Number'])
# Left-Side Collision
# print(df_crash.head(10))
# print(df.select_dtypes(include='number').columns)

# print(df[df['Crash Type'] ==  'Left-Side Collision'])
# print(df['Crash Type'].value_counts())


# crash_type_columns = [col for col in df.columns if "Crash Type" in col ]
# df = df[crash_type_columns].dropna()
# # print(df[crash_type_columns].value_counts())
# for  row in df[crash_type_columns]:
    
#     # print(df[row].value_counts())
#     print(df[row].values)

# print(df['DATE (UTC)'].dtype)
# df['DATE (UTC)'] = pd.to_datetime(df['DATE (UTC)'])

# print(df['DATE (UTC)'].dtype)


# crash_type_columns = [col for col in df.columns if "Crash Type" in col]


# for col in crash_type_columns:
#     non_null_values = df[col].dropna()
#     print(f"Non-null values in column '{col}':")
#     print(non_null_values.values)
#     print()
    
# for col in crash_type_columns:
#     non_null_rows = df[df[col].notna()]
#     print(f"\n-- ROws where '{col}' is not null")

#     print(non_null_rows[[col,'DATE (UTC)']])

# df['Left-Side Collision'] 

# Step 1: Convert date column to datetime
df['DATE (UTC)'] = pd.to_datetime(df['DATE (UTC)'])

# Step 2: Identify all Crash Type columns
crash_type_columns = [col for col in df.columns if "Crash Type" in col]

# Step 3: Find the first row with 'Left-Side Collision' in any Crash Type column
crash_index = None
for col in crash_type_columns:
    matching_rows = df[df[col] == 'Left-Side Collision']
    if not matching_rows.empty:
        crash_index = matching_rows.index[0]
        break

# Step 4: If a crash is found, extract 20 seconds before the incident
if crash_index is not None:
    incident_time = df.loc[crash_index, 'DATE (UTC)']
    start_time = incident_time - pd.Timedelta(seconds=20)

    # Step 5: Filter the DataFrame to get data within that 20-second window
    window_df = df[(df['DATE (UTC)'] >= start_time) & (df['DATE (UTC)'] <= incident_time)]

    # Step 6: Display the result
    print(f"Crash occurred at index {crash_index} and time {incident_time}")
    print(f"Showing data from {start_time} to {incident_time}")
    print(window_df)
else:
    print("No 'Left-Side Collision' found in any Crash Type column.")

# for index, row in window_df.iterrows():
#     row['Autosteer'].value()
valid_states = {"Autosteer", "Cruise Control Active", "Full Self-Driving", "Autopilot"}

print(window_df[window_df['Autonomous Driving State'].isin(valid_states)][['Autonomous Driving State','DATE (UTC)']])
