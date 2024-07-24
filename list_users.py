import subprocess

def list_users():
    try:
        result = subprocess.run(['lastlog'], stdout=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running lastlog: {e}")
        return None

def main():
    users = list_users()
    if users:
        print(users)

if __name__ == "__main__":
    main()
