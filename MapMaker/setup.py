import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(
	name="2048 Wars Map Maker",
	version='v0.2',
	options={"build_exe":{"packages":["pygame"],"include_files":["assets/icon.png"]}},
	description="Map maker for 2048 Wars game for android",
	executables = [Executable("main.py", base = base)]
	)