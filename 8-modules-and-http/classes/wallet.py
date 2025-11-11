from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import binascii

# The idea of this class is to create a private wallet to verify all transactions on your network
# It will hold a private key for transactions and a public one (related to the private one) for verifications
class Wallet:
  def __init__(self):
    self.private_key = None
    self.public_key = None

  def create_keys(self):
    private_key, public_key = self.generate_keys()
    self.private_key = private_key
    self.public_key = public_key

    with open('wallet.txt', mode='w') as wf:
      wf.write(public_key)
      wf.write('/n')
      wf.write(private_key)

  def save_keys(self):
    if self.private_key != None and self.public_key != None:
      try:
        with open('wallet.txt', mode='w') as wf:
          wf.write(self.public_key)
          wf.write('\n')
          wf.write(self.private_key)
          
          return True
      except (IOError, IndexError):
        print('Error saving wallet...')
        return False

  def load_keys(self):
    with open('wallet.txt', mode='r') as wf:
      # A try/catch logic that handles the wallet keys and catches any comming error
      try:
        keys = wf.readlines()
        # On this line you are reading the whole line, including the line jump (/n)
        # To remove that line, you select the whole copy of the list except the last item (the line jump)
        public_key = keys[0][:-1]
        private_key = keys[1]
        self.public_key = public_key
        self.private_key = private_key

        return True
      except (IOError, IndexError):
        print('Error loading wallet...')
        return False

  def generate_keys(self):
    # On this part, you create a key generating an RSA key with
    # 1024 bits of lenght and a random number (which is read from the Crypto library)
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    
    # To return such keys, first you have to parse them from its original binary
    # to a ascii-compatible and readable string
    return (
      binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
      binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    )

  def sign_transaction(self, sender, recipient, amount):
      """Sign a transaction and return the signature.

      Arguments:
          :sender: The sender of the transaction.
          :recipient: The recipient of the transaction.
          :amount: The amount of the transaction.
      """
      signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key)))
      h = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8'))
      signature = signer.sign(h)
      return binascii.hexlify(signature).decode('ascii')

  @staticmethod
  def verify_transaction(transaction):
      """Verify the signature of a transaction.

      Arguments:
          :transaction: The transaction that should be verified.
      """
      public_key = RSA.importKey(binascii.unhexlify(transaction.sender))
      verifier = PKCS1_v1_5.new(public_key)
      h = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
      return verifier.verify(h, binascii.unhexlify(transaction.signature))