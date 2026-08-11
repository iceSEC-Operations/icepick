"""
🧊 icepick — Advanced Penetration Suite
by iceSEC | Cyber Intelligence Operations
Standalone GUI — No external dependencies
"""
import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox, font
import socket
import json
import threading
import webbrowser
from datetime import datetime
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== CONSTANTS =====
GITHUB_URL = "https://github.com/iceSEC-Operations"
TELEGRAM_URL = "https://t.me/iceSEC_Operations"
OWNER_ID = "https://t.me/iceSEC_Operator"
EMAIL = "icesec@atomicmail.io"
LANDING_URL = "https://icesec-operations.github.io/LandingPage/"  # <-- اضافه شد

# ===== STYLE =====
BG_DARK = "#0a0e17"
BG_PANEL = "#111927"
BG_INPUT = "#0d1520"
BG_BUTTON = "#0d1520"
FG_TEXT = "#c8d6e5"
FG_GREEN = "#00ff88"
FG_RED = "#ff3355"
FG_BLUE = "#00d4ff"
FG_YELLOW = "#ffcc00"
FG_CYAN = "#00e5ff"
BORDER_COLOR = "#00d4ff"
SHADOW = "#00d4ff22"
LINK_HOVER = "#00aaff"

# ===== MAIN APP =====
class IcePickPro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧊 icepick — Advanced Penetration Suite")
        self.root.geometry("1100x800")
        self.root.configure(bg=BG_DARK)
        self.root.resizable(False, False)

        # Try to set icon
        try:
            self.root.iconbitmap(default='assets/icon.ico')
        except:
            pass

        # Variables
        self.is_running = False
        self.last_results = None
        self.has_promoted = False  # برای تبلیغات یک‌باره
        self._build_ui()

    def _open_link(self, url):
        webbrowser.open(url)

    def _build_ui(self):
        # ===== HEADER =====
        header = tk.Frame(self.root, bg=BG_DARK, height=100)
        header.pack(fill=tk.X, pady=(10, 0))

        # Left: Logo
        logo_frame = tk.Frame(header, bg=BG_DARK)
        logo_frame.pack(side=tk.LEFT, padx=30)

        tk.Label(logo_frame, text="🧊", font=("Segoe UI", 36), fg=FG_BLUE, bg=BG_DARK).pack(side=tk.LEFT)

        title_frame = tk.Frame(logo_frame, bg=BG_DARK)
        title_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(title_frame, text="icepick", font=("Segoe UI", 24, "bold"), fg=FG_TEXT, bg=BG_DARK).pack(anchor=tk.W)
        tk.Label(title_frame, text="Advanced Penetration Suite", font=("Segoe UI", 9), fg=FG_CYAN, bg=BG_DARK).pack(anchor=tk.W)

        # Right: Version + Social
        right_frame = tk.Frame(header, bg=BG_DARK)
        right_frame.pack(side=tk.RIGHT, padx=30)

        # Version
        tk.Label(right_frame, text="v1.0.1", font=("Segoe UI", 10, "bold"), fg=FG_YELLOW, bg=BG_DARK).pack(anchor=tk.E)
        tk.Label(right_frame, text="by iceSEC", font=("Segoe UI", 8), fg=FG_BLUE, bg=BG_DARK).pack(anchor=tk.E)

        # Social links (clickable)
        social_frame = tk.Frame(right_frame, bg=BG_DARK)
        social_frame.pack(anchor=tk.E, pady=(5, 0))

        # Landing Page link (NEW)
        landing_label = tk.Label(
            social_frame,
            text="🌐 Landing Page",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        landing_label.pack(side=tk.LEFT, padx=5)
        landing_label.bind("<Button-1>", lambda e: self._open_link(LANDING_URL))

        # GitHub link
        github_label = tk.Label(
            social_frame,
            text="🐙 GitHub",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        github_label.pack(side=tk.LEFT, padx=5)
        github_label.bind("<Button-1>", lambda e: self._open_link(GITHUB_URL))

        # Telegram link
        tele_label = tk.Label(
            social_frame,
            text="📱 Telegram Channel",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        tele_label.pack(side=tk.LEFT, padx=5)
        tele_label.bind("<Button-1>", lambda e: self._open_link(TELEGRAM_URL))

        # ===== SEPARATOR =====
        sep = tk.Frame(self.root, height=2, bg=BORDER_COLOR)
        sep.pack(fill=tk.X, padx=30, pady=10)

        # ===== INPUT PANEL =====
        panel = tk.Frame(self.root, bg=BG_PANEL, relief=tk.FLAT, bd=0)
        panel.pack(fill=tk.X, padx=30, pady=10)

        tk.Label(panel, text="🎯 TARGET", font=("Segoe UI", 10, "bold"), fg=FG_TEXT, bg=BG_PANEL).pack(side=tk.LEFT, padx=10)

        self.target_entry = tk.Entry(
            panel,
            font=("Segoe UI", 12),
            bg=BG_INPUT,
            fg=FG_TEXT,
            insertbackground=FG_CYAN,
            relief=tk.FLAT,
            bd=0,
            width=45,
            highlightthickness=1,
            highlightcolor=BORDER_COLOR,
            highlightbackground=BORDER_COLOR
        )
        self.target_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.target_entry.bind("<Return>", lambda e: self.start_scan())

        # Scan Button
        self.scan_btn = tk.Button(
            panel,
            text="⚡ START SCAN",
            font=("Segoe UI", 11, "bold"),
            bg=FG_BLUE,
            fg=BG_DARK,
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.start_scan
        )
        self.scan_btn.pack(side=tk.LEFT, padx=20)

        # Status indicator
        self.status_indicator = tk.Label(
            panel,
            text="● READY",
            font=("Segoe UI", 9, "bold"),
            fg=FG_GREEN,
            bg=BG_PANEL
        )
        self.status_indicator.pack(side=tk.RIGHT, padx=15)

        # ===== LOG AREA =====
        log_container = tk.Frame(self.root, bg=BG_DARK)
        log_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # Log header
        log_header = tk.Frame(log_container, bg=BG_DARK)
        log_header.pack(fill=tk.X)

        tk.Label(log_header, text="📋 CONSOLE", font=("Segoe UI", 9, "bold"), fg=FG_TEXT, bg=BG_DARK).pack(side=tk.LEFT)

        # Log text
        self.log_text = scrolledtext.ScrolledText(
            log_container,
            font=("Cascadia Code", 10),
            bg=BG_INPUT,
            fg=FG_TEXT,
            insertbackground=FG_CYAN,
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightcolor=BORDER_COLOR,
            highlightbackground=BORDER_COLOR,
            wrap=tk.WORD,
            padx=12,
            pady=12
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        # Tag styles for log
        self.log_text.tag_config("info", foreground=FG_CYAN)
        self.log_text.tag_config("ok", foreground=FG_GREEN)
        self.log_text.tag_config("warn", foreground=FG_YELLOW)
        self.log_text.tag_config("err", foreground=FG_RED)
        self.log_text.tag_config("vuln", foreground=FG_RED)

        # ===== BOTTOM BUTTONS =====
        btn_frame = tk.Frame(self.root, bg=BG_DARK)
        btn_frame.pack(fill=tk.X, padx=30, pady=10)

        self.save_btn = tk.Button(
            btn_frame,
            text="💾 SAVE REPORT",
            font=("Segoe UI", 10),
            bg=BG_PANEL,
            fg=FG_TEXT,
            relief=tk.FLAT,
            bd=0,
            padx=15,
            pady=6,
            cursor="hand2",
            state=tk.DISABLED,
            command=self.save_report
        )
        self.save_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="🗑 CLEAR LOG",
            font=("Segoe UI", 10),
            bg=BG_PANEL,
            fg=FG_TEXT,
            relief=tk.FLAT,
            bd=0,
            padx=15,
            pady=6,
            cursor="hand2",
            command=self.clear_log
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            btn_frame,
            text="❌ EXIT",
            font=("Segoe UI", 10),
            bg=BG_PANEL,
            fg=FG_RED,
            relief=tk.FLAT,
            bd=0,
            padx=15,
            pady=6,
            cursor="hand2",
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)

        # ===== FOOTER =====
        footer = tk.Frame(self.root, bg=BG_DARK)
        footer.pack(fill=tk.X, pady=(0, 8))

        # Line separator
        sep2 = tk.Frame(footer, height=1, bg="#1a2340")
        sep2.pack(fill=tk.X, padx=30, pady=5)

        # Footer content
        footer_inner = tk.Frame(footer, bg=BG_DARK)
        footer_inner.pack(fill=tk.X, padx=30)

        # Left: Brand
        tk.Label(
            footer_inner,
            text="🧊 iceSEC | Cyber Intelligence Operations",
            font=("Segoe UI", 8),
            fg=FG_BLUE,
            bg=BG_DARK
        ).pack(side=tk.LEFT)

        # Center: Tagline
        tk.Label(
            footer_inner,
            text="Precision strikes. Every time.",
            font=("Segoe UI", 8, "italic"),
            fg=FG_YELLOW,
            bg=BG_DARK
        ).pack(side=tk.LEFT, padx=20)

        # Right: Links (clickable)
        link_frame = tk.Frame(footer_inner, bg=BG_DARK)
        link_frame.pack(side=tk.RIGHT)

        # Landing Page
        lp_link = tk.Label(
            link_frame,
            text="🌐 Landing Page",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        lp_link.pack(side=tk.LEFT, padx=8)
        lp_link.bind("<Button-1>", lambda e: self._open_link(LANDING_URL))

        # Separator
        tk.Label(link_frame, text="|", font=("Segoe UI", 8), fg="#2a3a5a", bg=BG_DARK).pack(side=tk.LEFT)

        # GitHub
        g_link = tk.Label(
            link_frame,
            text="🐙 GitHub",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        g_link.pack(side=tk.LEFT, padx=8)
        g_link.bind("<Button-1>", lambda e: self._open_link(GITHUB_URL))

        # Separator
        tk.Label(link_frame, text="|", font=("Segoe UI", 8), fg="#2a3a5a", bg=BG_DARK).pack(side=tk.LEFT)

        # Telegram
        t_link = tk.Label(
            link_frame,
            text="📱 Telegram Channel",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        t_link.pack(side=tk.LEFT, padx=8)
        t_link.bind("<Button-1>", lambda e: self._open_link(TELEGRAM_URL))

        # Separator
        tk.Label(link_frame, text="|", font=("Segoe UI", 8), fg="#2a3a5a", bg=BG_DARK).pack(side=tk.LEFT)

        # Owner
        a_link = tk.Label(
            link_frame,
            text="👤 Owner",
            font=("Segoe UI", 8, "underline"),
            fg=FG_BLUE,
            bg=BG_DARK,
            cursor="hand2"
        )
        a_link.pack(side=tk.LEFT, padx=8)
        a_link.bind("<Button-1>", lambda e: self._open_link(OWNER_ID))

    def _log(self, msg, level="info"):
        tag = level if level in ["info", "ok", "warn", "err", "vuln"] else "info"
        self.log_text.insert(tk.END, f"{msg}\n", tag)
        self.log_text.see(tk.END)
        self.root.update()

    def _set_status(self, text, color):
        self.status_indicator.config(text=text, fg=color)
        self.root.update()

    def start_scan(self):
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a target!")
            return

        # ===== تبلیغات: فقط یکبار =====
        if not self.has_promoted:
            webbrowser.open(LANDING_URL)
            self.has_promoted = True
            self._log("🌐 Visit our Landing Page: " + LANDING_URL, "info")
        # =================================

        self.is_running = True
        self.scan_btn.config(state=tk.DISABLED, text="⏳ SCANNING...")
        self.save_btn.config(state=tk.DISABLED)
        self._set_status("● SCANNING", FG_YELLOW)
        self._log(f"\n{'='*60}")
        self._log(f"🧊 icepick scan started for: {target}", "info")
        self._log(f"{'='*60}")

        def run():
            try:
                results = self._scan(target)
                self.last_results = results
                self.root.after(0, self._scan_finished)
            except Exception as e:
                self._log(f"❌ Error: {e}", "err")
                self.root.after(0, self._scan_error)

        threading.Thread(target=run, daemon=True).start()

    def _scan(self, target):
        results = {
            "target": target,
            "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "profile": {},
            "open_ports": [],
            "vulnerabilities": []
        }

        # Profile
        self._log("🔍 Profiling target...", "info")
        try:
            ip = socket.gethostbyname(target)
            results["profile"]["ip"] = ip
            self._log(f"   ✅ IP: {ip}", "ok")
        except:
            self._log("   ❌ DNS resolution failed", "err")

        try:
            req = Request(f"https://{target}")
            req.add_header("User-Agent", "icepick/1.0")
            resp = urlopen(req, timeout=5)
            server = resp.headers.get("Server", "Unknown")
            results["profile"]["server"] = server
            self._log(f"   ✅ Server: {server}", "ok")
        except:
            pass

        # Port scan
        self._log("🔍 Scanning ports...", "info")
        ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                if sock.connect_ex((target, port)) == 0:
                    results["open_ports"].append(port)
                    self._log(f"   ✅ Port {port} OPEN", "ok")
                sock.close()
            except:
                pass

        # Vulnerability scan
        self._log("🔍 Scanning vulnerabilities...", "info")
        panels = ["/admin", "/wp-admin", "/cpanel", "/phpmyadmin", "/login", "/dashboard", "/backup", "/temp"]
        for panel in panels:
            try:
                url = f"http://{target}{panel}"
                req = Request(url)
                req.add_header("User-Agent", "icepick/1.0")
                resp = urlopen(req, timeout=2)
                if resp.status in [200, 403]:
                    results["vulnerabilities"].append({
                        "type": "Exposed Admin Panel",
                        "risk": "High",
                        "location": url
                    })
                    self._log(f"   💀 Admin panel: {url}", "vuln")
            except:
                pass

        # Score
        vuln_count = len(results["vulnerabilities"])
        score = max(0, 100 - (vuln_count * 15))
        results["security_score"] = score

        if score >= 80:
            risk = "Low"
        elif score >= 50:
            risk = "Medium"
        elif score >= 30:
            risk = "High"
        else:
            risk = "Critical"
        results["risk_level"] = risk

        self._log(f"   📊 Score: {score}/100 — Risk: {risk}")

        return results

    def _scan_finished(self):
        self.is_running = False
        self.scan_btn.config(state=tk.NORMAL, text="⚡ START SCAN")
        self.save_btn.config(state=tk.NORMAL)
        self._set_status("● READY", FG_GREEN)
        if self.last_results:
            self._log(f"\n✅ Scan complete! Score: {self.last_results['security_score']}/100 | Risk: {self.last_results['risk_level']}", "ok")
            self._log(f"{'='*60}")

    def _scan_error(self):
        self.is_running = False
        self.scan_btn.config(state=tk.NORMAL, text="⚡ START SCAN")
        self._set_status("● ERROR", FG_RED)

    def save_report(self):
        if not self.last_results:
            return
        filename = f"icepick_report_{self.last_results['target']}_{self.last_results['timestamp']}.json"
        with open(filename, "w") as f:
            json.dump(self.last_results, f, indent=2)
        self._log(f"💾 Report saved: {filename}", "ok")
        messagebox.showinfo("Success", f"Report saved as {filename}")

    def clear_log(self):
        self.log_text.delete(1.0, tk.END)

    def run(self):
        self.root.mainloop()


# ===== ENTRY =====
if __name__ == "__main__":
    app = IcePickPro()
    app.run()

    def main():
        app = IcePickPro()
        app.run()