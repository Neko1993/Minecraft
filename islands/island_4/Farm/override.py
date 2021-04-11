def check_flower(direction: str):
    block = agent.inspect(direction)
    block_data = agent.inspect_data(direction)
    flower_list = {
        0: 'poppy',
        1: 'blue_orchid',
        2: 'allium',
        3: 'houstonia',
        4: 'red_tulip',
        5: 'orange_tulip',
        6: 'white_tulip',
        7: 'pink_tulip',
        8: 'oxeye_daisy',
        9: 'cornflower',
        10: 'lily_of_the_valley',
        }
    if block == 'red_flower':
        return flower_list.get(block_data['data'], block)
    else:
        return block
    
@user-code
        