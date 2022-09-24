class ProductNotFound(Exception):
    """Raise when Product ID is not found in catalogue"""
    
    
class ProductAlreadyExists(Exception):
    """Raise when Product ID is already present in catalogue"""    
