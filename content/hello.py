


## CREATE METRICS
df['mrevpafGrowthHistorical'] = ((df['mRevPaf'] / df['mRevPafTrailing5Years']) ** (1/5)) - 1

df['mrevpafGrowth'] = ((df['mRevPaffwd3Years'] / df['mRevPaf']) ** (1/3)) - 1

df['gdpGrowthT5YR'] = ((df['gdp'] / df['gdpTrailing5Years']) ** (1/5)) - 1

df['futureRentToOwnGap4Percent'] = df['piti'] - (df['marketEffectiveRentPerUnit'] * 1.04 ** 3)


# New Metrics 

## CREATE METRICS
df['mrevpafGrowthHistorical'] = ((df['mRevPaf'] / df['mRevPafTrailing5Years']) ** (1/5)) - 1

df['mrevpafFutureGrowth'] = ((df['mRevPaffwd3Years'] / df['mRevPaf']) ** (1/3)) - 1

## 
df['mrevpafGrowth1YR'] = ((df['mRevPaf']) / df['mRevPaf'] ** (1/3)) - 1

df['gdpGrowthT5YR'] = ((df['gdp'] / df['gdpTrailing5Years']) ** (1/5)) - 1

df['futureRentToOwnGap4Percent'] = df['piti'] - (df['marketEffectiveRentPerUnit'] * 1.04 ** 3)