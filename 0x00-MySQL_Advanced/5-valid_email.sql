-- email validation
CREATE TRIGGER email_vali
BEFORE UPDATE ON users
FOR EACH ROW
IF NEW.email <> OLD.email THEN SET NEW.valid_email = 0;
