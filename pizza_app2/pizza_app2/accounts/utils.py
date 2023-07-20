def get_full_name(obj):
    first_name = obj.first_name if obj.first_name else ''
    last_name = obj.last_name if obj.last_name else ''

    if first_name or last_name:
        return f"{first_name} {last_name}"
    return None
