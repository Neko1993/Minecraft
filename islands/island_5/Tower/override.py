import time

def draw_square(size: int):
    for direction in ["forward","right","back","left"]:
        for position in range(0,size-1):
            agent.place(1,"down")
            agent.move(direction)

@user-code

agent.teleport([1018,159,79], [1018,159,76])
build_tower()

time.sleep(2)
timer = 0
while timer < 30:
    # The MC Function places a emerald block if the code is allowed to build the 2 support towers
    if world.is_block([1027,154,60], "emerald_block"):
        # Tower A
        agent.teleport([1009,159,70], [1009,159,66])
        build_tower()
        # Tower B
        agent.teleport([1027,159,70], [1027,159,66])
        build_tower()
        break
    # if a nether wart block is placed, then there's an error with the tower and we raise an issue
    if world.is_block([1027,154,60], "nether_wart_block"):
        say("There seems to be an issue with your tower")
        raise Exception("Issue with your build_tower, please fix")
    else:
        time.sleep(1)
        timer = timer + 1
# If the timer reaches 30(seconds) we time out and say there's an issue
if timer == 30:
    say("There seems to be an issue with your tower function")
    say("Reset the tower with the builder and start again")
    raise Exception("Issue with your build_tower, please fix")