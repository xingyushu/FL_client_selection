import random

# Define total number of clients, total bandwidth and power constraints
num_clients = 3000
B = 1000
P = 100

# Generate a list of clients with random values for ID, bandwidth, power, and SNR
client_list = []
for i in range(num_clients):
    client = {
        'id': i,
        'bandwidth': random.randint(1, B),
        'power': random.randint(1, P),
        'snr': random.uniform(1, 10)
    }
    client_list.append(client)

# Sort the client list by SNR in descending order
client_list.sort(key=lambda x: x['snr'], reverse=True)

# Initialize a list to store the selected clients
selected_clients = []

# Initialize variables to store the total bandwidth and power
total_bandwidth = 0
total_power = 0

# Iterate through the client list
for client in client_list:
    # Check if the client satisfies the bandwidth and power constraints
    if total_bandwidth + client['bandwidth'] <= B and total_power + client['power'] <= P:
        # Add the client to the list of selected clients
        selected_clients.append(client)
        total_bandwidth += client['bandwidth']
        total_power += client['power']
    if len(selected_clients) == 10:
        break

# Compute the total SNR of the selected clients
total_snr = sum([client['snr'] for client in selected_clients])

print("Selected clients:", selected_clients)
print("Total SNR:", total_snr)
