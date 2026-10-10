import time
import multiprocessing
import os

def complex_calculation(number):
    """
    Simulates a CPU-bound task, like a complex calculation on an Excel cell/row.
    This function represents a unit of work that would typically be done sequentially.
    """
    # A simple, somewhat CPU-intensive operation to simulate data processing
    result = 0
    for _ in range(1_000_000): # Simulate heavy computation for each item
        result += number * number / (number + 1) if number != -1 else 0
    return f"Processed {number} -> {result:.2f}"

def sequential_processing(data):
    """
    Processes data sequentially, similar to how traditional VBA macros operate.
    This method uses a single thread/core.
    """
    print("\n--- Sequential Processing (Traditional Method) ---")
    start_time = time.time()
    results = [complex_calculation(item) for item in data]
    end_time = time.time()
    print(f"Sequential processing took: {end_time - start_time:.4f} seconds")
    return results

def parallel_processing(data):
    """
    Processes data in parallel using multiprocessing, leveraging 'dual-core' Python.
    This approach distributes tasks across available CPU cores, enabling faster execution
    for CPU-bound operations, a key aspect of modern AI agent interaction.
    """
    print("\n--- Parallel Processing (Dual-Core Python Approach) ---")
    start_time = time.time()
    # Use a Pool to distribute tasks across available CPU cores
    # os.cpu_count() determines the number of processes to match your CPU cores
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        results = pool.map(complex_calculation, data) # Apply complex_calculation to all items in data in parallel
    end_time = time.time()
    print(f"Parallel processing took: {end_time - start_time:.4f} seconds")
    return results

if __name__ == "__main__":
    # Simulate a dataset, like a list of rows from an Excel sheet
    sample_data = list(range(1, 101)) # 100 items for processing

    print(f"Simulating processing of {len(sample_data)} items (e.g., Excel rows).")
    print(f"Number of CPU cores detected: {os.cpu_count()}")

    # Demonstrate traditional sequential processing (like VBA macros)
    sequential_processing(sample_data)

    # Demonstrate 'Dual-Core Python' parallel processing for efficiency
    parallel_processing(sample_data)

    print("\nThis example highlights how 'Dual-Core Python' (using multiprocessing) can")
    print("significantly speed up CPU-bound data processing tasks compared to traditional")
    print("sequential methods, providing a more efficient foundation for AI agent interactions.")
