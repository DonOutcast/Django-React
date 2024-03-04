import os


def os_getenv(key: str, default: str = None) -> str:
    env_value = os.getenv(key, default)
    if env_value == "":
        print(f"Environment variable '{key}' is set to empty string. Using default value '{default}'")
        env_value = default
    return env_value
