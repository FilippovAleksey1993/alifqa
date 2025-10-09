def validate_phone_number(phone):
    return phone.startswith('998') and len(phone) == 12

def get_first_product_name(response_json):
    if response_json.get('variations') and len(response_json['variations']) > 0:
        return response_json['variations'][0]['variation']['productName']
    return None

def get_first_product_id(response_json):
    if response_json.get('variations') and len(response_json['variations']) > 0:
        return response_json['variations'][0]['variation']['id']
    return None