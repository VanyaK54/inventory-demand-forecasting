CREATE TABLE Inventory (
    id INT PRIMARY KEY,
    date DATE,
    warehouse_id INT,
    product_id INT,
    units_sold INT,
    stock_level INT
);

CREATE TABLE Weather (
    date DATE,
    location VARCHAR(50),
    temperature FLOAT,
    precipitation FLOAT
);

CREATE TABLE Holidays (
    date DATE PRIMARY KEY,
    name VARCHAR(100),
    region VARCHAR(50)
);
