import numpy as np

def calculate(list_of_nine):
    # Enforce exactly 9 digits
    if len(list_of_nine) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Reshape the flat list into a 3x3 matrix
    matrix = np.array(list_of_nine).reshape(3, 3)
    
    # Calculate statistics and explicitly cast back to standard Python lists via .tolist()
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().item()
        ]
    }
    
    return calculations