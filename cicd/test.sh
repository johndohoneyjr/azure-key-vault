#! /bin/bash

az login --service-principal --username ...

az group create --name mytest-john --location eastus

az acr create -n johnldregistry -g uci-blue-rg --sku Standard

# Create a secret in the keyvault

az keyvault secret set --vault-name xxx --name "mySecret" --value "myPassword"

# Create a certificate in the keyvault

az keyvault certificate create --vault-name xxx --name myCert --policy "$(az keyvault certificate get-default-policy)"
