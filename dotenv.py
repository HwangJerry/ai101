import os

def load_dotenv():
    with open(".env", "r") as f:
        file = f.read()
        lines = file.split("\n")
        for l in lines:
            l.strip()
            if l.startswith("#"):
                continue
            k, v = l.split("=")
            os.environ[k] = v

