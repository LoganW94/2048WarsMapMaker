from cx_Freeze import setup, Executable

setup(
	name="2048 Wars Map Maker",
	version='v0.2',
	options={"build_exe":{"packages":["pygame"],"include_files":["assets/icon.png"]}},
	description="Map maker for 2048 Wars game for android",
	executables = [Executable("main.py")]
	)