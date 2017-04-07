import cx_Freeze

executables = [cx_Freeze.Executable("maker.py")]

cx_Freeze.setup(
	name="2048 Wars Map Maker",
	options={"build_exe":{"packages":["pygame"],"include_files":["assets/icon.png"]}},
	description="Map maker for 2048 Wars game for android",
	executables = executables
	)