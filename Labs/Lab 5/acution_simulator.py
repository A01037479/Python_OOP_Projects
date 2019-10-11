import random


class Auction:
    def __init__(self, bidders, item, starting_price):
        self.bidders = bidders
        self.auctioneer = None
        self.item = item
        self.starting_price = starting_price

    def start_bid(self):
        print('Starting Auction!!\n'
              '------------------')
        starting_bidder = Bidder('Starting Bid', 0, 0, 0, 0)
        self.auctioneer = Auctioneer(self.bidders, self.starting_price,
                                     starting_bidder)
        print(f'Auctioning {self.item} starting at {self.starting_price}')
        for bidder in self.bidders:
            self.auctioneer.attach_bidder(bidder)
        self.auctioneer.notify_bidders()

        if self.auctioneer.highest_current_bidder is not starting_bidder:
            print(f'\nThe winner of the auction is: '
                  f'{self.auctioneer.highest_current_bidder.name} at '
                  f'${self.auctioneer.highest_current_bid}!\n')
        else:
            print(f'\nNo one bidded for the item {self.item}\n')

    def highest_bids(self):
        print('Highest Bids Per Bidder')
        highest_bids_dict = {bidder: bidder.get_highest_bid() for bidder in
                             self.bidders}
        for item in highest_bids_dict.items():
            print(f'Bidder: {item[0].name} Highest Bid: {item[1]}')


class Auctioneer:
    def __init__(self, bidders, highest_current_bid, highest_current_bidder):
        self.bidders = bidders
        self.highest_current_bid = highest_current_bid
        self.highest_current_bidder = highest_current_bidder
        self.observers = []
        self.auction_probability = random.random()

    def name(self):
        return self.name

    def notify_bidders(self):
        for observer in self.observers:
            observer(self)

    def attach_bidder(self, callback):
        self.observers.append(callback)

    def reset_probability(self):
        self.auction_probability = random.random()

    def accept_bid(self, bid, bidder):
        self.highest_current_bid = bid
        self.highest_current_bidder = bidder
        self.reset_probability()
        self.notify_bidders()


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
        if self.bid_increase_perc * auctioneer.highest_current_bid < \
                self.budget and self is not auctioneer.highest_current_bidder \
                and self.bid_probability > auctioneer.auction_probability:
            bid = auctioneer.highest_current_bid * self.bid_increase_perc
            print(f'{self.name} bidded {bid} in response to '
                  f'{auctioneer.highest_current_bidder.name}\'s bid of '
                  f'{auctioneer.highest_current_bid}')
            if bid > self.highest_bid:
                self.highest_bid = bid
            auctioneer.accept_bid(bid, self)

    def get_highest_bid(self):
        return self.highest_bid


def main():
    restart = True
    while restart:
        bid_item = input('\nEnter bid item: ')
        try:
            starting_price = float(input('Enter starting price: '))
            num_bidders = int(input('Enter number of bidders: '))
            bidders = []
            for i in range(0, num_bidders):
                name = input(f'Enter bidder {i + 1}\'s name: ')
                budget = float(input(f'Enter bidder {i + 1}\'s budget: '))
                bid_increase_perc = random.random() + 1
                bidders.append(
                    Bidder(name, budget, random.random(), bid_increase_perc, 0))
            auction = Auction(bidders, bid_item, starting_price)
            auction.start_bid()
            auction.highest_bids()
        except ValueError:
            print('Invalid! Enter integers.')
        else:
            restart = False


if __name__ == '__main__':
    main()
