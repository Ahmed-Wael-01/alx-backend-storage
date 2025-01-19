-- email validation
CREATE TRIGGER email_vali
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = 0 WHERE NEW.email <> OLD.email;
