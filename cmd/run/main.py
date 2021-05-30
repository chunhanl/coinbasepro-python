import cbpro
from secret import API_KEY, PASS_PHRASE, B64_SECRET


auth_client = cbpro.AuthenticatedClient(API_KEY, B64_SECRET, PASS_PHRASE)
print(auth_client.get_accounts())