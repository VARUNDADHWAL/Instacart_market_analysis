-- -------------------------------------------
-- create database instacart_market first then run these queries in instacart_market
-- -------------------------------------------

-- STEP 1: CREATE TABLES
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    eval_set TEXT,
    order_number INTEGER,
    order_dow INTEGER,
    order_hour_of_day INTEGER,
    days_since_prior_order NUMERIC
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    aisle_id INTEGER,
    department_id INTEGER
);

CREATE TABLE IF NOT EXISTS aisles (
    aisle_id INTEGER PRIMARY KEY,
    aisle TEXT
);

CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department TEXT
);

CREATE TABLE IF NOT EXISTS order_products_prior (
    order_id INTEGER,
    product_id INTEGER,
    add_to_cart_order INTEGER,
    reordered INTEGER
);

CREATE TABLE IF NOT EXISTS order_products_train (
    order_id INTEGER,
    product_id INTEGER,
    add_to_cart_order INTEGER,
    reordered INTEGER
);

-- ============================================
-- STEP 2: LOAD DATA (COPY commands)
-- ============================================

COPY orders
FROM 'D:/instacart_market_analysis/orders.csv'
DELIMITER ','
CSV HEADER;

COPY products
FROM 'D:/instacart_market_analysis/products.csv'
DELIMITER ','
CSV HEADER;

COPY aisles
FROM 'D:/instacart_market_analysis/aisles.csv'
DELIMITER ','
CSV HEADER;

COPY departments
FROM 'D:/instacart_market_analysis/departments.csv'
DELIMITER ','
CSV HEADER;

COPY order_products_prior
FROM 'D:/instacart_market_analysis/order_products__prior.csv'
DELIMITER ','
CSV HEADER;

COPY order_products_train
FROM 'D:/instacart_market_analysis/order_products__train.csv'
DELIMITER ','
CSV HEADER;
