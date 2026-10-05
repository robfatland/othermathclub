def simulate_ms_halfway(threshold=1e-10, max_iterations=1000):
    """
    Simulate Ms. Halfway's journey.
    
    Args:
        threshold: Stop when movement is smaller than this value (microscopic progress)
        max_iterations: Maximum number of iterations to prevent infinite loops
    
    Returns:
        tuple: (final_position, iterations, positions_history)
    """
    # Initial conditions
    home = 0.0
    post_office = 1.0
    current_position = home
    destination = post_office
    
    positions = [current_position]
    destinations_history = []
    
    iteration = 0
    
    while iteration < max_iterations:
        # Calculate halfway point to destination
        previous_position = current_position
        current_position = (current_position + destination) / 2
        
        # Store for tracking
        positions.append(current_position)
        destinations_history.append(destination)
        
        # Check if movement is microscopic
        movement = abs(current_position - previous_position)
        if movement < threshold:
            break
        
        # Update destination: go back to where she just was
        destination = previous_position
        
        iteration += 1
    
    return current_position, iteration, positions, destinations_history


def main():
    """
    Main function to solve and display the Ms Halfway problem.
    """
    print("=" * 70)
    print("MS. HALFWAY PROBLEM SOLVER")
    print("=" * 70)
    print()
    print("Problem Statement:")
    print("-" * 70)
    print("Ms. Halfway starts at home (0 km) and wants to walk to the")
    print("post office (1 km away). Each time she walks, she only goes")
    print("halfway to her destination, then changes her mind and decides")
    print("to return to where she just was (but again only goes halfway).")
    print("This pattern continues indefinitely.")
    print()
    print("Question: Where does she eventually end up?")
    print("-" * 70)
    print()
    
    # Run simulation
    final_position, iterations, positions, destinations = simulate_ms_halfway()
    
    # Display results
    print("SIMULATION RESULTS:")
    print("=" * 70)
    print(f"Final Position: {final_position:.15f} km from home")
    print(f"Number of iterations: {iterations}")
    print(f"As a fraction: approximately 1/3 km from home")
    print(f"Exact fraction: {final_position} ≈ {1/3}")
    print()
    
    # Show first few iterations
    print("First 15 iterations:")
    print("-" * 70)
    print(f"{'Step':<6} {'Position (km)':<18} {'Destination (km)':<18} {'Movement'}")
    print("-" * 70)
    print(f"{'Start':<6} {0.0:<18.10f} {'Post Office (1)':<18}")
    
    for i in range(min(15, len(positions) - 1)):
        dest_label = f"{destinations[i]:.10f}"
        if i == 0:
            dest_label = f"{destinations[i]:.10f} (Post Office)"
        elif destinations[i] == 0.0:
            dest_label = f"{destinations[i]:.10f} (Home)"
        
        movement = abs(positions[i+1] - positions[i])
        print(f"{i+1:<6} {positions[i+1]:<18.10f} {dest_label:<18} {movement:.10f}")
    
    if iterations > 15:
        print(f"... ({iterations - 15} more iterations)")
    
    print()
    print("ANALYSIS:")
    print("-" * 70)
    print("The sequence converges to exactly 1/3 km from home.")
    print("This can be proven mathematically:")
    print()
    print("If we denote her position after n steps as p_n, then:")
    print("  p_1 = 1/2")
    print("  p_2 = (p_1 + 0)/2 = 1/4")
    print("  p_3 = (p_2 + p_1)/2 = (1/4 + 1/2)/2 = 3/8")
    print("  p_4 = (p_3 + p_2)/2 = (3/8 + 1/4)/2 = 5/16")
    print()
    print("The sequence oscillates around 1/3 and converges to it.")
    print("=" * 70)
    
    # Verify the answer
    print()
    print(f"Verification: {final_position:.15f} ≈ {1/3:.15f}")
    print(f"Difference from 1/3: {abs(final_position - 1/3):.2e} km")
    print()


if __name__ == "__main__":
    main()
