import bpy
import mathutils

obj = bpy.context.selected_objects[0]
obj2 = bpy.context.selected_objects[1]

def get_bounding_box(obj):
            # Get the world-space bounding box
            bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
            bbox_min = mathutils.Vector((min([v.x for v in bbox_corners]), 
                            min([v.y for v in bbox_corners]), 
                            min([v.z for v in bbox_corners])))
            bbox_max = mathutils.Vector((max([v.x for v in bbox_corners]), 
                            max([v.y for v in bbox_corners]), 
                            max([v.z for v in bbox_corners])))
            print(bbox_min, bbox_max)
            return bbox_min, bbox_max

def calculate_overlap_volume(obj1, obj2):
    min1, max1 = get_bounding_box(obj1)
    min2, max2 = get_bounding_box(obj2)
    print (min1, max1)
    print (min2, max2)
    
    # Calculate overlap in each dimension
    overlap_min = mathutils.Vector((max(min1.x, min2.x), 
                        max(min1.y, min2.y), 
                        max(min1.z, min2.z)))
    overlap_max = mathutils.Vector((min(max1.x, max2.x), 
                        min(max1.y, max2.y), 
                        min(max1.z, max2.z)))

    # Calculate the dimensions of the overlap box
    overlap_size = overlap_max - overlap_min
    
    # If there's no overlap in any dimension, the volume is zero
    if overlap_size.x <= 0 or overlap_size.y <= 0 or overlap_size.z <= 0:
        print("No overlap")
        return 0.0

    # Calculate and return the overlap volume
    overlap_volume = overlap_size.x * overlap_size.y * overlap_size.z
    
    #Obj1 volume
    volume = obj1.dimensions.x * obj1.dimensions.y * obj1.dimensions.z
    print(volume)
    
    print((overlap_volume/volume)*100,"% overlap")
    return overlap_volume

#get_bounding_box(obj)
calculate_overlap_volume(obj,obj2)
