"""Run the XP backend server"""
import subprocess, sys, os

print("Starting XP Backend Server on http://127.0.0.1:8000")
proc = subprocess.Popen(
    [sys.executable, '-m', 'uvicorn', 'main:app', '--host', '127.0.0.1', '--port', '8000', '--reload'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
for line in iter(proc.stdout.readline, b''):
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
