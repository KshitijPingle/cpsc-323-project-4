# CPSC 323
# Project 4
from leader import *
from block import *
from link_blocks import *
from get_definitions import *
from get_gen_kill_sets import *
from get_used_sets import *
from get_in_out_sets import *
from forward_analysis import *
from backward_analysis import *
from output_cfg import *

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
    # print(f"leaders: {leaders}")
    # print(f"size: {len(leaders)}")

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
    #     print(f"Block {index + 1}: {block}")

    # print(blocks)

    ####################################################################################################################
    # TO DO: implement data flow analysis using the CFG: forward, reaching definitions
    list_of_block_nodes = []

    # instantiate blocks with line number and its instructions and append to array
    for i, array_of_instruc in enumerate(blocks):
        block_node = Block(i + 1, array_of_instruc)
        list_of_block_nodes.append(block_node)

    # instantiate starting number for each blocks (line number for leaders)
    for index_for_leaders, block in enumerate(list_of_block_nodes):
        block.start_line_number = leaders[index_for_leaders]

    # links successors and predecessors for each block via jump targets, and fall throughs
    link_blocks(list_of_block_nodes)

    all_definitions = get_definitions(list_of_block_nodes)

    # reminder:
    #           GEN = new definitions in the block
    #           KILL = definitions from other blocks of the same variable as the current block's GEN
    gen, kill = get_gen_kill_sets(list_of_block_nodes, all_definitions)
    used = get_used_sets(list_of_block_nodes)
    # print(kill)

    # instantiate gen, kill, and used sets to each block
    for index, block in enumerate(list_of_block_nodes):
        block.gen_sets = gen[index + 1]
        block.kill_sets = kill[index + 1]
        block.used_sets = used[index + 1]

    # print(gen[5])

    # compute reaching definition for forward data flow analysis
    forward_analysis(list_of_block_nodes)

    ####################################################################################################################
    # TO DO: implement data flow analysis using the CFG: backward, live variables
    backward_analysis(list_of_block_nodes)

    ####################################################################################################################
    # TO DO: output CFG

    # CFG is a graph, not a tree.
    # therefore, printing as a ASCII tree like project 2 would not be appropriate.
    # block is reached from multiple paths and are not linear

    output_cfg(list_of_block_nodes)
