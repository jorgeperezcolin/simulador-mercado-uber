import numpy as np

def run_simulation(params):
    steps = params["steps"]
    drivers = params["drivers"]
    users = params["users"]
    base_price = params["base_price"]
    price_sensitivity = params["price_sensitivity"]

    results = []

    for step in range(steps):

        # Demanda efectiva (usuarios que solicitan viaje)
        demand = np.random.poisson(users * 0.8)

        # Oferta efectiva (conductores disponibles)
        supply = np.random.poisson(drivers * 0.9)

        trips = min(demand, supply)

        # Surge pricing básico
        imbalance = demand - supply
        price_multiplier = 1 + imbalance * price_sensitivity
        price_multiplier = max(0.5, price_multiplier)

        price = base_price * price_multiplier

        utilization = trips / drivers if drivers > 0 else 0

        results.append({
            "step": step,
            "demand": demand,
            "supply": supply,
            "trips": trips,
            "price": round(price, 2),
            "utilization": utilization
        })

    return results
