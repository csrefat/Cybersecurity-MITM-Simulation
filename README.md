# Cybersecurity MITM Attack Simulation

A Python-based simulation demonstrating a **Modification of Messages** Man-in-the-Middle (MITM) attack using TCP sockets.

## 🎬 Demonstration Video
Watch the full MITM attack simulation video here: https://youtu.be/PXPfYpV0fyo

## 📁 Files Included
- `server.py` - TCP Server script receiving messages.
- `client.py` - TCP Client script sending messages.
- `attack.py` - MITM Proxy script intercepting and modifying messages in real time.

## 🚀 How to Run
1. Start Server: `python3 server.py`
2. Start Interceptor: `python3 attack.py`
3. Start Client: `python3 client.py`
