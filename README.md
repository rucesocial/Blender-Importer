# Blender Importer

Blender Importer is a Python script that allows you to quickly import 3D models into Blender by double-clicking the file in Windows Explorer. The script determines the file type based on the extension and calls the appropriate Blender import operator.
This code is a very useful tool for Blender users, especially for those who want to import multiple files into Blender, as it saves time by allowing you to quickly select and import the file into Blender instead of right-clicking, going to the file menu, and importing it into Blender.

# How to use
```bat
@echo off

set "blender_path=C:\Program Files (x86)\Steam\steamapps\common\Blender\blender.exe"
set "import_script_path=C:\Ruce\GitHub\Blender-Importer\import_script.py"
set obj_file=%1

"%blender_path%" -P "%import_script_path%" -- "%obj_file%"
```

Replace `C:\Program Files\Blender Foundation\Blender\blender.exe` with the path to your Blender executable, and replace `C:\path\to\blender_importer.py` with the path to the Blender Importer script. Save the file as `blender_import.bat`.

Then, right-click on an .fbx file and select "Open with" -> "Choose another app". Select "More apps" -> "Look for another app on this PC" and select `blender_import.bat`. Check the "Always use this app to open .fbx files" box and click "OK". Now, double-clicking on an .fbx file will automatically open it in Blender using the Blender Importer script.

## Supported File Types

Blender Importer supports the following file types:

- .fbx: Supported in Blender 2.6 and later versions
- .obj: Supported in almost all Blender versions
- .3ds: Supported in almost all Blender versions
- .glb: Supported in Blender 2.80 and later versions
- .dae: Supported in almost all Blender versions
- .abc: Supported in Blender 2.72 and later versions
- .stl: Supported in almost all Blender versions
- .x3d: Supported in almost all Blender versions
- .usd: Supported in Blender 2.93 and later versions


