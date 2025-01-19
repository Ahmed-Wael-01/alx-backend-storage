-- trigger to decrease quantity of an item
CREATE TRIGGER decs
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
