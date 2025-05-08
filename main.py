# CPSC 323
# Project 4
from leader import *
from cfg_builder import build_cfg
from block import *

if (__name__ == "__main__"):
    tac_code = {}
    filename = 'test_cases/test1.in'

    # Read lines from input and store them
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            tac_code[index + 1] = line

    # print(tac_code)

    # Find Leaders
    leaders = find_leaders(tac_code)
    # print(leaders)

    # Find Blocks
    blocks = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line_num in enumerate(leaders):
            if (index == 0):
                continue
            block = []
            for i in range(leaders[index - 1] - 1, leaders[index] - 1):
                block += [lines[i]]

            blocks.append(block)
        
        # Still need to append last block
        block = []
        for i in range(leaders[-1] - 1, len(tac_code)):
            block += [lines[i]]
        blocks.append(block)
    
    # Print out all blocks
    # for index, block in enumerate(blocks):
    #     print(f"Block {index + 1}:")
    #     print(block)

    # print(blocks)

    # instantiate blocks with line number and its instructions
    list_of_block_nodes = []
    for i, array_of_instruc in enumerate(blocks):
        block_node = Block(i + 1, array_of_instruc)
        list_of_block_nodes.append(block_node)

    for node in list_of_block_nodes:
        print(f"{node.block_number}: {node.instructions}")

    # TO DO: instantiate each node with successor and predecessor to link nodes together


    # Step 3:
    # cfg = build_cfg(blocks, leaders)
    # print("\n=== Control Flow Graph ===")
    # for block_num, successors in cfg.items():
    #     print(f"Block {block_num} -> {successors}")