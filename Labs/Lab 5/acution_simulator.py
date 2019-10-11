import random


class Auction:
    def __init__(self, bidders, item, starting_price):
        self.bidders = bidders
        self.auctioneer = None
        self.item = item
        self.starting_price = starting_price

    def start_bid(self):
        starting_bidder = Bidder('Starting Bid', 0, 0, 0, 0)
        self.auctioneer = Auctioneer(self.bidders, self.starting_price,
                                     starting_bidder)
        for bidder in self.bidders:
            self.auctioneer.attach_observer(bidder)
        self.auctioneer.execute_callbacks()

        print(f'The winner of the auction is: '
              f'{self.auctioneer.highest_current_bidder.name} at '
              f'${self.auctioneer.highest_current_bid}!')


class Auctioneer:
    def __init__(self, bidders, highest_current_bid, highest_current_bidder):
        self.bidders = bidders
        self.highest_current_bid = highest_current_bid
        self.highest_current_bidder = highest_current_bidder
        self.observers = []
        self.auction_probability = 0.3

    def execute_callbacks(self):  # notify bidders
        for observer in self.observers:
            observer(self)

    def attach_observer(self, callback):
        self.observers.append(callback)

    def set_highest_current_bid(self, bid):
        self.highest_current_bid = bid
        self.auction_probability = random.random()
        self.execute_callbacks()


class Bidder:
    def __init__(self, name, budget, bid_probability, bid_increase_perc,
                 highest_bid):
        self.name = name
        self.budget = budget
        self.bid_probability = bid_probability
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = highest_bid

    def update_bid_probability(self):
        self.bid_probability = random.random()

    def __call__(self, auctioneer):
        self.update_bid_probability()
        if self.bid_increase_perc * auctioneer.highest_current_bid < self.budget and \
                self is not auctioneer.highest_current_bidder and \
                self.bid_probability > auctioneer.auction_probability:
            # print(f'---{self.name} has budget to bid')
            bid = auctioneer.highest_current_bid * self.bid_increase_perc
            print(f'{self.name} bidded {bid} in response to '
                  f'{auctioneer.highest_current_bidder.name}\'s bid of '
                  f'{auctioneer.highest_current_bid}')
            if bid > self.highest_bid:
                self.highest_bid = bid
            auctioneer.highest_current_bidder = self
            auctioneer.set_highest_current_bid(bid)


def main():
    # bid_item = input('Enter bid item: ')
    bid_item = 'iphone'
    # starting_price = float(input('Enter starting price: '))
    starting_price = 100
    # num_bidders = input('Enter number of bidders: ')
    num_bidders = 10
    bidders = []
    for i in range(0, int(num_bidders)):
        name = input(f'Enter bidder {i + 1}\'s name: ')
        # budget = float(input(f'Enter bidder {i + 1}\'s budget: '))
        budget = 2000
        bid_increase_perc = float(
            input(f'Enter bidder {i + 1}\'s increase %: '))
        bidders.append(
            Bidder(name, budget, random.random(), bid_increase_perc, 0))
    auction = Auction(bidders, bid_item, starting_price)
    auction.start_bid()


if __name__ == '__main__':
    main()
