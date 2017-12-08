class OrderbookEntry(object):

    def __init__(self, price, qty):
        self.price = price
        self.qty = qty

    def __str__(self):
        return str(self.price) + ": " + str(self.qty)

    def __repr__(self):
        return str(self)

    def getPrice(self):
        return self.price

    def getQty(self):
        return self.qty


class OrderbookState(object):

    def __init__(self, tradePrice=0.0):
        self.tradePrice = tradePrice
        self.buyers = []
        self.sellers = []

    def __str__(self):
        s = ""
        s = s + "Price: " + str(self.tradePrice) + "\n"
        s = s + "Buyers: " + str(self.buyers) + "\n"
        s = s + "Sellers: " + str(self.sellers)
        return s

    def __repr__(self):
        return str(self)

    def setTradePrice(self, tradePrice):
        self.tradePrice = tradePrice

    def addBuyer(self, entry):
        self.buyers.append(entry)

    def addBuyers(self, entries):
        for entry in entries:
            self.buyers.append(entry)

    def addSeller(self, entry):
        self.sellers.append(entry)

    def addSellers(self, entries):
        for entry in entries:
            self.sellers.append(entry)

    def getBuyers(self):
        return self.buyers

    def getSellers(self):
        return self.sellers

    def getBidAskMid(self):
        firstBuy = self.getBuyers()[0]
        firstSell = self.getSellers()[0]
        return (firstBuy.getPrice() + firstSell.getPrice()) / 2.0


class Orderbook(object):

    def __init__(self):
        self.states = []

    def __str__(self):
        s = ''
        i = 1
        for state in self.states:
            s = s + 'State ' + str(i) + "\n"
            s = s + '-------' + "\n"
            s = s + str(state)
            s = s + "\n\n"
            i = i + 1
        return s

    def __repr__(self):
        return str(self)

    def addState(self, state):
        self.states.append(state)

    def addStates(self, states):
        for state in states:
            self.states.append(state)

    def getStates(self):
        return self.states

    def getState(self, index):
        if len(self.states) <= index:
            raise Exception('Index out of orderbook state.')
        return self.states[index]