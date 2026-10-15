import numpy as np


def simulate_morning(rng: np.random.Generator | None = None) -> tuple[int, float]:
    opening_minutes = 4 * 60
    mean_time_between_arrivals = 3.0
    service_time = 3.0

    if rng is None:
        rng = np.random.default_rng()
    arrival_times = []
    arrival_time = 0.0

    while True:
        arrival_time += rng.exponential(mean_time_between_arrivals)
        if arrival_time >= opening_minutes:
            break
        arrival_times.append(arrival_time)

    next_available_time = 0.0
    total_wait = 0.0

    for arrival_time in arrival_times:
        service_start = max(arrival_time, next_available_time)
        total_wait += service_start - arrival_time
        next_available_time = service_start + service_time

    served_customers = len(arrival_times)
    average_wait = total_wait / served_customers if served_customers else 0.0
    return served_customers, average_wait


if __name__ == "__main__":
    simulation_count = 1000
    rng = np.random.default_rng()
    results = [simulate_morning(rng) for _ in range(simulation_count)]
    customers_served = sum(customers for customers, _ in results)
    total_wait = sum(customers * wait for customers, wait in results)
    average_customers = customers_served / simulation_count
    average_wait = total_wait / customers_served if customers_served else 0.0
    print(f"Average customers per morning: {average_customers:.2f}")
    print(f"Average wait: {average_wait:.2f} minutes")
