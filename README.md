# 🧊 icepick

**Advanced Penetration Suite — Precision strikes. Every time.**  
One tool. Three interfaces: Desktop GUI, CLI, and Android (coming soon).

[فارسی](#-فارسی) · [Download](https://github.com/iceSEC-Operations/icepick/releases) · [Report an issue](https://github.com/iceSEC-Operations/icepick/issues)

---

**icepick** is a lightweight, powerful, and AI-assisted penetration testing suite designed for precision security assessments. Built by **iceSEC | Cyber Intelligence Operations**, it combines speed, accuracy, and elegance in a single tool.

---

## 🎯 What makes it useful

| Capability | What it gives you |
|------------|-------------------|
| 🚀 **Multi-Threaded Port Scanning** | Scan 23+ common ports in seconds with adjustable worker count |
| 🎯 **Smart Vulnerability Detection** | Detect SQLi, XSS, exposed admin panels, and more |
| 🖥️ **Professional GUI** | Dark theme with hacker cursor (neon ring + crosshair + particle trail), matrix rain background |
| 📊 **Live Results** | Search, sort, inspect, and copy results while a scan is still running |
| 📈 **Security Scoring** | 0–100 score with risk assessment (Low/Medium/High/Critical) |
| 💾 **One-Click Export** | Save detailed JSON reports with all findings |
| 🔗 **Brand Integration** | iceSEC Landing Page, Telegram Channel, GitHub, and Support |

---

## 🖥️ Choose your interface

| Interface | Platforms | Best for |
|-----------|-----------|----------|
| **Desktop GUI** | Windows, Linux, macOS | Full experience, live filtering, speed, and exports |
| **CLI** | Windows, Linux, macOS, Termux | Keyboard-first scanning, automation-friendly |
| **Android** | Android 7.0+ | Coming soon |

---

## 🔄 Signal Desk Workflow

```mermaid
flowchart LR
    A["Configure scan"] --> B["Discover vulnerabilities & ports"]
    B --> C["Inspect or copy results live"]
    B --> D["Stop or finish discovery"]
    D --> E["Review ranked results"]
    E --> F["Export JSON report"]

The desktop interface keeps each responsibility in its own workspace:

- **Scan** — configure target, ports, workers, timeout, and scan options.
- **Results** — monitor progress, filter and sort endpoints, copy results at any time.
- **Export** — save detailed JSON reports with security scoring.

---

## ✨ Core Features

### Discovery and Ranking

- Target profiling (IP, Server, Technology Stack)
- Multi-port scanning with configurable worker count and timeout
- Live health, port, and status reporting
- Vulnerability detection (SQLi, XSS, Admin Panels)
- Cancellation that preserves results already discovered

### Security Scoring and Reporting

- 0–100 security score based on findings
- Risk assessment (Low/Medium/High/Critical)
- Detailed vulnerability information with locations
- One-click JSON export

### Copy and Export

- Copy results at any time
- Save detailed JSON reports
- Generate comprehensive security assessments

---

## 📥 Download version 1.0.0

Download the build for your platform from GitHub Releases.

### Desktop GUI

| Platform | Release asset |
|----------|---------------|
| Windows x64 | `icepick-gui-windows-amd64.zip` |

### CLI

| Platform | Release asset |
|----------|---------------|
| Windows x64 | `icepick-cli-windows-amd64.exe` |
| Linux x64 | `icepick-cli-linux-amd64` |
| macOS | `icepick-cli-macos` |

---

## 🚀 Quick Start

### Desktop GUI

1. Download the latest `icepick-gui-windows-amd64.zip`
2. Extract the folder
3. Run `icepick-gui.exe`
4. Enter a target and click **START SCAN**
5. View results in real-time
6. Export your report with one click

### CLI

```bash
# Download the CLI binary
chmod +x icepick-cli-linux-amd64
./icepick-cli-linux-amd64 -t example.com
```

### Termux

```bash
pkg update
pkg install curl -y
curl -fL -o "$PREFIX/bin/icepick" \
  https://github.com/iceSEC-Operations/icepick/releases/download/v1.0.0/icepick-cli-linux-arm64
chmod +x "$PREFIX/bin/icepick"
icepick -t example.com
```

---

## 🛠️ Build from Source

### Requirements

- Python **3.8+**
- Tkinter (built-in)
- No external dependencies required

### Test and Build

```bash
# Clone the repository
git clone https://github.com/iceSEC-Operations/icepick.git
cd icepick

# Run the GUI
python gui_standalone.py

# Build EXE with PyInstaller
pyinstaller --onedir --windowed --name icepick-gui --hidden-import=tkinter --hidden-import=socket --hidden-import=json --hidden-import=threading --hidden-import=urllib --hidden-import=concurrent.futures gui_standalone.py
```

---

## 📁 Repository Map

```
icepick/
├── gui_standalone.py          # Main GUI application
├── icepick/                    # Core package
│   ├── core/                   # Engine modules
│   ├── scanner/                # Scanner modules
│   ├── gui/                    # GUI components
│   └── utils/                  # Utilities
├── assets/                     # Logos & banners
├── docs/                       # Documentation
├── examples/                   # Example outputs
├── README.md                   # This file
├── LICENSE                     # MIT License
└── requirements.txt            # Dependencies
```

---

## 🔗 Connect with iceSEC

| Platform | Link |
|----------|------|
| 🌐 **Landing Page** | [icesec-operations.github.io/LandingPage](https://icesec-operations.github.io/LandingPage/) |
| 📱 **Telegram Channel** | [@iceSEC_Operations](https://t.me/iceSEC_Operations) |
| 👤 **Owner** | [@iceSEC_Operator](https://t.me/iceSEC_Operator) |
| 🐙 **GitHub** | [iceSEC-Operations](https://github.com/iceSEC-Operations) |
| 📧 **Email** | [icesec@atomicmail.io](mailto:icesec@atomicmail.io) |

---

## 🤝 Contributing

We welcome feedback and suggestions! Here's how you can help:

- 🐛 **Report bugs** via [Issues](https://github.com/iceSEC-Operations/icepick/issues)
- 💡 **Suggest features** via [Issues](https://github.com/iceSEC-Operations/icepick/issues)
- 💬 **Ask questions** via [Discussions](https://github.com/iceSEC-Operations/icepick/discussions)

> **Note:** We do not accept Pull Requests at this time.

---

## ⚠️ Disclaimer

> **This tool is for EDUCATIONAL and ETHICAL purposes only.**  
> Use it only on systems you own or have explicit permission to test.  
> iceSEC is not responsible for any misuse or damage caused by this tool.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>🧊 iceSEC | Cyber Intelligence Operations</strong><br>
  <em>Precision strikes. Every time.</em>
</p>

<p align="center">
  Made with ❤️ by <strong>iceSEC</strong>
</p>
```
