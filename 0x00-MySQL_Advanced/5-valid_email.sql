-- create trigger that resets valid email field when email is changed
DELIMETER $$$
CREATE TRIGGER `resetvalidemail` BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN
    SET NEW.valid_email = 0;
END IF;
END
$$$
DELIMETER ;