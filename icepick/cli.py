"""
🧊 icepick — Advanced Penetration Suite
by iceSEC | Cyber Intelligence Operations
"""

import sys
import os

# اضافه کردن مسیر ریشه‌ی پروژه به sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui_standalone import IcePickPro

def main():
    app = IcePickPro()
    app.run()

if __name__ == "__main__":
    main()