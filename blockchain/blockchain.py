# central blockchain

from blockData import BlockData  # BlockData class
from block import Block         # Block class

blockchain = []

# add a new block to the blockchain
# returns the new block it created


def addNewBlock(transactionType, success, mineInt, catchInt, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin):
    blockData = BlockData(transactionType, success, mineInt, catchInt,
                          encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin)
    previousBlockHash = None
    if len(blockchain) > 0:
        previousBlockHash = blockchain[len(blockchain)-1].getHash()

    newBlock = Block(blockData, previousBlockHash)
    blockchain.append(newBlock)
    return newBlock


def printBlockchain():
    for i in range(len(blockchain)):
        block = blockchain[i]
        print("===== Block " + str(i+1) + " =====")
        print("Hash: " + block.getHash())
        print("BlockData: " + str(block.getBlockData().getTuple()))
        print("Previous Hash: " + str(block.getPreviousHash()))
        print()
