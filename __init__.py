import bpy
import os

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
        layout.operator("object.name_low", text="Name '_low'")
        layout.operator("object.name_high", text="Name '_high'")
        layout.separator()
        export_box = layout.box()
        export_box.label(text="Export Selected to FBX")
        export_box.label(text="Path:")
        export_box.prop(context.scene, "fbx_export_path", text="")
        export_box.operator("object.export_low_mesh", text="Export Low Mesh")
        export_box.operator("object.export_high_mesh", text="Export High Mesh")


class NameMeshLow(bpy.types.Operator):
    bl_idname = "object.name_low"
    bl_label = "Name '_low' to Object Name"

    def execute(self, context):
        for obj in context.selected_objects:
            if "_low" in obj.name:
                continue
            if "_high" in obj.name:
                obj.name = obj.name.replace("_high", "_low")
                continue
            obj.name = obj.name + "_low"
        return {"FINISHED"}


class NameMeshHigh(bpy.types.Operator):
    bl_idname = "object.name_high"
    bl_label = "Name '_high' to Object Name"

    def execute(self, context):
        for obj in context.selected_objects:
            if "_high" in obj.name:
                continue
            if "_low" in obj.name:
                obj.name = obj.name.replace("_low", "_high")
                continue

            obj.name = obj.name + "_high"
        return {"FINISHED"}


class ExportLowMesh(bpy.types.Operator):
    bl_idname = "object.export_low_mesh"
    bl_label = "Export Selected LowMesh Objects to FBX"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")
        for obj in context.scene.objects:
            if obj.name.endswith("_low"):
                obj.select_set(True)

        path = context.scene.fbx_export_path

        selected_objects = context.selected_objects
        if not selected_objects:
            self.report({"WARNING"}, "No objects selected.")
            return {"CANCELLED"}

        export_path = os.path.join(path, "export_low.fbx")
        bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        self.report({"INFO"}, f"Selected objects exported to: {export_path}")
        return {"FINISHED"}


class ExportHighMesh(bpy.types.Operator):
    bl_idname = "object.export_high_mesh"
    bl_label = "Export Selected HighMesh Objects to FBX"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")
        for obj in context.scene.objects:
            if obj.name.endswith("_high"):
                obj.select_set(True)

        path = context.scene.fbx_export_path

        selected_objects = context.selected_objects
        if not selected_objects:
            self.report({"WARNING"}, "No objects selected.")
            return {"CANCELLED"}

        export_path = os.path.join(path, "export_high.fbx")
        bpy.ops.export_scene.fbx(filepath=export_path, use_selection=True)
        self.report({"INFO"}, f"Selected objects exported to: {export_path}")
        return {"FINISHED"}


def register():
    bpy.utils.register_class(BlenderBakeNamingPreferences)
    bpy.utils.register_class(ObjectBakeNamingPanel)
    bpy.utils.register_class(NameMeshLow)
    bpy.utils.register_class(NameMeshHigh)
    bpy.utils.register_class(ExportLowMesh)
    bpy.utils.register_class(ExportHighMesh)


def unregister():
    bpy.utils.unregister_class(BlenderBakeNamingPreferences)
    bpy.utils.unregister_class(ObjectBakeNamingPanel)
    bpy.utils.unregister_class(NameMeshLow)
    bpy.utils.unregister_class(NameMeshHigh)
    bpy.utils.unregister_class(ExportLowMesh)
    bpy.utils.unregister_class(ExportHighMesh)


if __name__ == "__main__":
    register()
