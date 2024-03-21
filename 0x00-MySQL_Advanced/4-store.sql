-- create a trigger that decreases quantity of an item in items table after adding a row to the orders table
CREATE TRIGGER `decreaseorders` AFTER INSERT ON `orders`
    FOR EACH ROW
    UPDATE `items` SET quantity = quantity - NEW.number
    WHERE `name` = NEW.item_name;
