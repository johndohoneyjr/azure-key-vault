from datetime import datetime, timedelta
from pickletools import pybytes
from azure.identity import ClientSecretCredential
from azure.keyvault.certificates import CertificateClient, CertificatePolicy, WellKnownIssuerNames
from cryptography.hazmat.backends import default_backend
import msal
import os
from cryptography import x509

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
tenant_id = os.environ['TENANT_ID']

credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Upload the certificate to Azure Key Vault
kv_uri = "https://my-by-demo-kv.vault.azure.net/"
client = CertificateClient(vault_url=kv_uri, credential=credential)
certificateName = input("Input a name for your certificate > ")
keyVaultName="my-by-demo-kv"
print(f"Creating a certificate in {keyVaultName} called '{certificateName}' ...")

policy = CertificatePolicy.get_default()
poller = client.begin_create_certificate(certificate_name=certificateName, policy=policy)
certificate = poller.result()

print(f"Retrieving your certificate from {keyVaultName}.")

retrieved_certificate = client.get_certificate(certificateName)

print(retrieved_certificate.cer)    


print(" done.")