#! /bin/bash

az login --service-principal --username ...

az group create --name mytest-john --location eastus

az acr create -n johnldregistry -g uci-blue-yonder-rg --sku Standard

az acr delete -n johnldregistry -g uci-blue-yonder-rg

# Create a secret in the keyvault

az keyvault secret set --vault-name uci9267d3 --name "mySecret" --value "myPassword"

# Create a certificate in the keyvault

az keyvault certificate create --vault-name uci9267d3 --name myCert --policy "$(az keyvault certificate get-default-policy)"
