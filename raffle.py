import requests


# Get the list of all delegators
# IMPORTANT: Get list timely after the epoch change and save it so that the correctness 
# of the list is assured.
headers = {
    'authority': 'adastat.net',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'accept': '*/*',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://adastat.net/pools/e6ac159ee8063742eadcb48be45f29d9a67b4158439070032f42d10c',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('t', '1638272309265'),
)

response = requests.get('https://adastat.net/rest/v0/pool/3d2294baebe5bbeaa920af59e8461068582bb6c17522bbc7308e8567.json', headers=headers, params=params)

json_response = response.json()

# make sure 
participants_e305=json_response['delegators']

number_participants=len(participants_e305)

# enter the latest epoch nonce earliest 1.5 days prior to the snapshot available
epoch_nonce305 = '0940fcab1de3b3f60bb8f6b57eb9d7139a6d23be07f5fdaa9b9b067df7039945' 
print('Epoch nonce:', epoch_nonce305)


# conversion to decimal
dec = int(epoch_nonce305, 16)

#the number of the winner is determined by the modulo of the decimal epoch nonce and the number of participating delegators.
# 1st place 150 ADA
place_1 = (dec)%number_participants

# 2nd place 100 ADA
place_2 = (dec+dec)%number_participants

# 3rd place 50 ADA
place_3 = (dec+dec+dec)%number_participants

winner1=json_response['delegators'][place_1]
winner2=json_response['delegators'][place_2]
winner3=json_response['delegators'][place_3]


print(f"{number_participants} delegators have participated: \n")

print('1st place: ',winner1[0], "wins 150 ADA")
print('2nd place: ',winner2[0], "wins 100 ADA")
print('3rd place: ',winner3[0], "wins 50 ADA")
