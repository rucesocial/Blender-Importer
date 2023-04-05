import bpy
import os
import sys

# Get all arguments after the fourth argument as a list
file_path = sys.argv[4:]

# Join the arguments into a single string
file_path = " ".join(file_path)

# Remove any quotation marks in the file path
file_path = file_path.replace('"', '')

# Store the original file path
original_path = file_path

# Get the extension of the file
ext = os.path.splitext(file_path)[1].lower()

# Get the active scene in the current Blender context
scene = bpy.context.scene

# Get the operator properties
act = None
if hasattr(scene, "act") and scene.act is not None:
    act = scene.act
    act.custom_export_path = 1
    act.export_path = os.path.dirname(original_path)
else:
    print("Scene object has no attribute 'act' or it is None")

# Set the custom export path and export directory path to the directory of the original file path
if act is not None:
    act.custom_export_path = 1
    act.export_path = os.path.dirname(original_path)

# Import the file based on the file extension
if ext == ".fbx": # Supported in Blender 2.6 and later versions
    bpy.ops.import_scene.fbx(filepath=file_path)
elif ext == ".obj": # Supported in almost all Blender versions
    bpy.ops.import_scene.obj(filepath=file_path)
elif ext == ".3ds": # Supported in almost all Blender versions
    bpy.ops.import_scene.autodesk_3ds(filepath=file_path)
elif ext == ".glb": # Supported in Blender 2.80 and later versions
    bpy.ops.import_scene.gltf2(filepath=file_path)
elif ext == ".dae": # Supported in almost all Blender versions
    bpy.ops.wm.collada_import(filepath=file_path)
elif ext == ".abc": # Supported in Blender 2.72 and later versions
    bpy.ops.alembic_import(filepath=file_path)
elif ext == ".stl": # Supported in almost all Blender versions
    bpy.ops.import_mesh.stl(filepath=file_path)
elif ext == ".x3d": # Supported in almost all Blender versions
    bpy.ops.import_scene.x3d(filepath=file_path)
elif ext == ".usd": # Supported in Blender 2.93 and later versions
    bpy.ops.usd.import_file(filepath=file_path)
else:
    print("Extension %r is not known!" % ext)

