# Answers to DB Assignment

Q.1 Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

The above diagram of table product_category and product along with their data types, it appears to represent a classic one-to-many relationship between Product_Category and Product.


Q. 2 How could you ensure that each product in the "Product" table has a valid category assigned to it?

To ensure that each product in the "Product" table has a valid category assigned to it, I used a foreign key constraint. The foreign key constraint will enforce referential integrity, ensuring that the values in the "category_id" column of the "Product" table match the values in the "id" column of the "Category" table.

-- Create the product_category table
CREATE TABLE product_category (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    desc TEXT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

-- Create the product table with a foreign key constraint
CREATE TABLE product (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    desc TEXT,
    SKU VARCHAR(255),
    quantity INT,
    category_id INT,
    inventory_id INT,
    modified_at TIMESTAMP,
    price DECIMAL,
    deleted_at TIMESTAMP,
    discount_id INT,
    created_at TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_category(id)
);
By setting up this foreign key constraint, I prevented the insertion of products with non-existent or invalid category IDs, maintaining the integrity of the relationship between the "Product" and "Product_Category" tables.