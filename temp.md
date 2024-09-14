# Real Estate Investment Coding Challenge

Author: Remi Jonathan Choquette

## Problem Statement

You are tasked with analyzing a dataset of potential real estate investments to determine the best property to invest in. Each property has different attributes that affect its investment potential. Additionally, each property may have dependencies on other properties, meaning certain properties must be considered before others. Your goal is to create a function that identifies the property with the highest investment score, taking into account these dependencies.

In real estate investment, certain properties may have dependencies on others due to zoning laws, development plans, or financial strategies. For example, investing in a commercial property might require prior investment in adjacent residential properties to meet local zoning requirements or to facilitate infrastructure improvements. Similarly, a multi-property development project might require sequential investment to ensure proper phasing and resource allocation. However, properties that depend on other high-quality properties may become less desirable due to increased competition and crowding effects.

### Dataset

The dataset is a list of dictionaries, where each dictionary represents a property. Each property has the following attributes:

- `property_id` (string): A unique identifier for the property.
- `price` (float): The purchase price of the property in dollars.
- `rent` (float): The monthly rental income from the property in dollars.
- `maintenance_cost` (float): The monthly maintenance cost for the property in dollars.
- `location_score` (float): A score between 0 and 10 indicating the desirability of the property's location.
- `projected_appreciation` (float): The annual projected appreciation rate of the property in percentage.
- `market_trend` (float): A score between -10 and 10 indicating the current market trend for the location. Note: For Collection 5, this value is `"unknown"` for every property.
- `dependencies` (list): A list of `property_id` strings that must be considered before this property.

### Investment Score Calculation

The investment score for each property is calculated using a combination of its base investment score and the investment scores of its dependent properties. This calculation is defined as follows:

