import bpy

from .modules.export import ExportHighMesh, ExportLowMesh
from .modules.naming import NameMeshHigh, NameMeshLow
from .modules.duplicate import DuplicateToHigh, DuplicateToLow
from .modules.sort import SortCollectionWithName

bl_info = {
    "name": "BakeNaming",
    "author": "Jooz",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > BakeNaming",
    "description": "Adds buttons to append '_low' or '_high' to selected object names",
    "category": "BakeNaming",
}


class BlenderBakeNamingPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    export_path = bpy.props.StringProperty(
        name="Example File Path",
        default="",
        subtype="DIR_PATH",
    )
    bpy.types.Scene.fbx_export_path = export_path


class ObjectBakeNamingPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_Bake_Naming"
    bl_label = "BakeNaming"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BakeNaming"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Name Objects")
        layout.operator("object.name_low", text="Name '_low'")
        layout.operator("object.name_high", text="Name '_high'")
        layout.separator()
        layout.label(text="Duplicate Objects")
        layout.operator("object.duplicate_low", text="Duplicate to '_low'")
        layout.operator("object.duplicate_high", text="Duplicate to '_high'")
        layout.separator()
        layout.label(text="Sort Collection")
        layout.operator("object.sort_collection_with_name", text="Sort Collection")
        layout.separator()
        export_box = layout.box()
        export_box.label(text="Export Objects to FBX")
        export_box.label(text="Path:")
        export_box.prop(context.scene, "fbx_export_path", text="")
        export_box.operator("object.export_low_mesh", text="Export Low Mesh")
        export_box.operator("object.export_high_mesh", text="Export High Mesh")

def register():
    bpy.utils.register_class(BlenderBakeNamingPreferences)
    bpy.utils.register_class(ObjectBakeNamingPanel)
    bpy.utils.register_class(NameMeshLow)
    bpy.utils.register_class(NameMeshHigh)
    
    bpy.utils.register_class(ExportLowMesh)
    bpy.utils.register_class(ExportHighMesh)
    
    bpy.utils.register_class(DuplicateToLow)
    bpy.utils.register_class(DuplicateToHigh)

    bpy.utils.register_class(SortCollectionWithName)


def unregister():
    bpy.utils.unregister_class(BlenderBakeNamingPreferences)
    bpy.utils.unregister_class(ObjectBakeNamingPanel)
    bpy.utils.unregister_class(NameMeshLow)
    bpy.utils.unregister_class(NameMeshHigh)
    
    bpy.utils.unregister_class(ExportLowMesh)
    bpy.utils.unregister_class(ExportHighMesh)

    bpy.utils.unregister_class(DuplicateToLow)
    bpy.utils.unregister_class(DuplicateToHigh)

    bpy.utils.unregister_class(SortCollectionWithName)


if __name__ == "__main__":
    register()
