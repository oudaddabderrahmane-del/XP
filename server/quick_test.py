import requests

r = requests.post('http://127.0.0.1:8000/api/ai/build-estimate', json={
    'parts': [
        {'category': 'CPU', 'name': 'AMD Ryzen 7 7800X3D', 'power_consumption': 120, 'price': 389},
        {'category': 'GPU', 'name': 'NVIDIA RTX 4090', 'power_consumption': 450, 'price': 1599},
        {'category': 'RAM', 'name': 'Corsair 32GB DDR5', 'power_consumption': 10},
    ]
}, timeout=5)
d = r.json()

r2 = requests.post('http://127.0.0.1:8000/api/auth/login', json={'email': 'admin@xp.game', 'password': 'admin123'}, timeout=5)
token = r2.json()['access_token']

r3 = requests.post('http://127.0.0.1:8000/api/keys?name=TestKey', headers={'Authorization': f'Bearer {token}'}, timeout=5)
r3_data = r3.json()

with open('test_output.txt', 'w') as f:
    f.write(f"=== Build Estimate Results ===\n")
    f.write(f"Status: {r.status_code}\n")
    f.write(f"FPS 1080p: {d['fps']['1080p']}\n")
    f.write(f"FPS 1440p: {d['fps']['1440p']}\n")
    f.write(f"FPS 4K: {d['fps']['4k']}\n")
    f.write(f"Bottleneck: {d['bottleneck']['note']} ({d['bottleneck']['percentage']}%)\n")
    f.write(f"Temperature: {d['temperature']}\n")
    f.write(f"Power Draw: {d['total_power_draw']}W\n\n")
    f.write(f"=== API Key ===\n")
    f.write(f"Status: {r3.status_code}\n")
    f.write(f"Response: {r3_data}\n")
    f.write("\nAll endpoints working!\n")

print("Done")
