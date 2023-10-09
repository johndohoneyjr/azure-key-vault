from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.storage.blob import BlobServiceClient
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import msal
import os
from azure.identity import ClientSecretCredential

from cryptography.fernet import Fernet

key = Fernet.

# Azure setup
key_vault_name = '<your-key-vault-name>'
key_name = 'blogdata'
storage_account_name = 'dohoneystorage'
container_name = 'blogdata'
blob_name = 'mflix.json'
file_path = 'mflix.json'

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
tenant_id = os.environ['TENANT_ID']

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Download the key from Azure Key Vault
kv_uri = "https://my-by-demo-kv.vault.azure.net/"
key_client = KeyClient(vault_url=kv_uri, credential=credential)
key = key_client.get_key(key_name)

# Read the file and encrypt it
with open(file_path, 'rb') as file:
    plaintext = file.read()
key.
ciphertext = key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Upload the encrypted data to Azure Blob Storage
blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net", credential=credential)
blob_client = blob_service_client.get_blob_client(container_name, blob_name)

blob_client.upload_blob(ciphertext)
