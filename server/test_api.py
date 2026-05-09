"""Test all API endpoints"""
import subprocess, time, sys, os

# Start uvicorn in a subprocess
proc = subprocess.Popen(
    [sys.executable, '-m', 'uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '8000', '--log-level', 'error'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)
time.sleep(4)

results = []
try:
    import requests
    
    tests = [
        ('GET', '/health', None),
        ('GET', '/api/products', None),
        ('GET', '/api/parts', None),
        ('GET', '/api/communities', None),
        ('GET', '/api/users', None),
        ('POST', '/api/auth/login', {'email': 'admin@xp.game', 'password': 'admin123'}),
        ('POST', '/api/ai/recommend', {'budget': 1500, 'use_case': 'gaming'}),
        ('POST', '/api/ai/compatibility', {'parts': [{'category': 'CPU', 'name': 'Intel i7', 'power_consumption': 253}, {'category': 'GPU', 'name': 'RTX 4090', 'power_consumption': 450}, {'category': 'PSU', 'name': '850W', 'power_consumption': 850}]}),
        ('GET', '/api/favorites', None, 'admin_token'),
    ]
    
    # Get auth token first
    r = requests.post('http://127.0.0.1:8000/api/auth/login', json={'email': 'admin@xp.game', 'password': 'admin123'}, timeout=5)
    admin_token = r.json().get('access_token', '')
    results.append(f"[{r.status_code}] /api/auth/login -> {list(r.json().keys())}")
    
    for method, path, body in tests:
        try:
            headers = {}
            if 'admin_token' in str(tests) and admin_token:
                headers['Authorization'] = f'Bearer {admin_token}'
            
            if method == 'GET':
                r = requests.get(f'http://127.0.0.1:8000{path}', headers=headers, timeout=5)
            else:
                r = requests.post(f'http://127.0.0.1:8000{path}', json=body or {}, headers=headers, timeout=5)
            
            data = r.json()
            if isinstance(data, dict):
                summary = str(list(data.keys())[:3])
                if 'products' in data:
                    summary = f"products={len(data['products'])}"
                elif 'parts' in data:
                    summary = f"parts={len(data['parts'])}"
                elif 'communities' in data:
                    summary = f"communities={len(data['communities'])}"
                elif 'users' in data:
                    summary = f"users={len(data['users'])}"
            else:
                summary = 'ok'
            results.append(f"[{r.status_code}] {path} -> {summary}")
        except Exception as e:
            results.append(f"[ERR] {path} -> {e}")

except Exception as e:
    results.append(f"Setup error: {e}")
finally:
    proc.terminate()
    proc.wait()

# Write results
with open('test_results.txt', 'w') as f:
    f.write('\n'.join(results))
print('\n'.join(results))
print("\nTests written to test_results.txt")
