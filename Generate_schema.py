import pandas as pd
import os

# ── CONFIG: update these paths to match where your CSVs are saved ──────
csv_files = {
    "orders":                 "D:/instacart_market_analysis/orders.csv",
    "products":               "D:/instacart_market_analysis/products.csv",
    "aisles":                 "D:/instacart_market_analysis/aisles.csv",
    "departments":            "D:/instacart_market_analysis/departments.csv",
    "order_products_prior":   "D:/instacart_market_analysis/order_products__prior.csv",
    "order_products_train":   "D:/instacart_market_analysis/order_products__train.csv",
}

# ── Map pandas dtypes → PostgreSQL types ───────────────────────────────
def pandas_to_pg(dtype, col_name):
    dtype_str = str(dtype)
    col_lower = col_name.lower()
    if 'int' in dtype_str:
        return 'INTEGER'
    elif 'float' in dtype_str:
        return 'NUMERIC'
    elif 'bool' in dtype_str:
        return 'BOOLEAN'
    elif 'datetime' in dtype_str:
        return 'TIMESTAMP'
    else:
        if any(x in col_lower for x in ['_id', 'id']):
            return 'INTEGER'
        elif any(x in col_lower for x in ['name', 'desc', 'aisle', 'department']):
            return 'TEXT'
        else:
            return 'TEXT'

def generate_create_table(csv_path, table_name):
    df = pd.read_csv(csv_path, nrows=500)   # sample 500 rows to infer types
    lines = [f"CREATE TABLE IF NOT EXISTS {table_name} ("]
    col_defs = []
    for col in df.columns:
        pg_type = pandas_to_pg(df[col].dtype, col)
        is_pk = (col == f"{table_name.rstrip('s')}_id") or (col == f"{table_name}_id")
        if is_pk:
            col_defs.append(f"    {col} {pg_type} PRIMARY KEY")
        else:
            col_defs.append(f"    {col} {pg_type}")
    lines.append(",\n".join(col_defs))
    lines.append(");")
    return "\n".join(lines)

def generate_copy_statement(csv_path, table_name):
    abs_path = os.path.abspath(csv_path).replace("\\", "/")
    return (
        f"COPY {table_name}\n"
        f"FROM '{abs_path}'\n"
        f"DELIMITER ','\n"
        f"CSV HEADER;"
    )

# ── RUN ─────────────────────────────────────────────────────────────────
print("=" * 60)
print("  AUTO-GENERATED PostgreSQL SCHEMA")
print("  Copy everything below into your Query Editor")
print("=" * 60)
print()

all_creates = []
all_copies  = []

for table_name, csv_path in csv_files.items():
    if os.path.exists(csv_path):
        all_creates.append(generate_create_table(csv_path, table_name))
        all_copies.append(generate_copy_statement(csv_path, table_name))
    else:
        print(f"-- WARNING: {csv_path} not found, skipping {table_name}\n")

print("-- ============================================")
print("-- STEP 1: CREATE TABLES")
print("-- ============================================\n")
for stmt in all_creates:
    print(stmt)
    print()

print("-- ============================================")
print("-- STEP 2: LOAD DATA (COPY commands)")
print("-- ============================================\n")
for stmt in all_copies:
    print(stmt)
    print()

print("-- ============================================")
print("-- STEP 3: VERIFY ROW COUNTS")
print("-- ============================================\n")
for table_name in csv_files:
    print(f"SELECT COUNT(*) FROM {table_name};")