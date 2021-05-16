
import hashlib
from block import Block
from blockData import BlockData

block1Data = BlockData(1211, "Jeremy")
block2Data = BlockData(1334, "Henry")

block1 = Block(block1Data, None)
block2 = Block(block2Data, block1.getHash())

print("Block 1 hash: " + str(block1.getHash()))
print("Block 2 hash: " + str(block2.getHash()))
