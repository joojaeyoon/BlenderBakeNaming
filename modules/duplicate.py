import bpy

class DuplicateToLow(bpy.types.Operator):
    bl_idname = "object.duplicate_low"
    bl_label = "Duplicate selected objects and Name _low"

    def execute(self, context):
        new_objects =[]
        for obj in context.selected_objects:
            new_name = obj.name
            new_obj = obj.copy()
            new_obj.data = obj.data.copy()
            context.collection.objects.link(new_obj)

            new_objects.append(new_obj)
            obj.select_set(False)

            if "_high" in new_name:
                new_obj.name = new_name.replace("_high","_low")
                continue

            new_obj.name = new_name + "_low"
        
        for new_obj in new_objects:            
            new_obj.select_set(True)

        return {"FINISHED"}


class DuplicateToHigh(bpy.types.Operator):
    bl_idname = "object.duplicate_high"
    bl_label = "Duplicate selected objects and Name _high"

    def execute(self, context):
        new_objects =[]
        for obj in context.selected_objects:
            new_name = obj.name
            new_obj = obj.copy()
            new_obj.data = obj.data.copy()
            context.collection.objects.link(new_obj)

            new_objects.append(new_obj)
            obj.select_set(False)

            if "_low" in new_name:
                new_obj.name = new_name.replace("_low","_high")
                continue

            new_obj.name = new_name + "_high"
        
        for new_obj in new_objects:            
            new_obj.select_set(True)
        
        return {"FINISHED"}