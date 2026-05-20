ROLE_PERMISSIONS = {
    "ADMIN": ["CREATE", "UPDATE", "DELETE", "ROLLBACK"],
    "EDITOR": ["CREATE", "UPDATE"],
    "VIEWER": ["READ"]
}

def validate_permission(role, action):

    permissions = ROLE_PERMISSIONS.get(role, [])

    return action in permissions
