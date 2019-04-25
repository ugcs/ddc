import bpy
import math
sce = bpy.context.scene
# CHANGE THESE PARAMETERS ACCORDING TO BLENDER ANIMATION
number_of_uavs = 20 # number of uavs in blender scene
scene_frames = 2600 # length of animation in frames

scale = 1.3 # scale of animation found using distance script
speed_treshold = 5.0 # speed treshold in meters per second

# CHANGE BLENDER FRAME RATE TO SPEED UP OR SLOW DOWN THE ANIMATION
# Note: Blender frame rate needs to be divisible with target frame rate
blender_frame_rate = 24 # blender framerate
frame_rate = 4 # target autopilot framerate, default value is 4

l_x = 0
l_y = 0
l_z = 0

print("\nBlender frame rate: " + str(blender_frame_rate))
print("Target frame rate: " + str(frame_rate))

if (blender_frame_rate % frame_rate != 0):
    nth_frame = int(round(blender_frame_rate / frame_rate))
else:
    nth_frame = int(blender_frame_rate / frame_rate)

print("\nChecking every " + str(nth_frame) + "th frame")

print("\nRunning velocity check")

for i in range(0, number_of_uavs):
    ob = bpy.data.objects['Sphere_' + str(i)]
    print("\nChecking Sphere " + str(i))
    for f in range(sce.frame_start, scene_frames):
        if ((f-1) % nth_frame == 0):
            sce.frame_set(f)
            if (f>nth_frame):
                x = ob.matrix_world.to_translation().x * scale
                y = ob.matrix_world.to_translation().y * scale
                z = ob.matrix_world.to_translation().z * scale
                dx = l_x - x
                dy = l_y - y
                dz = l_z - z
                d = math.sqrt(dx*dx + dy*dy + dz*dz)
                s = d * frame_rate
                if (s > speed_treshold):
                    print("Danger! Speed = " + str(round(s,2)) + " m\s for " + str(i) + " on frame " + str(f))
                l_x = x
                l_y = y
                l_z = z
            else:
                l_x = ob.matrix_world.to_translation().x * scale
                l_y = ob.matrix_world.to_translation().y * scale
                l_z = ob.matrix_world.to_translation().z * scale

print("\nDone checking velocity")
