import bpy
import os

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