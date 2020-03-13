import bpy
import os
sce = bpy.context.scene
# CHANGE THESE PARAMETERS ACCORDING TO BLENDER ANIMATION
number_of_uavs = 20 # number of uavs in blender scene
scene_frames = 2600 # length of animation in frames
# CHANGE THESE PARAMETERS ACCORDING TO DISTANCE AND VELOCITY SCRIPTS
scale = 1.3 # scale of animation found using distance script
blender_frame_rate = 24 # blender framerate found using velocity script
frame_rate = 4 # target autopilot framerate, default value is 4

print("\nBlender frame rate: " + str(blender_frame_rate))
print("Target frame rate: " + str(frame_rate))

if (blender_frame_rate % frame_rate != 0):
    nth_frame = int(round(blender_frame_rate / frame_rate))
else:
    nth_frame = int(blender_frame_rate / frame_rate)

print("\nCalculating coordinates for every " + str(nth_frame) + "th frame")

path = os.getcwd()
print("\nCurrent directory: " + path + "\n")

try:
        os.mkdir("paths")
except OSError:
        print("Path folder found\n")
else:
        print("Successfully created paths folder\n")

for i in range(0, number_of_uavs):
    ob = bpy.data.objects['Sphere_' + str(i)]
    # create PATH file for every object
    file = open('paths/APM-' + str(i+1) + '.PATH', 'wb')
    # iterate through frames
    for f in range(sce.frame_start, scene_frames):
        if (((f-1) % nth_frame) == 0):
            sce.frame_set(f)
            # get scaled position
            x = int(ob.matrix_world.to_translation().x * 100 * scale)
            y = int(ob.matrix_world.to_translation().y * 100 * scale)
            z = int(ob.matrix_world.to_translation().z * 100 * scale)
            # get color
            r = int(ob.active_material.diffuse_color[0] * 255)
            g = int(ob.active_material.diffuse_color[1] * 255)
            b = int(ob.active_material.diffuse_color[2] * 255)
            file.write((x).to_bytes(2, byteorder='little', signed=True))
            file.write((y).to_bytes(2, byteorder='little', signed=True))
            file.write((z).to_bytes(2, byteorder='little', signed=True))
            file.write((r).to_bytes(2, byteorder='little', signed=True))
            file.write((g).to_bytes(2, byteorder='little', signed=True))
            file.write((b).to_bytes(2, byteorder='little', signed=True))
    print("Path APM-"+ str(i+1)+" exported")
    file.close()

print("\nFinished path file export")
