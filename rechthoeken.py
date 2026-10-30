def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> TODO:
    """
    >>> is_same_rectangle(4, 6, 0, 4)
    True 
    >>> is_same_rectangle(0, 0, 6, 9)
    False 
    >>> is_same_rectangle(7, 1, 7, 1)
    True
    """

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> TODO:
    """
    Controleert of beide rechthoeken hetzelfde vierkant zijn
    >>> is_same_square(4, 4, 4, 4)
    True
    >>> is_same_square(2, 2, 3, 4)
    False
    >>> is_same_square(5, 5, 5, 5)
    True
    """

def calculate_length(c1: int, c2: int) -> int:
    """
    Berekent de lengte van een zijde op basis van twee coördinaten
    >>> calculate_length(0, 7) 
    7
    >>> calculate_length(2, 9)
    7
    >>> calculate_length(1, 13)
    12
    """

if __name__ == '__main__':
    ax1 = int(input("Geef de x1 van A:"))
    ax2 = int(input("geef de x2 van A"))
    ay1 = int(input("Geef de y1 van A"))
    ay2 = int(input("Geef de y2 van A")) 
    
    bx1 = int(input("Geef de x1 van B:"))
    bx2 = int(input("geef de x2 van B:"))
    by1 = int(input("Geef de y1 van B"))
    by2 = int(input("Geef de y2 van A")) 
    