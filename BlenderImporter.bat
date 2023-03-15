@echo off

set "blender_path=C:\Program Files (x86)\Steam\steamapps\common\Blender\blender.exe"
set "import_script_path=C:\Ruce\GitHub\Blender-Importer\import_script.py"
set obj_file=%1

"%blender_path%" -P "%import_script_path%" -- "%obj_file%"
