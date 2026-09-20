# USER PROFILE 

# in witch string concept is most time is used

name="  vishesh unadkat  "
# email="VISHESHUNADKAT@GMAIL.COM"
email=input("enter your email")
username="vishesh123"
bio = "AI/ML enthusiast, Python developer, RAG learner"

# validate a email

def validate_email():
    """
    this function is for validate user email 
    """

    user_email=email.strip().lower()
    print(user_email)

    if "@" not in user_email:
        print("Invalid Email:email do not have @")

    if user_email.startswith("@"):
        print("Invalid Email : email do not start with @")

    if user_email.endswith("@"):
        print("Invalid Email : email do not end with @")        


validate_email()
