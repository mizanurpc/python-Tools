import random, secrets, string

random.seed(42)
print(random.randint(0, 999999))  # same number every run!

token = secrets.token_urlsafe(32)  # session / reset tokens
otp = f"{secrets.randbelow(10**6):06d}"

alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(secrets.choice(alphabet) for _ in range(16))
print(token, otp, password, sep="\n")

user_supplied_token = token  

# timing-safe comparison of secrets
result = secrets.compare_digest(token, user_supplied_token)
print("Token match:", result)
