import cbpro
from cmd.run.secret import API_KEY
from cmd.run.secret import PASS_PHRASE
from cmd.run.secret import B64_SECRET


auth_client = cbpro.AuthenticatedClient(API_KEY, B64_SECRET, PASS_PHRASE)
print(auth_client.get_accounts())