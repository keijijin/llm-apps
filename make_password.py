import streamlit_authenticator as stauth

def hash_password(password):
    return stauth.Hasher([password]).generate()[0]

if __name__ == "__main__":
    password = input("Enter the password to hash: ")
    hashed_password = hash_password(password)
    print("Hashed password: ", hashed_password)