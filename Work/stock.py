
class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    __slots__ = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares

s = Stock("veis", "22", 5100)
print(s)
s.__dict__