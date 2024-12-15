import featuretools as ft

# load data
data = ft.demo.load_mock_customer()

# datasets
customers_df = data["customers"]
customers_df.sample(5)

sessions_df = data["sessions"]
sessions_df.sample(5)

transactions_df = data["transactions"]
transactions_df.sample(5)

dataframes = {
    "customers": (customers_df, "customers_id"),
    "sessions": (sessions_df, "session_id", "session_start"),
    "transactions": (transactions_df, "transaction_id", "transaction_time")
}

relationship = [
    ("sessions", "session_id", "transactions", "session_id"),
    ("customers", "customer_id", "sessions", "customer_id")
]

feature_matrix_customers, features_defs = ft.dfs(
    dataframes=dataframes,
    relationships=relationship,
    target_dataframe_name="customers"
)
print(feature_matrix_customers)
