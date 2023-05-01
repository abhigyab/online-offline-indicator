from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

kv_url = 'https://kv-innercirclerecommend.vault.azure.net/'

credential = DefaultAzureCredential()
client = SecretClient(vault_url=kv_url, credential=credential)


def get_secret_value(secret_name):
    """
    Function to retrieve the secret value for a key

    Args:
        secret_name     (str)   : Name of the secret account

    Returns:
        secret_value    (str)   : Value of the associated secret account
    """
    retrieved_secret = client.get_secret(secret_name)
    secret_value = retrieved_secret.value

    return secret_value
