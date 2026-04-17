from phonebook import execute_function, execute_procedure

pattern = "John"
result = execute_function("search_phonebook", [pattern])
print(result)

execute_procedure("add_or_update_user", ["Alice", "1234567890"])

users = ["John,1234567890", "Jane,0987654321"]
execute_procedure("add_multiple_users", [users])