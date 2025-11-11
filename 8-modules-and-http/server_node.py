from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from classes.wallet import Wallet
from classes.blockchain import Blockchain

# Is telling in what context is running Flask
# If you start the proyect from this file, __name__ will be '__main__'
# Otherwise, it will the name of the file you assigned this line
server_app = Flask(__name__)
server_wallet = Wallet()
server_blockchain = Blockchain(server_wallet.public_key)
# This will make our server open to outside callings
CORS(server_app)

@server_app.route('/', methods=['GET'])
def get_ui():
  return send_from_directory('ui', 'node.html')

# Each route is referenced to the created Flask ([server_app] variable)
# Its first argument is related to the route we are opening to the public
# The second one is a definition of the approved HTTP methods to call this route
@server_app.route('/wallet', methods=['POST'])
def create_keys():
  server_wallet.create_keys()

  if server_wallet.save_keys():
    global server_blockchain

    server_blockchain = Blockchain(server_wallet.public_key)
    correct_response = {
      'public_key': server_wallet.public_key,
      'private_key': server_wallet.private_key,
      'funds': server_blockchain.get_balance()
    }
    
    # EVERY response must be parsed into JSON
    # Flask facilitates it with jsonify, which asks for the argument to parse
    # Alongside with the parsed response, you can add a HTTP response as the next argument
    return jsonify(correct_response), 201
  else:
    error_response = { 'message': 'Saving the keys failed' }
    return jsonify(error_response), 500

@server_app.route('/wallet', methods=['GET'])
def load_keys():
  if server_wallet.load_keys():
    global server_blockchain

    server_blockchain = Blockchain(server_wallet.public_key)
    correct_response = {
      'public_key': server_wallet.public_key,
      'private_key': server_wallet.private_key,
      'funds': server_blockchain.get_balance()
    }
    
    return jsonify(correct_response), 201
  else:
    error_response = { 'message': 'Loading the keys failed' }
    return jsonify(error_response), 500
  
@server_app.route('/transactions', methods=['GET'])
def get_open_transactions():
  server_transactions = server_blockchain.get_open_transactions()
  dict_transactions = [tx.__dict__ for tx in server_transactions]
  return jsonify(dict_transactions), 200
  
@server_app.route('/transaction', methods=['POST'])
def add_transaction():
  if server_wallet.public_key == None:
    error_response = { 'message': 'No wallet set up' }
    return jsonify(error_response), 400
  
  values = request.get_json()

  if not values:
    error_response = { 'message': 'No data found' }
    return jsonify(error_response), 400
  
  required_values = ['recipient', 'amount']
  
  if not all(field in values for field in required_values):
    error_response = { 'message': 'Required data is missing' }
    return jsonify(error_response), 400
  
  recipient = values['recipient']
  amount = values['amount']
  signature = server_wallet.sign_transaction(
    server_wallet.public_key,
    recipient,
    amount
  )

  success_transaction = server_blockchain.add_transaction(
    recipient,
    server_wallet.public_key,
    signature,
    amount)
  
  if success_transaction:
    success_response = {
      'message': 'Creating a transaction success',
      'transaction': {
        'recipient': recipient,
        'amount': amount,
        'signature': signature
      },
      'funds': server_blockchain.get_balance()
    }
    return jsonify(success_response), 201
  else:
    error_response = { 'message': 'Creating a transaction failed' }
    return jsonify(error_response), 500


@server_app.route('/mine', methods=['POST'])
def mine():
  mined_block = server_blockchain.mine_block()
    
  if mined_block != None:
    dict_mined_block = mined_block.__dict__.copy()
    dict_mined_block['transactions'] = [mined_tx.__dict__ for mined_tx in dict_mined_block['transactions']]
    
    success_response = {
      'message': 'Block added successfully',
      'block': dict_mined_block,
      'funds': server_blockchain.get_balance()
    }

    return jsonify(success_response), 201
  else:
    error_response = {
      'message': 'Adding a block failed',
      'wallet_set_up': server_wallet.public_key != None
    }

    return jsonify(error_response), 500

@server_app.route('/chain', methods={'GET'})
def get_chain():
  blockchain_snapshot = server_blockchain.chain
  dict_snapshot = [block.__dict__.copy() for block in blockchain_snapshot]
  
  for dict_block_snapshot in dict_snapshot:
    dict_block_snapshot['transactions'] = [tx.__dict__ for tx in dict_block_snapshot['transactions']]
  
  return jsonify(dict_snapshot), 200

@server_app.route('/balance', methods=['GET'])
def get_balance():
  balance = server_blockchain.get_balance()

  if balance != None:
    success_response = {
      'message': 'Fetched balance successfully',
      'funds': balance
    }

    return jsonify(success_response), 200
  else:
    error_response = {
      'message': 'Loading balance failed',
      'wallet_set_up': server_wallet.public_key != None
    }

    return jsonify(error_response), 500
  
@server_app.route('/node', methods=['POST'])
def add_node():
  form_values = request.get_json()

  if not form_values:
    error_message = { 'message': 'No data attached' }
    return jsonify(error_message), 400
  print(form_values)
  if 'node' not in form_values:
    error_message = { 'message': 'No node data founded' }
    return jsonify(error_message), 400
  
  node_value = form_values['node']
  server_blockchain.add_peer_node(node_value)

  success_response = {
    'message': 'Node added successfully',
    'all_nodes': server_blockchain.get_all_nodes()
  }
  return jsonify(success_response), 201

@server_app.route('/node/<node_url>', methods=['DELETE'])
def remove_node(node_url):
  if node_url == '' or node_url == None:
    error_response = { 'message': 'No node url provided' }
    return jsonify(error_response), 400
  
  server_blockchain.remove_peer_node(node_url)
  success_response = {
    'message': 'Node removed',
    'all_nodes': server_blockchain.get_all_nodes()
  }
  return jsonify(success_response), 200

@server_app.route('/nodes', methods=['GET'])
def get_nodes():
  nodes_response = { 'all_nodes': server_blockchain.get_all_nodes() }
  return jsonify(nodes_response), 200


# At the bottom of the file, you can run the API if the program is beign run
# from this file (which will give the __name__ variable the name __main__)
# If not, __name__ will be asigned file's name as its value
if __name__ == '__main__':
  server_app.run(host='0.0.0.0', port=5060)