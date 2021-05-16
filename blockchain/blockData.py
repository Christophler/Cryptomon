
# block data will be dependent on how we design the game
class BlockData:
    def __init__(self, transactionType, success, mineInt, catchInt, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin):
        # `transactionType` transaction type (str types: mine, validate, sell)
        # `success` (bool True or False)
        # `mineInt`, `catchInt`, `encounter`, `numGraphicCards`, `numDogecoin`, `numEthereum`, `numBitcoin` global variables
        self.transactionType = transactionType
        self.success = success
        self.mineInt, self.catchInt, self.encounter, self.numGraphicCards, self.numDogecoin, self.numEthereum, self.numBitcoin = mineInt, catchInt, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin

    def getTuple(self):
        # tuple should consist of the data that will affect the hash
        tup = (self.transactionType, self.success, self.mineInt, self.catchInt, self.encounter, self.numGraphicCards, self.numDogecoin, self.numEthereum, self.numBitcoin)
        return tup