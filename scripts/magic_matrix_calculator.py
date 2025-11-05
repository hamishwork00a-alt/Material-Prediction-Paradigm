"""
Magic Matrix Calculator (Core Algorithm)
Calculates the Magic Square Imbalance (ΔS') for a 3D atomic structure.
"""

import numpy as np

def calculate_delta_S(atomic_density_matrix):
    """
    Calculate the Magic Square Imbalance (ΔS') for a 3D matrix.

    Args:
        atomic_density_matrix (numpy.ndarray): A 3D array representing the 
                                               atomic density or potential field.

    Returns:
        float: The ΔS' value, quantifying the degree of symmetry breaking.
    """
    n = len(atomic_density_matrix)
    
    # Calculate the perfect sum for an ideal magic square of size n
    # For a 3D magic cube, the magic constant is M = n*(n^3 + 1)/2
    # We use a normalized version for comparison
    total_sum = np.sum(atomic_density_matrix)
    magic_constant_perfect = total_sum / n  # Ideal average per line
    
    total_deviation = 0.0
    count = 0

    # Check all rows, columns, and pillars
    for i in range(n):
        for j in range(n):
            # Sum along the k-axis (rows in 3D)
            row_sum_k = np.sum(atomic_density_matrix[i, j, :])
            total_deviation += abs(row_sum_k - magic_constant_perfect)
            count += 1

            # Sum along the i-axis (columns in 3D)  
            col_sum_i = np.sum(atomic_density_matrix[:, j, i])
            total_deviation += abs(col_sum_i - magic_constant_perfect)
            count += 1

    # Check main diagonals (simplified for 3D)
    diag1_sum = np.sum([atomic_density_matrix[k, k, k] for k in range(n)])
    diag2_sum = np.sum([atomic_density_matrix[k, k, n-1-k] for k in range(n)])
    
    total_deviation += abs(diag1_sum - magic_constant_perfect)
    total_deviation += abs(diag2_sum - magic_constant_perfect)
    count += 2

    # Normalize the total deviation
    delta_S = total_deviation / (count * magic_constant_perfect)
    
    return round(delta_S, 5)

def structure_to_density_matrix(atoms, grid_size=5):
    """
    Convert atomic structure to a simplified density matrix.
    
    Note: In production, this would use DFT electron density or atomic potentials.
    This is a placeholder implementation for demonstration.
    """
    # Placeholder: create a mock density matrix
    # In real implementation, this would project atomic potentials onto a grid
    matrix = np.ones((grid_size, grid_size, grid_size))
    
    # Add some random noise to simulate symmetry breaking
    # In real usage, this would come from actual atomic positions
    np.random.seed(42)  # For reproducibility
    noise = np.random.normal(0, 0.1, (grid_size, grid_size, grid_size))
    
    return matrix + noise

# Example usage
if __name__ == "__main__":
    # Create a test matrix (perfect crystal would be all 1s)
    test_matrix = np.ones((5, 5, 5))
    
    print("Testing Magic Matrix Calculator:")
    print("Perfect crystal ΔS':", calculate_delta_S(test_matrix))
    
    # Test with slight imperfection
    test_matrix[2, 2, 2] = 0.5  # Introduce a "vacancy"
    print("Crystal with defect ΔS':", calculate_delta_S(test_matrix))
