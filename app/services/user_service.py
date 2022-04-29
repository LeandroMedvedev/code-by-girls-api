def check_user_data(data: dict):
    received_keys = set(data.keys())
    valid_keys = {"name", "email", "password"}
    invalid_keys = received_keys.difference(valid_keys)

    return received_keys, valid_keys, invalid_keys

def check_mandatory_keys(data: dict):
    received_keys = set(data.keys())

    if "password" not in received_keys:
        return True
    if "name" not in received_keys:
        return True
    if "email" not in received_keys:
        return True
    
    return False

def normalize_data(data: dict):
    data["email"] = data["email"].lower()
    data["name"] = data["name"].title()

    return data

def check_value_type(data):
    wrong_values = []
    for value in data.values():
        if type(value) != str :
            wrong_values.append(value)
    return len(wrong_values)