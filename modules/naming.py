import bpy

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