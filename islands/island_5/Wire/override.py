def correct_location(location_input):
    x = int(location_input.x)
    y = int(location_input.y)-1
    z = int(location_input.z)
    return x,y,z

@user-code

# This function forces the code to exit as the code builder can't exit it
@forever
def end_task():
    # If the BP adds an emerald block to this location we know the task is complete
    if world.is_block([1021, 154, 60], "emerald_block"):
        exit(0)