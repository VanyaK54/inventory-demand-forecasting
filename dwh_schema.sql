-- Inventory Demand Forecasting Data Warehouse Schema

-- 1. DimWarehouse
CREATE TABLE DimWarehouse (
    warehouse_id INT PRIMARY KEY,
    warehouse_name VARCHAR(100),
    location VARCHAR(100)
);

-- 2. DimProduct
CREATE TABLE DimProduct (
    product_id INT PRIMARY KEY,
    product_code VARCHAR(50),
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- 3. DimDate
CREATE TABLE DimDate (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    day_of_week INT,
    is_weekend BIT,
    is_holiday BIT
);

-- 4. FactInventory
CREATE TABLE FactInventory (
    inventory_id INT PRIMARY KEY IDENTITY(1,1),
    date_id DATE,
    warehouse_id INT,
    product_id INT,
    units_sold INT,
    stock_level INT,
    temperature FLOAT,
    precipitation FLOAT,
    FOREIGN KEY (date_id) REFERENCES DimDate(date_id),
    FOREIGN KEY (warehouse_id) REFERENCES DimWarehouse(warehouse_id),
    FOREIGN KEY (product_id) REFERENCES DimProduct(product_id)
);
