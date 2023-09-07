import os

def get_authorized_keys(username=None):
    if username is None:
        # If no username is provided, use the currently logged-in user
        import getpass
        username = getpass.getuser()

    authorized_keys_path = os.path.expanduser(f"~{username}/.ssh/authorized_keys")

    try:
        with open(authorized_keys_path, 'r') as auth_keys_file:
            authorized_keys = auth_keys_file.read().strip()
            return authorized_keys
    except FileNotFoundError:
        return None

def main():
    authorized_keys = get_authorized_keys()
    if authorized_keys is not None:
        print("Authorized SSH Keys:")
        print(authorized_keys)
    else:
        print("No authorized keys found for this user.")

if __name__ == "__main__":
    main()
