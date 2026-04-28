-- Процедура добавления телефона к контакту
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phones (contact_id, phone, type)
    SELECT id, p_phone, p_type FROM contacts WHERE name = p_name;
END; $$;

-- Процедура перемещения в группу
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE g_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group) ON CONFLICT DO NOTHING;
    SELECT id INTO g_id FROM groups WHERE name = p_group;
    UPDATE contacts SET group_id = g_id WHERE name = p_name;
END; $$;