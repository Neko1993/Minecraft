import time

@user-code

# This dict holds all the 
variable_dict = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
    }
    
list_of_numbers = [1, 2, 4, 3, 2, 1]
counter = 0  # Counter used for checking how far we're through the message
for bit in list_of_numbers:
    block = variable_dict.get(agent.inspect_data("forward")["data"], "Z")
    counter = counter + 1
    num = decode(block)
    
    if num == None:
        raise Exception("No number given! Please fix your function, or Reset Bit Input and try again.")
        break
    say("Decoded bit as : {}".format(int(num)))
    
    if num != bit:
        say("Incorrect bit given!")
        raise Exception("Incorrect bit! Please fix your function, or Reset Bit Input and try again.")
        break
    else:
        if counter == 6:  # If we recieve the last bit
            say("Received full all the data, task complete!")
            say("Data: 1, 2, 4, 3, 2, 1")
            time.sleep(1)  # Delay to allow the player to see the message be for we complete the task
        else:
            say("Loading Next Bit")
        world.summon("snow_golem", [1007,150,132])
    time.sleep(1)
        
world.summon("snow_golem", [1014,148,132])