$$
\text{investment\_score(property)} = \text{base\_investment\_score(property)}
$$
$$
    + \sum \left\{ f(\text{investment\_score(dep\_property)} \text{} \right\} 
$$

Where:

- The base investment score is calculated using the following formula:

$$
\text{base\_investment\_score} = \left( \frac{\text{rent} - \text{maintenance\_cost}}{\text{price}} \right) \times
\text{location\_score}
$$
$$
\times \left( 1 + \text{projected\_appreciation} \right) \times \left( 1 + \left( \frac{\text{market\_trend}}{10}
\right) \right)
$$

- The function (_f_) is a non-linear or non-increasing function where `x` is the investment score and `n` is the number of properties considered

$$ f(x, n)=- \frac{\sqrt{x}}{n} $$

If `x` is negative, it can be considered to be equal to 0.

### Input

- `properties`: A list of dictionaries, where each dictionary contains the attributes of a property as described above.

### Output

- Return the `property_id` of the property with the highest investment score, considering dependencies.
- Should an error be contained with the set, this component of the set and any depending members should be ignored for solving that collection of the problem.

### Example

```python
properties = [
    {
        "property_id": "P1", # score 0.068289
        "price": 200000,
        "rent": 1500,
        "maintenance_cost": 200,
        "location_score": 8.5,
        "projected_appreciation": 0.03,
        "market_trend": 2.0,
        "dependencies": []
    },
    {
        "property_id": "P2", # score 0.623198359105106
        "price": 15000,
        "rent": 1200,
        "maintenance_cost": 150,
        "location_score": 9.0,
        "projected_appreciation": 0.04,
        "market_trend": 3.5,
        "dependencies": ["P1"]
    },
    {
        "property_id": "P3", # score -0.4748853879215606
        "price": 250000,
        "rent": 1800,
        "maintenance_cost": 300,
        "location_score": 7.5,
        "projected_appreciation": 0.02,
        "market_trend": 1.0,
        "dependencies": ["P1", "P2"]
    }
]

print(best_investment_property(properties))  # Expected output: "P2"
```

## Test Collections

### Collection 1

```python
properties_1 = [
    {
        "property_id": "A1",
        "price": 449557.98,
        "rent": 2909.23,
        "maintenance_cost": 430.69,
        "location_score": 7.96,
        "projected_appreciation": 0.02,
        "market_trend": -7.13,
        "dependencies": []
    },
    {
        "property_id": "A2",
        "price": 403483.26,
        "rent": 2743.92,
        "maintenance_cost": 231.66,
        "location_score": 8.79,
        "projected_appreciation": 0.05,
        "market_trend": 13.77,
        "dependencies": []
    },
    {
        "property_id": "A3",
        "price": 462249.94,
        "rent": 2577.77,
        "maintenance_cost": 372.34,
        "location_score": 7.08,
        "projected_appreciation": 0.04,
        "market_trend": 1.85,
        "dependencies": []
    },
    {
        "property_id": "A4",
        "price": 452794.75,
        "rent": 2532.68,
        "maintenance_cost": 412.0,
        "location_score": 8.76,
        "projected_appreciation": 0.02,
        "market_trend": -4.03,
        "dependencies": []
    },
    {
        "property_id": "A5",
        "price": 109755.92,
        "rent": 1705.57,
        "maintenance_cost": 171.24,
        "location_score": 1.25,
        "projected_appreciation": 0.1,
        "market_trend": -1.32,
        "dependencies": []
    }
]
```

### Collection 2

```python
properties_2 = [
    {
        "property_id": "B8",
        "price": 320000,
        "rent": 2700,
        "maintenance_cost": 320,
        "location_score": 9.2,
        "projected_appreciation": 0.09,
        "market_trend": 4.5,
        "dependencies": []
    },
    {
        "property_id": "B1",
        "price": 15000,
        "rent": 1400,
        "maintenance_cost": 150,
        "location_score": 6.8,
        "projected_appreciation": 0.02,
        "market_trend": 1.0,
        "dependencies": ["B4"]
    },
    {
        "property_id": "B2",
        "price": 18000,
        "rent": 1600,
        "maintenance_cost": 180,
        "location_score": 7.0,
        "projected_appreciation": 0.03,
        "market_trend": 1.5,
        "dependencies": ["B6", "B7"]
    },
    {
        "property_id": "B4",
        "price": 22000,
        "rent": 1900,
        "maintenance_cost": 220,
        "location_score": 8.0,
        "projected_appreciation": 0.05,
        "market_trend": 10,
        "dependencies": ["B8"]
    },
    {
        "property_id": "B6",
        "price": 280000,
        "rent": 2300,
        "maintenance_cost": 280,
        "location_score": 8.8,
        "projected_appreciation": 0.07,
        "market_trend": 3.5,
        "dependencies": []
    },
    {
        "property_id": "B7",
        "price": 300000,
        "rent": 2500,
        "maintenance_cost": 300,
        "location_score": 9.0,
        "projected_appreciation": 0.08,
        "market_trend": 4.0,
        "dependencies": []
    },
    {
        "property_id": "B3",
        "price": 200000,
        "rent": 1700,
        "maintenance_cost": 200,
        "location_score": 7.5,
        "projected_appreciation": 0.04,
        "market_trend": 2.0,
        "dependencies": []
    },
    {
        "property_id": "B5",
        "price": 25000,
        "rent": 2100,
        "maintenance_cost": 250,
        "location_score": 8.5,
        "projected_appreciation": 0.06,
        "market_trend": 3.0,
        "dependencies": ["B3"]
    }
]
```

### Collection 3

```python
properties_3 = [
    {
        "property_id": "C4",
        "price": 480000,
        "rent": 3900,
        "maintenance_cost": 480,
        "location_score": 9.3,
        "projected_appreciation": 0.07,
        "market_trend": 4.2,
        "dependencies": ["C2"]
    },
    {
        "property_id": "C2",
        "price": 450000,
        "rent": 3700,
        "maintenance_cost": 450,
        "location_score": 9.0,
        "projected_appreciation": 0.07,
        "market_trend": 4.0,
        "dependencies": ["C5", "C7"]
    },
    {
        "property_id": "C7",
        "price": 540000,
        "rent": 4300,
        "maintenance_cost": 540,
        "location_score": 9.7,
        "projected_appreciation": 0.09,
        "market_trend": 4.7,
        "dependencies": ["C6"]
    },
    {
        "property_id": "C1",
        "price": 5000000,
        "rent": 4000,
        "maintenance_cost": 500,
        "location_score": 9.5,
        "projected_appreciation": 0.08,
        "market_trend": 4.5,
        "dependencies": []
    },
    {
        "property_id": "C6",
        "price": 520000,
        "rent": 4100,
        "maintenance_cost": 520,
        "location_score": 9.6,
        "projected_appreciation": 0.08,
        "market_trend": 4.6,
        "dependencies": ["C4"]
    },
    {
        "property_id": "C5",
        "price": 460000,
        "rent": 3800,
        "maintenance_cost": 460,
        "location_score": 9.1,
        "projected_appreciation": 0.07,
        "market_trend": 4.1,
        "dependencies": ["C4"]
    },
    {
        "property_id": "C8",
        "price": 56000,
        "rent": 4500,
        "maintenance_cost": 560,
        "location_score": 9.8,
        "projected_appreciation": 0.1,
        "market_trend": 4.8,
        "dependencies": ["C1", "C3"]
    },
    {
        "property_id": "C3",
        "price": 420000,
        "rent": 3500,
        "maintenance_cost": 420,
        "location_score": 8.8,
        "projected_appreciation": 0.06,
        "market_trend": 3.5,
        "dependencies": []
    }
]
```

### Collection 4

```python
properties_4 = [
    {
        "property_id": "D5",
        "price": 3800,
        "rent": 3400,
        "maintenance_cost": 380,
        "location_score": 8.7,
        "projected_appreciation": 0.05,
        "market_trend": 3.2,
        "dependencies": ["D4"]
    },
    {
        "property_id": "D3",
        "price": 310000,
        "rent": 3000,
        "maintenance_cost": 310,
        "location_score": 8.0,
        "projected_appreciation": 0.03,
        "market_trend": 2.5,
        "dependencies": []
    },
    {
        "property_id": "D4",
        "price": 400000,
        "rent": 3500,
        "maintenance_cost": 400,
        "location_score": 9.0,
        "projected_appreciation": 0.06,
        "market_trend": 3.5,
        "dependencies": ["D2", "D3"]
    },
    {
        "property_id": "D2",
        "price": 330000,
        "rent": 3100,
        "maintenance_cost": 330,
        "location_score": 8.3,
        "projected_appreciation": 0.04,
        "market_trend": 2.8,
        "dependencies": []
    },
    {
        "property_id": "D7",
        "price": 440000,
        "rent": 3800,
        "maintenance_cost": 440,
        "location_score": 9.3,
        "projected_appreciation": 0.08,
        "market_trend": 4.0,
        "dependencies": ["D6"]
    },
    {
        "property_id": "D1",
        "price": 350000,
        "rent": 3200,
        "maintenance_cost": 350,
        "location_score": 8.5,
        "projected_appreciation": 0.05,
        "market_trend": 3.0,
        "dependencies": ["D8"]
    },
    {
        "property_id": "D8",
        "price": 460000,
        "rent": 4000,
        "maintenance_cost": 460,
        "location_score": 9.5,
        "projected_appreciation": 0.09,
        "market_trend": 4.2,
        "dependencies": ["D7"]
    },
    {
        "property_id": "D6",
        "price": 420000,
        "rent": 3600,
        "maintenance_cost": 420,
        "location_score": 9.2,
        "projected_appreciation": 0.07,
        "market_trend": 3.7,
        "dependencies": []
    }
]
```
## Additional Challenge: Predicting Market Trends


For Collection 5, the `market_trend` values are unknown. Your task is to predict these values using machine learning techniques. You will be provided with two CSV files: `known.csv` and `unknown.csv`. 

### Collection 5

```python
properties_5 = [
    {
        "property_id": "E4",
        "price": 330000,
        "rent": 2800,
        "maintenance_cost": 330,
        "location_score": 8.2,
        "projected_appreciation": 0.06,
        "market_trend": "unknown",
        "dependencies": ["E6", "E7"]
    },
    {
        "property_id": "E1",
        "price": 275000,
        "rent": 2500,
        "maintenance_cost": 275,
        "location_score": 7.5,
        "projected_appreciation": 0.04,
        "market_trend": "unknown",
        "dependencies": ["E4"]
    },
    {
        "property_id": "E8",
        "price": 410000,
        "rent": 3200,
        "maintenance_cost": 410,
        "location_score": 0.1,
        "projected_appreciation": 0.1,
        "market_trend": "unknown",
        "dependencies": ["E7"]
    },
    {
        "property_id": "E2",
        "price": 290000,
        "rent": 2600,
        "maintenance_cost": 290,
        "location_score": 7.8,
        "projected_appreciation": 0.05,
        "market_trend": "unknown",
        "dependencies": ["E4", "E5"]
    },
    {
        "property_id": "E7",
        "price": 390000,
        "rent": 310,
        "maintenance_cost": 390,
        "location_score": 8.9,
        "projected_appreciation": 0.09,
        "market_trend": "unknown",
        "dependencies": []
    },
    {
        "property_id": "E3",
        "price": 310000,
        "rent": 2700,
        "maintenance_cost": 310,
        "location_score": 8.0,
        "projected_appreciation": 0.05,
        "market_trend": "unknown",
        "dependencies": ["E5"]
    },
    {
        "property_id": "E6",
        "price": 370000,
        "rent": 3000,
        "maintenance_cost": 370,
        "location_score": 0.7,
        "projected_appreciation": 0.08,
        "market_trend": "unknown",
        "dependencies": []
    },
    {
        "property_id": "E5",
        "price": 350000,
        "rent": 290,
        "maintenance_cost": 350,
        "location_score": 8.5,
        "projected_appreciation": 0.07,
        "market_trend": "unknown",
        "dependencies": ["E7", "E8"]
    }
]
```

The `known.csv` file contains historical data with all features and the `market_trend` label, while the `unknown.csv` file contains only the features without the `market_trend` label. The columns in these CSV files are as follows:

- `property_id` (string): A unique identifier for the property.
- `market_trend_t_minus_3` (float): A score between -10 and 10 indicating the market trend from three years ago.
- `market_trend_t_minus_2` (float): The market trend from two years ago.
- `market_trend_t_minus_1` (float): The market trend from the previous year.
- `fear_index` (float): A value between 0 and 1 indicating the fear of losing money on the property.
- `price` (float): The price of the property in dollars.
- `property_type` (string): One of `studio`, `3-1/2`, or `4-1/2`.
- `market_trend` (float): The market trend for the current year (available only in `known.csv`).

### Sample of rows

#### known.csv (full data is given in the link)
```csv
property_id,market_trend_t_minus_3,market_trend_t_minus_2,market_trend_t_minus_1,fear_index,price,property_type,market_trend
0,0.2,2.9,3.5,0.57,473000,3-1/2,3.7
1,0.3,2.6,2.6,0.11,353000,3-1/2,3.8
2,0.1,1.8,4.3,0.7,388000,4-1/2,2.8
3,0.1,2.2,3.1,0.36,486000,3-1/2,2.8
```

#### unknown.csv (full data is given in the link)
```csv
property_id,market_trend_t_minus_3,market_trend_t_minus_2,market_trend_t_minus_1,fear_index,price,property_type
E1,-0.0,1.4,4.0,0.5,275000,studio
E2,0.7,2.7,3.2,0.72,290000,studio
E3,0.4,1.1,3.9,0.37,310000,3-1/2
E4,0.0,1.8,3.5,0.27,330000,3-1/2
E5,0.3,3.0,3.1,0.5,350000,4-1/2
E6,-0.4,1.0,4.1,0.01,370000,4-1/2
E7,0.5,3.1,3.7,0.72,390000,4-1/2
E8,0.3,2.9,3.1,0.81,410000,studio
```


### Task

1. **Train a Model**: Use the data from `known.csv` to train a machine learning model to predict the `market_trend`.
2. **Predict Market Trends**: Use the trained model to predict the `market_trend` values for the properties in `unknown.csv`.
3. **Integrate Predictions**: Integrate the predicted `market_trend` values back into the properties in Collection 5.
4. **Determine Best Investment**: Use the `best_investment_property` function to find the best property to invest in for Collection 5, now that the `market_trend` values are known.

### Hint

If you are not familiar with predictive algorithms, the simplest approach would be to use **Linear Regression**. You can find more information about Linear Regression on its [Wikipedia page](https://en.wikipedia.org/wiki/Linear_regression).


## Instructions

1. Implement the `best_investment_property` function to find the best property for each collection.
2. Ensure that you handle dependencies correctly.
3. Ensure that all attribute properties are respected.
4. Predict the `market_trend` values for Collection 5 using the provided `known.csv` and `unknown.csv` files.
5. Fill in the `Best Property ID` for each collection in the submission form.
6. Submit only the filled-in submission form.


### Submission form

```text
Collection 1 Best Property ID: AX
Collection 2 Best Property ID: BX
Collection 3 Best Property ID: CX
Collection 4 Best Property ID: DX
Collection 5 Best Property ID: EX
```

Good luck!
