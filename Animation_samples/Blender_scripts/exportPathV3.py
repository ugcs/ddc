import bpy
sce = bpy.context.scene
number_of_uavs = 20
scale = 1.0 # centimeters in one position unit (default value = 1.0, means one unit = one centimeter. larger scale - larger dance)
scene_frames = 2600 # scene frame length 
position_frame_rate = 8 # our target, autopilot, position framerate. Path files will be exported only if blender_frame_rate is devisable by this value
color_frame_rate = 24 # our target, autopilot, color framerate. Path files will be exported only if blender_frame_rate is devisable by this value
blender_frame_rate = 24 # blender framerate
pos = [[]] # array of uavs and coordinates
col = [[]] # array of uavs and colors

allow_generate = True

if ((blender_frame_rate % position_frame_rate) != 0):
    print("blender_frame_rate should be divided by position_frame_rate.")
    allow_generate = False

if ((blender_frame_rate % color_frame_rate) != 0):
    print("blender_frame_rate should be divided by color_frame_rate.")
    allow_generate = False

if (allow_generate):
    # init arrays
    for i in range(0, number_of_uavs):
        pos.append([])
        col.append([])
    # get positions and colors from scene
    for f in range(sce.frame_start, scene_frames): 
        save_position = ((f-1) % (blender_frame_rate / position_frame_rate) == 0)
        save_color = ((f-1) % (blender_frame_rate / color_frame_rate) == 0)
        if (save_position or save_color):
            sce.frame_set(f)
            for i in range(0, number_of_uavs):
                ob = bpy.data.objects["Sphere_" + str(i)]
                if (save_position):
                    p = [0,0,0]
                    # get position from blender scene and convert it to centimeters
                    p[0] = int(ob.matrix_world.to_translation()[0] * 100)
                    p[1] = int(ob.matrix_world.to_translation()[1] * 100) 
                    p[2] = int(ob.matrix_world.to_translation()[2] * 100) 
                    pos[i].append(p)          
                if (save_color):
                    c = [0,0,0]
                    # get colors from blender scene and convert it from float[0,1] to int[0,255] interval
                    c[0] = int(ob.active_material.diffuse_color[0] * 255)
                    c[1] = int(ob.active_material.diffuse_color[1] * 255)
                    c[2] = int(ob.active_material.diffuse_color[2] * 255)
                    col[i].append(c)     
    # save positions and colors to files
    for i in range(0, number_of_uavs):
        # write header
        file = open('c:/path/DSS-' + str(i+1) + '.PATH3', 'wb')
        # l = <- for supress blender console output
        l = file.write("DP".encode()) #magic bytes
        l = file.write((3).to_bytes(1, byteorder='little', signed=True)) # format version
        l = file.write((14).to_bytes(1, byteorder='little', signed=True)) # header size
        l = file.write((0).to_bytes(4, byteorder='little', signed=True)) # crc. if zero it will be calculated in DSS Client later
        l = file.write((0).to_bytes(2, byteorder='little', signed=True)) # reserved
        l = file.write(int(scale * 10).to_bytes(2, byteorder='little', signed=False)) # millmeteres in unit (so we multiply by ten). Here is one unit = 10 millimeters
        l = file.write((2).to_bytes(1, byteorder='little', signed=True)) # section count (we have two: position and colors)
        l = file.write((8).to_bytes(1, byteorder='little', signed=True)) # section header size
        # section 1 header
        l = file.write((1).to_bytes(1, byteorder='little', signed=True)) # section type 1 means positions
        l = file.write((0).to_bytes(1, byteorder='little', signed=True)) # reserved
        l = file.write((position_frame_rate * 1000).to_bytes(2, byteorder='little', signed=False)) # section FPS
        l = file.write((len(pos[i]) * 6).to_bytes(4, byteorder='little', signed=False)) # section size in bytes. 6 is the size of block: 2bytes * 3coordinates.
        # section 2 header
        l = file.write((2).to_bytes(1, byteorder='little', signed=True)) # section type 2 means colors
        l = file.write((0).to_bytes(1, byteorder='little', signed=True)) # reserved
        l = file.write((color_frame_rate * 1000).to_bytes(2, byteorder='little', signed=False)) # section FPS
        l = file.write((len(col[i]) * 3).to_bytes(4, byteorder='little', signed=False)) # section size in bytes. 3 is the size of block: 1byte * 3values.
        # fill section 1 with positions
        for p in pos[i]:
            for x in p:
                l = file.write((x).to_bytes(2, byteorder='little', signed=True))
        # fill section 2 with colors
        for c in col[i]:
            for x in c:
                if (x > 255):
                    x = 255
                l = file.write((x).to_bytes(1, byteorder='little', signed=False)) # unsigned!
        file.close()
else:
    print("ERROR! Path files were not generated!")


    