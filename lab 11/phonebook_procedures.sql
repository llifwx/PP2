
-- 1. Функция поиска по шаблону (с алиасом таблицы)
CREATE OR REPLACE FUNCTION search_contacts_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone FROM contacts c
    WHERE c.first_name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Процедура добавления/обновления одного пользователя
CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts c WHERE c.first_name = name) THEN
        UPDATE contacts c SET phone = phone WHERE c.first_name = name;
    ELSE
        INSERT INTO contacts(first_name, phone) VALUES (name, phone);
    END IF;
END;
$$;

-- 3. Процедура массовой вставки с проверкой валидности телефона
CREATE OR REPLACE PROCEDURE insert_many_users(users TEXT[][], OUT invalid_entries TEXT[][])
LANGUAGE plpgsql AS $$
DECLARE
    name TEXT;
    phone TEXT;
    temp TEXT[] := '{}';
BEGIN
    invalid_entries := ARRAY[]::TEXT[][];
    FOREACH temp SLICE 1 IN ARRAY users
    LOOP
        name := temp[1];
        phone := temp[2];
        IF phone ~ '^\+?[0-9]{7,15}$' THEN
            CALL insert_or_update_user(name, phone);
        ELSE
            invalid_entries := array_append(invalid_entries, ARRAY[name, phone]);
        END IF;
    END LOOP;
END;
$$;

-- 4. Функция пагинации (с алиасом таблицы)
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, offs INT)
RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone FROM contacts c
    ORDER BY c.id
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;

-- 5. Процедура удаления по имени или телефону (с алиасом)
CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts c
    WHERE c.first_name = identifier OR c.phone = identifier;
END;
$$;
