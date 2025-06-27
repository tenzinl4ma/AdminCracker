# AdminCrack 🛡️

![image](https://github.com/user-attachments/assets/0a829704-c4ac-41dd-9a36-f7234622f02b)



> **AdminCrack** is an open-source penetration testing utility designed to simulate password harvesting and bruteforcing techniques against a fake `sudo` clone — all in a controlled, educational environment.

---

## Description

**AdminCrack** helps security researchers and ethical hackers demonstrate the risks of password reuse and local privilege escalation by replacing `sudo` with a controlled, instrumented clone.\
It logs fake credentials and allows brute-forcing using a custom or existing wordlist (like `rockyou.txt`) to simulate cracking behavior.

---

## Legal Disclaimer

This tool is **strictly intended for educational, ethical, and authorized security assessments only**.\
Do **not** use AdminCrack on any system without **explicit written permission**.

The developer is **not responsible** for any misuse or damage caused by this tool.

---

## Installation for Kali Linux

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AdminCrack.git
cd AdminCrack
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

## 🧪 Usage Examples

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

## ⚙️ Features

- Fake `sudo` binary to safely capture passwords
- Logs real/fake password attempts
- Python brute-forcer with progress output
- Prevents accidental use on real sudo
- Stylish terminal output with pyfiglet
- Easy to extend for demo/lab environments

---

## 🖼️ Screenshots



---

## 🔗 Dependencies

- Python 3.x
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- Unix-like system (tested on Kali Linux)

---

## 🤝 Contributing

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

## 📜 License

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
Instagram: [DraggonWarrior](https://www.instagram.com/tenzinlama212/#) <br>
Email: tenzinlama212@gmail.com
---

## Ethical Use Reminder

AdminCrack exists for one purpose: **to educate and protect**.\
Misuse of this tool violates ethical hacking standards and legal boundaries.

Stay sharp.\
Stay ethical.
Stay halal
