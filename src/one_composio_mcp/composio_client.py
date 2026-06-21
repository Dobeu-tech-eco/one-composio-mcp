from composio import Composio


def build_composio_client(api_key: str) -> Composio:
    return Composio(api_key=api_key)
