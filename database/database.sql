CREATE DATABASE IF NOT EXISTS bluestocks;
USE bluestocks;

CREATE TABLE IF NOT EXISTS ml (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id VARCHAR(50) UNIQUE,
    company_name VARCHAR(100),
    roe FLOAT,
    roce FLOAT,
    net_profit FLOAT,
    pros TEXT,
    cons TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
