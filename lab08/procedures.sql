CREATE PROCEDURE add_or_update_user(new_name TEXT, new_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = new_name) THEN
        UPDATE phonebook
        SET phone = new_phone
        WHERE name = new_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (new_name, new_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE PROCEDURE add_multiple_users(user_data TEXT[])
AS $$
DECLARE
    user_record TEXT;
    user_name TEXT;
    user_phone TEXT;
BEGIN
    FOR user_record IN SELECT unnest(user_data)
    LOOP
        user_name := split_part(user_record, ',', 1);
        user_phone := split_part(user_record, ',', 2);
        IF length(user_phone) = 10 THEN
            INSERT INTO phonebook(name, phone)
            VALUES (user_name, user_phone);
        ELSE
            RAISE NOTICE 'Некорректный номер телефона для пользователя: %', user_name;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;