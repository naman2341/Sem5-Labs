CREATE OR REPLACE TRIGGER Validate_Employee BEFORE INSERT OR UPDATE ON EMPLOYEE
FOR EACH ROW
BEGIN
IF LOWER(:NEW.role) != 'cashier' OR LOWER(:NEW.role != 'pharmacist') OR LOWER(:NEW.role != 'cpht') OR
LOWER(:NEW.role != 'intern') THEN
RAISE_APPLICATION_ERROR(-20000, 'Invalid role given for employee');
END IF;
IF :NEW.license := NULL AND LOWER(:new.role) != 'cashier' THEN
RAISE_APPLICATION_ERROR(-20000, 'Can not leave license blank for anyone except cashiers'); END IF;
END;