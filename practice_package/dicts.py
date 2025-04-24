def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result

def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            if not isinstance(inverted[value], list):
                inverted[value] = [inverted[value]]
            inverted[value].append(key)
        else:
            inverted[value] = key  
    for key in inverted:
        if not isinstance(inverted[key], list):
            inverted[key] = [inverted[key]]
    return inverted

def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""
    
    headers = [col.upper() for col in columns]
    max_lengths = {col: len(header) for col, header in zip(columns, headers)}
    
    all_rows = []
    for item in data_dict.values():
        row = []
        for col in columns:
            val = str(item.get(col, "N/A"))
            max_lengths[col] = max(max_lengths[col], len(val))
            row.append(val)
        all_rows.append(row)
    
    header_parts = []
    for col, header in zip(columns, headers):
        header_parts.append(f" {header:<{max_lengths[col]}} ")
    header_row = "|" + "|".join(header_parts) + "|"
    
    separator_parts = []
    for col in columns:
        separator_parts.append("-" * (max_lengths[col] + 2))
    separator = "|" + "|".join(separator_parts) + "|"
    
    formatted_rows = []
    for row in all_rows:
        row_parts = []
        for col, cell in zip(columns, row):
            row_parts.append(f" {cell:<{max_lengths[col]}} ")
        formatted_rows.append("|" + "|".join(row_parts) + "|")
    
    return "\n".join([header_row, separator] + formatted_rows)

def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_update(result[key], value)
            else:
                result[key] = value
    return result