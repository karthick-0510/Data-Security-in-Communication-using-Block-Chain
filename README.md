# 🛰️ Secure Satellite Communication using Blockchain & QKD Protocol

## 🌐 Overview

Satellite communication plays a vital role in developing **global communication networks**. It has gained traction as an effective alternative to terrestrial networks, which often face issues like limited coverage and stability.

However, satellite networks encounter significant challenges:
- 🧠 Low data processing capacity  
- 💾 Limited storage  
- 🔓 Weak security infrastructure  
- 🚨 Illegal access and intrusion risks  

To tackle these issues, this project proposes a **secure satellite communication framework** using:

- 🔗 **Blockchain Technology** for tamper-proof logging  
- 🧬 **Quantum Key Distribution (QKD)** for secure authentication and encryption  

---

## 🏗️ Architecture

This project incorporates:
- 🛰️ **Satellites** with constrained resources (limited power and space)  
- 📡 **Terrestrial base stations**  
- 📶 A **wireless heterogeneous network**  
- 📲 Both **traditional and resource-constrained devices**

---

## 🔐 Core Features

1. 👥 **User & Device Registration**  
2. ✅ **Authentication using MAC address and QKD-simulated hashing**  
3. 🛑 **Revocation of rogue devices**  
4. 🧾 **Blockchain-inspired logging of communication events**

---

## ⚙️ How It Works

- 📤 Satellite sends data to the terrestrial station  
- 🗃️ Base station logs communication details in a **distributed blockchain ledger**  
- 🚫 Unauthorized devices are detected and blocked  
- 🔑 Encryption keys are securely distributed using simulated **Quantum Key Distribution**

---

## 🚀 Benefits

- 🔐 Enhanced **Security & Privacy** for next-gen networks  
- 🌍 Better **coverage & reliability** over traditional terrestrial systems  
- 🤖 Supports **IoT**, **6G**, and **Autonomous Vehicles**  
- 🔍 Detects and mitigates attacks in real-time  

---

## 🧠 Technologies Used

- 🐍 Python (Flask)
- 🗃️ MySQL
- 📊 SHA-1 Hashing for file integrity
- 🔗 Blockchain concept simulation
- 🖥️ MAC Address-based authentication

---

## 📂 Modules

- `mac.py`: Extracts and formats the system MAC address  
- `Main.py`: Main backend logic including routing, user management, file upload/download, and verification  
- `satcom.sql`: SQL schema for managing users, data logs, and blockchain-like records  

---

## 📜 License

This project is for **academic and research purposes**. Contributions are welcome to make it more robust and production-ready. 🌟

---

## 🙌 Acknowledgements

- 🚀 Inspired by the need for secure communication in **6G and space technology**  
- 👨‍💻 Built as a part of undergraduate AI/ML research  
