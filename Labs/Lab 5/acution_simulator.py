import random


class Auction:
    def __init__(self, bidders, item, starting_price):
        self.bidders = bidders
        self.auctioneer = None
        self.item = item
        self.starting_price = starting_price

    def start_bid(self):
        self.auctioneer = Auctioneer(self.bidders, self.starting_price, None)
        largest_bidder_probability = 0
        highest_current_bidder = None
        highest_current_bid = 0
        bidding = True
        while bidding:
            bidding = False
            for bidder in self.bidders:
                bidder(self.auctioneer)
                bidder_probability = bidder.bid_probability
                if bidder.enough_budget:
                    bidding = True
                if bidder_probability > largest_bidder_probability:
                    largest_bidder_probability = bidder_probability
                    highest_current_bidder = bidder
                    highest_current_bid = bidder.bid_increase_perc * \
                                          self.auctioneer.highest_current_bid
            if self.auctioneer.highest_current_bidder is None:
                start_bidder = 'Starting'
            else:
                start_bidder = self.auctioneer.highest_current_bidder.name
            print(f'{highest_current_bidder.name} bidded {highest_current_bid} '
                  f'in response to {start_bidder}\'s bid of '
                  f'{self.auctioneer.highest_current_bid}')
            self.auctioneer.accept_bid(highest_current_bid, highest_current_bidder)
        print(f'The winner of the auction is: '
              f'{self.auctioneer.highest_current_bidder.name} at '
              f'${self.auctioneer.highest_current_bid}!')



class Auctioneer:
    def __init__(self, bidders, highest_current_bid, highest_current_bidder):
        self.bidders = bidders
        self.highest_current_bid = highest_current_bid
        self.highest_current_bidder = highest_current_bidder
        self.observers = []

    def accept_bid(self, bid, bidder):
        #self.excute_callbacks()
        self.highest_current_bid = bid
        self.highest_current_bidder = bidder

    def execute_callbacks(self):
        for observer in self.observers:
            observer(self)


    def attach_observer(self, callback):
        self.observers.append(callback)


class Bidder:
    def __init__(self, name, budget, bid_probability, bid_increase_perc,
                 highest_bid):
        self.name = name
        self.budget = budget
        self.bid_probability = bid_probability
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = highest_bid
        self.enough_budget = True

    def update_bid_probability(self):
        self.bid_probability = random.random()

    def __call__(self, auctioneer):
        if auctioneer.highest_current_bidder is not None \
                and self.name == auctioneer.highest_current_bidder.name:
            print(f'{self.name} cant reliate myself')
            self.bid_probability = 0
        elif self.bid_increase_perc*auctioneer.highest_current_bid <= self.budget:
            print(f'{self.name} has budget to bid')
            self.update_bid_probability()
        if self.bid_increase_perc*auctioneer.highest_current_bid > self.budget:
            self.enough_budget = False
            self.bid_probability = 0


def main():
    #bid_item = input('Enter bid item: ')
    bid_item = 'iphone'
    #starting_price = float(input('Enter starting price: '))
    starting_price = 100
    #num_bidders = input('Enter number of bidders: ')
    num_bidders = 2
    bidders = []
    for i in range(0, int(num_bidders)):
        name = input(f'Enter bidder {i + 1}\'s name: ')
        #budget = float(input(f'Enter bidder {i + 1}\'s budget: '))
        budget = 500
        bid_increase_perc = float(input(f'Enter bidder {i + 1}\'s increase %: '))
        bidders.append(
            Bidder(name, budget, 0, bid_increase_perc, 0))
    auction = Auction(bidders, bid_item, starting_price)
    auction.start_bid()




if __name__ == '__main__':
    main()
