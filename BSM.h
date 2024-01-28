#include <iostream>

class BSM
{
public:
    BSM(
        float, float, float, float, float, long, long);

    float getBsmAssetPrice();
    float getBsmStrikePrice();
    float getBsmGrowth();
    float getBsmVolatility();
    float getBsmYears();
    long getBsmSteps();
    long getBsmMonteCarloSims();

    void setBsmAssetPrice(float);
    void setBsmStrikePrice(float);
    void setBsmGrowth(float);
    void setBsmVolatility(float);
    void setBsmYears(float);
    void setBsmSteps(long);
    void setBsmMonteCarloSims(long);

    void logNormalRandomWalk();

    double getCallPrice();
    double getPutPrice();

    double rn(); // Function to generate random number

    ~BSM();

private:
    float bsmAssetPrice;
    float bsmStrikePrice;
    float bsmMarketGrowth;
    float bsmAssetVol;
    float bsmYrsToExpiry;
    long bsmSteps;
    long bsmMonteCarloSims;
};