import bpy

class SortCollectionWithName(bpy.types.Operator):
    bl_idname = "object.sort_collection_with_name"
    bl_label = "Sort collections with name high and low"

    def execute(self, context):
        low_collection = None
        high_collection = None

        for col in bpy.data.collections:
            if col.name == "Low":
                low_collection = col
            elif col.name == "High":
                high_collection = col
        
        if low_collection is None:
            low_collection = bpy.data.collections.new("Low")
            context.scene.collection.children.link(low_collection)
        if high_collection is None:
            high_collection = bpy.data.collections.new("High")
            context.scene.collection.children.link(high_collection)

        for obj in context.scene.objects:
            if "_low" in obj.name:
                for c in obj.users_collection:
                    c.objects.unlink(obj)
                low_collection.objects.link(obj)
            if "_high" in obj.name:
                for c in obj.users_collection:
                    c.objects.unlink(obj)
                high_collection.objects.link(obj)

        return {"FINISHED"}
