import hashlib

# basic block

class Block:
    def __init__(self, blockData, previousBlockHash):
        # `blockData` must be BlockData type
        # `previousBlockHash` should be previous hash, (ex: previousBlock.getHash())
        self.blockData = blockData
        self.previousBlockHash = previousBlockHash

    def getTuple(self):
        return (self.blockData.getTuple(), self.previousBlockHash)

    def getHash(self):
        hashId = hashlib.md5()
        toHash = self.getTuple()
        hashId.update(repr(toHash).encode('utf-8'))
        return hashId.hexdigest()

    # returns BlockData object
    def getBlockData(self):
        return self.blockData
