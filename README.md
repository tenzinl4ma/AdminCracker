<h1> AdminCrack </h1> 

![image](https://github.com/user-attachments/assets/0a829704-c4ac-41dd-9a36-f7234622f02b)



> **AdminCrack** is an open-source penetration testing utility designed to simulate password harvesting and bruteforcing techniques against a fake `sudo` clone — all in a controlled, educational environment.

---

 <h1>About</h1>

AdminCrack is a lightweight and stealthy post-exploitation tool designed for red teams, ethical hackers, and security researchers to safely perform sudo bruteforcing without touching the real system binary.

Instead of hammering the actual /usr/bin/sudo — which could trigger detection, logging, or rate-limiting mechanisms — AdminCrack clones the sudo interface into a custom sandboxed wrapper, allowing you to:

Safely capture sudo prompts in a simulated environment

Bruteforce the fake sudo using custom or standard password lists (like rockyou.txt)

Avoid leaving traces in system logs or alerting EDR/HIDS tools

Validate if a guessed password is the real admin password by comparing against sudo behavior

Seamlessly escalate from low-privilege (guest) to high-privilege (admin) once the password is cracked

Great for lab environments, internal tests, or post-shell privilege escalation scenarios

With built-in detection to prevent accidentally targeting the real sudo, AdminCrack ensures safe testing conditions.
---

<h1>Legal Disclaimer</h1> 

This tool is **strictly intended for educational, ethical, and authorized security assessments only**.\
Do **not** use AdminCrack on any system without **explicit written permission**.

The developer is **not responsible** for any misuse or damage caused by this tool.

---

<h1>Installation for Kali Linux</h1>

### 1. Clone the repository

```bash
git clone https://github.com/tenzinl4ma/AdminCracker.git
```

### 2. Install Python requirements

```bash
pip install -r requirements.txt
```

If `pyfiglet` is missing:

```bash
pip install pyfiglet
```

### 3. Set up the fake sudo clone

```bash
mkdir -p ~/bin
cp fake_sudo.sh ~/bin/sudo
chmod +x ~/bin/sudo
```

### 4. Add fake sudo to your path

Edit your `~/.zshrc` or `~/.bashrc` file and add:

```bash
export PATH="$HOME/bin:$PATH"
```

Then reload your shell config:

```bash
source ~/.zshrc   # or
source ~/.bashrc
```

---

<h1>🧪 Usage Examples</h1>

### Run the brute-force engine

```bash
python3 cracker.py
```

### Set wordlist path inside `cracker.py`

```python
WORDLIST = "/usr/share/wordlists/rockyou.txt"
```

You can replace this with any custom list.

---

<h1><⚙️ Features/h1> 

- Fake `sudo` binary to safely capture passwords
- Logs real/fake password attempts
- Python brute-forcer with progress output
- Prevents accidental use on real sudo
- Stylish terminal output with pyfiglet
- Easy to extend for demo/lab environments

---

## 
<img width="1414" alt="Screenshot 2025-06-27 at 12 51 34 PM" src="https://github.com/user-attachments/assets/648dccbe-606f-4c2c-9824-66c8da530963" />



---

 <h1>🔗 Dependencies</h1>

- Python 3.x
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- Unix-like system (tested on Kali Linux)

---

<h1>🤝 Contributing</h1>

Contributions are welcome!

1. Fork this repo
2. Create a feature branch
   ```bash
   git checkout -b new-feature
   ```
3. Commit your changes
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch
   ```bash
   git push origin new-feature
   ```
5. Open a pull request

Bug reports and feature suggestions are also appreciated through Issues.

---

<h1>📜 License/h1> 

MIT License

```
MIT License

Copyright (c) 2025 Tenzin Lama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Tenzin Lama**\
<br>
Instagram: [DraggonWarrior](https://www.instagram.com/tenzinlama212/#) <br>
Email: tenzinlama212@gmail.com
---

## Ethical Use Reminder

AdminCrack exists for one purpose: **to educate and protect**.\
Misuse of this tool violates ethical hacking standards and legal boundaries.

Stay sharp.\
Stay ethical.<br>
Stay halal
