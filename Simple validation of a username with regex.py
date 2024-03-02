import re
def validate_usr(username):
    return bool(re.fullmatch(r'[a-z0-9_]{4,16}', username))




validate_usr('asddsa')
validate_usr('a')
validate_usr('Hass')
validate_usr('Hasd_12assssssasasasasasaasasasasas')
validate_usr('')