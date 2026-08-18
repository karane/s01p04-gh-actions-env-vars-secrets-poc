import os


def get_required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise KeyError(f"missing required env var: {name}")
    return value


def mask(value: str, visible: int = 4) -> str:
    if len(value) <= visible:
        return "*" * len(value)
    return value[:visible] + "*" * (len(value) - visible)


def build_connection_label(env_name: str, region: str) -> str:
    return f"{env_name}-{region}"
