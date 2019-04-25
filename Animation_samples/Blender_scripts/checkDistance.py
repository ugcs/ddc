import bpy
import math
sce = bpy.context.scene
# CHANGE THESE PARAMETERS ACCORDING TO BLENDER ANIMATION
number_of_uavs = 20 # number of uavs in blender scene
scene_frames = 2600 # length of animation in frames

d_treshold = 249 # distance threshold in centimeters 

# CHANGE SCALE BASED ON SCRIPT OUTPUT TO INREASE OR DECREASE DISTANCE
scale = 1.3

print("\nRunning distance check\n")

for i in range(0, number_of_uavs):
    ob = bpy.data.objects['Sphere_' + str(i)]
    print("\nChecking Sphere " + str(i))
    for f in range(sce.frame_start, scene_frames):
        if ((f-1) % 3 == 0):
            sce.frame_set(f)
            x = int(ob.matrix_world.to_translation().x*100 * scale)
            y = int(ob.matrix_world.to_translation().y*100 * scale)
            z = int(ob.matrix_world.to_translation().z*100 * scale)
            for k in range(i+1, number_of_uavs):
                if (k != i):
                    ob2 = bpy.data.objects['Sphere_' + str(k)]
                    x2 = int(ob2.matrix_world.to_translation().x*100 * scale)
                    y2 = int(ob2.matrix_world.to_translation().y*100 * scale)
                    z2 = int(ob2.matrix_world.to_translation().z*100 * scale)
                    dx = x2 - x
                    dy = y2 - y
                    dz = z2 - z
                    d = math.sqrt(dx*dx + dy*dy + dz*dz)
                    if (d < d_treshold):
                        print("Danger! Distance = " + str(round(d/100,2)) + " m between " + str(i) + " and " + str(k) + " on frame " + str(f))
                        
print("\nDone checking distance")
