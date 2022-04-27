SELECT SalesPerson.name FROM Orders
JOIN Company ON (Orders.com_id = Company.com_id and Company.name='RED') 
RIGHT JOIN SalesPerson ON (SalesPerson.sales_id = Orders.sales_id)
WHERE Orders.sales_id IS NULL