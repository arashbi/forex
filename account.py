from enum import Enum
import math

from matplotlib import pyplot as plt
import numpy as np  # linear algebra


class Trade:

    def __init__(self, size, price: float, long: int, short: int):
        self.size = size
        self.price = price
        self.long = long
        self.short = short

    def __str__(self):
        return f"Trade: {self.size} at {self.price} "


def normalize(arr):
    m = np.max([math.fabs(a) for a in arr])
    n = arr / m
    return n



class Wallet:
    def __init__(self):
        self.trades: list[Trade] = []
        self.avg_prices: list[float] = [0]
        self.positions: list[int] = [0]
        self._profits: list[float] = [0]
        self.step = 0
        self.dollars: list[float] = [0]
        self.euros: list[int] = [0]

    def trade(self, price: float, size: int, long: int, short: int):
        if self.last_position() + size > 100:
            size = 100 - self.last_position()
        elif self.last_position() + size < -100:
            size = 100 + self.last_position()
        new_step = self.step + 1
        t = Trade(size, price, long, short)
        self.trades.append(t)
        self.calculate_profit1(t)
        self.step = new_step

    def calculate_avg_price(self, total_positions, price, size, closed_positions):
        if closed_positions == 0:
            if total_positions == 0:
                avg_price = 0
            else:
                avg_price = (self.avg_prices[self.step] * self.positions[
                    self.step] + price * size) / total_positions
        elif total_positions == 0:
            avg_price = 0
        elif math.fabs(size) > math.fabs(self.positions[self.step]):
            avg_price = price
        else:
            avg_price = self.last_avg_price()

        return avg_price

    def calculate_profit1(self, trade: Trade):
        self.euros.append(self.euros[self.step] + trade.size)
        self.dollars.append(self.dollars[self.step] - trade.size * trade.price)
        self._profits.append(self.dollars[self.step] + self.euros[self.step] * trade.price)

    def calculate_profit(self, trade: Trade):
        if self.last_position() == 0:
            return 0, self.last_profit()
        if trade.size * self.positions[self.step] >= 0:
            return 0, self._profits[self.step]
        closing_positions = math.fabs(self.positions[self.step]) \
            if math.fabs(trade.size) > math.fabs(self.positions[self.step]) \
            else math.fabs(trade.size)
        result = self._profits[self.step] + closing_positions * \
                 (-1 if trade.size > 0 else 1) * (trade.price - self.avg_prices[self.step])
        return closing_positions, round(result, 2)

    def close(self, price: float, ):
        self.trade(price, self.last_position() * -1, 0, 0)

    def profits(self):
        return self._profits

    def last_profit(self):
        return self._profits[len(self._profits) - 1]

    def last_position(self):
        return self.euros[len(self.euros) - 1]

    def last_avg_price(self):
        return round(self.avg_prices[len(self.avg_prices) - 1], 2)

    def __str__(self):
        return f"wallet ${self.avg_prices[self.step]} * {self.positions[self.step]} at " \
               f"{round(self._profits[self.step], 2)}"

    def print(self, title):
        max_positions = [math.fabs(x) for x in self.euros]
        max_position = np.amax(max_positions)
        print(f"{title} total profit {self.last_profit()}")
        print(f"{title} Number of trades {len(self.trades)}")
        print(f"{title} max open positions {max_position}")

    def draw(self, title):
        plt.style.use('_mpl-gallery')
        # make data
        x = np.linspace(0, len(self.profits()), len(self.profits()))
        fig, ax = plt.subplots()
        fig.set_size_inches(18.5, 4.5)
        ax.set_title(f"Formula: {title}", color='C0')
        longs = list(map(lambda t: t.long, self.trades))
        longs.append(len(longs) - 1)
        shorts = list(map(lambda t: t.short, self.trades))
        shorts.append(len(shorts) - 1)

        positions = [(i / (i + j)) - 0.5 if i + j != 0 else 0 for i, j in zip(longs, shorts)]
        normalized_positions = positions

        ax.plot(x, normalize(self._profits), linewidth=2.0, label="profit", color='red')
        ax.plot(x, normalize(self.euros), linewidth=1.0, label="positions", color='yellow' )
        p1 = ax.bar(x, normalize(self.euros), 3,  label='bs')
        ax.plot(x, normalized_positions, linewidth=3.0, label="all positions", color="green")

        ps = list(map(lambda t: t.price * 10000 - 10000, self.trades))
        ps.append(ps[len(ps) - 1])
        print(f"{title} total profit {self.last_profit()}")
        max_positions = [math.fabs(x) for x in self.euros]
        max_position = np.amax(max_positions)
        print(f"{title} Number of trades {len(self.trades)}")
        print(f"{title} max open positions {max_position}")
        normalized_price = normalize(ps)
        ax.plot(x, normalized_price, linewidth=1.0, label="prices", color='black')
        ax.legend()
        return ax


def simulate(bid_prices, ask_prices, longs, shorts, functions):
    wallet= Wallet()
    l = len(ask_prices)
    for i in range(l):
        for f in functions:
            size = f(ask_prices, longs, shorts, i)
            wallet.trade(bid_prices[i], size, longs[i], shorts[i])
    return wallet

