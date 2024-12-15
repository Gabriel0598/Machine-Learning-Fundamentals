import featuretools as ft
import pandas as pd

# load data
data = ft.demo.load_mock_customer()

# datasets
customers_df = data["customers"]
sessions_df = data["sessions"]
transactions_df = data["transactions"]

# Explicitly parse datetime columns
sessions_df["session_start"] = pd.to_datetime(sessions_df["session_start"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
transactions_df["transaction_time"] = pd.to_datetime(transactions_df["transaction_time"], format="%Y-%m-%d %H:%M:%S", errors="coerce")

dataframes = {
    "customers": (customers_df, "customer_id"),
    "sessions": (sessions_df, "session_id", "session_start"),
    "transactions": (transactions_df, "transaction_id", "transaction_time")
}

relationships = [
    ("sessions", "session_id", "transactions", "session_id"),
    ("customers", "customer_id", "sessions", "customer_id")
]

feature_matrix_customers, features_defs = ft.dfs(
    dataframes=dataframes,
    relationships=relationships,
    target_dataframe_name="customers"
)

print(feature_matrix_customers)

feature_matrix_sessions, features_defs = ft.dfs(
    dataframes=dataframes, relationships=relationships, target_dataframe_name="sessions"
)

feature_matrix_sessions.head(5)

feature = features_defs[18]
print(feature)

ft.graph_feature(feature)
ft.describe_feature(feature)
