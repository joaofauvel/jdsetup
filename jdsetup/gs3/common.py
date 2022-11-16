from uuid import uuid4


def fmt_uuid4() -> str:
    return f'{{{str(uuid4())}}}'