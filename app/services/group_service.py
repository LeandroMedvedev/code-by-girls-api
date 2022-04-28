def check_data(data: dict):
    received_keys = set(data.keys())
    valid_keys = {"name", "description"}
    invalid_keys = received_keys.difference(valid_keys)

    return received_keys, valid_keys, invalid_keys
