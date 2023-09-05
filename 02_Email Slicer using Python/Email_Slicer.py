def email_slicer():
    print("Welcome to Email Slicer")

    email = input("Please Enter your Email: ")

    (username , domain) = email.split("@")
    (domain , extention) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extention)


email_slicer()