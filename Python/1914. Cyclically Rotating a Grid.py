#-- 1914. Cyclically Rotating a Grid --
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Rotates each layer of the grid counter-clockwise by k positions.
      
        Args:
            grid: 2D matrix to rotate
            k: Number of positions to rotate each layer
      
        Returns:
            The rotated grid
        """
        def rotate_layer(layer_index: int, rotation_count: int) -> None:
            """
            Rotates a specific layer of the grid counter-clockwise.
          
            Args:
                layer_index: Index of the layer (0 for outermost)
                rotation_count: Number of positions to rotate
            """
            # Extract all elements from the current layer in counter-clockwise order
            layer_elements = []
          
            # Top row (left to right, excluding last element)
            for col in range(layer_index, num_cols - layer_index - 1):
                layer_elements.append(grid[layer_index][col])
          
            # Right column (top to bottom, excluding last element)
            for row in range(layer_index, num_rows - layer_index - 1):
                layer_elements.append(grid[row][num_cols - layer_index - 1])
          
            # Bottom row (right to left, excluding last element)
            for col in range(num_cols - layer_index - 1, layer_index, -1):
                layer_elements.append(grid[num_rows - layer_index - 1][col])
          
            # Left column (bottom to top, excluding last element)
            for row in range(num_rows - layer_index - 1, layer_index, -1):
                layer_elements.append(grid[row][layer_index])
          
            # Calculate effective rotation (avoid unnecessary full rotations)
            effective_rotation = rotation_count % len(layer_elements)
            if effective_rotation == 0:
                return
          
            # Rotate the elements
            layer_elements = layer_elements[effective_rotation:] + layer_elements[:effective_rotation]
          
            # Place rotated elements back into the grid
            element_index = 0
          
            # Top row (left to right, excluding last element)
            for col in range(layer_index, num_cols - layer_index - 1):
                grid[layer_index][col] = layer_elements[element_index]
                element_index += 1
          
            # Right column (top to bottom, excluding last element)
            for row in range(layer_index, num_rows - layer_index - 1):
                grid[row][num_cols - layer_index - 1] = layer_elements[element_index]
                element_index += 1
          
            # Bottom row (right to left, excluding last element)
            for col in range(num_cols - layer_index - 1, layer_index, -1):
                grid[num_rows - layer_index - 1][col] = layer_elements[element_index]
                element_index += 1
          
            # Left column (bottom to top, excluding last element)
            for row in range(num_rows - layer_index - 1, layer_index, -1):
                grid[row][layer_index] = layer_elements[element_index]
                element_index += 1
      
        # Get grid dimensions
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Calculate number of layers (each layer is a rectangular ring)
        num_layers = min(num_rows, num_cols) // 2
      
        # Rotate each layer
        for layer in range(num_layers):
            rotate_layer(layer, k)
      
        return grid
