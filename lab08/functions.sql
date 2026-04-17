CREATE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, surname, phone
    FROM phonebook
    WHERE name LIKE '%' || pattern || '%'
       OR surname LIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION get_phonebook_page(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, surname, phone
    FROM phonebook
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;