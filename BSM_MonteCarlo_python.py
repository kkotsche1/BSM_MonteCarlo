import random
import math
import time

class BSM:
    def __init__(self, assPrc, strPrc, gth, vola, yrs, stps, monsims):
        self.bsmAssetPrice = assPrc
        self.bsmStrikePrice = strPrc
        self.bsmMarketGrowth = gth
        self.bsmAssetVol = vola
        self.bsmYrsToExpiry = yrs
        self.bsmSteps = stps
        self.bsmMonteCarloSims = monsims
        self.bsmCallPrice = 0
        self.bsmPutPrice = 0

    def rn(self):
        return random.random()

    def logNormalRandomWalk(self):
        callPayoffPot = 0
        putPayoffPot = 0
        timeStep = self.bsmYrsToExpiry / self.bsmSteps
        sqrtTimeStep = math.sqrt(timeStep)

        for i in range(self.bsmMonteCarloSims):
            assPrice = self.bsmAssetPrice

            for j in range(self.bsmSteps):
                assPrice *= (1 + self.bsmMarketGrowth * timeStep + self.bsmAssetVol * sqrtTimeStep * (sum([self.rn() for _ in range(12)]) - 6))

            if assPrice > self.bsmStrikePrice:
                callPayoffPot += (assPrice - self.bsmStrikePrice)
            elif assPrice < self.bsmStrikePrice:
                putPayoffPot += (self.bsmStrikePrice - assPrice)

        self.bsmCallPrice = callPayoffPot / self.bsmMonteCarloSims
        self.bsmPutPrice = putPayoffPot / self.bsmMonteCarloSims

    # Getter and setter methods can be added here if needed.

# Example usage
if __name__ == "__main__":
    random.seed(time.time())  # Seed for random number generation

    asset_price = 100
    strike_price = 100
    growth = 0.05
    volatility = 0.2
    years = 1
    steps = 256
    simulations = 1000000

    bsm = BSM(asset_price, strike_price, growth, volatility, years, steps, simulations)

    start_time = time.time()

    bsm.logNormalRandomWalk()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Time taken for logNormalRandomWalk: {:.6f} seconds.".format(elapsed_time))
    print("CALL OPTION PRICE:", bsm.bsmCallPrice)
    print("PUT OPTION PRICE:", bsm.bsmPutPrice)
