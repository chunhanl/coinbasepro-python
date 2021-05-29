import cbpro

public_client = cbpro.PublicClient()
print(public_client.get_products())
print(public_client.get_time())