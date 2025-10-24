"""
Program Name : paper_sizes_A0_to_A8.py
Author       : Soumodip Ghosh
Description  : 
    This program calculates and prints the dimensions (in millimeters)
    of paper sizes A0 through A8 according to the ISO 216 standard.
    
    A0 has dimensions 1189 mm × 841 mm.
    Each subsequent size A(n) is obtained by cutting A(n-1)
    in half parallel to its shorter side.

    Formula:
        width(n) = height(n-1)
        height(n) = width(n-1) / 2

Usage:
    Run this file directly using Python:
        python paper_sizes_A0_to_A8.py

Output:
    Prints a neatly formatted table showing A0–A8 paper sizes.
"""

def generate_paper_sizes():
    """
    Function to calculate and return paper sizes A0 to A8.

    Returns:
        list of tuples: Each tuple contains (size_name, width, height)
                        Example -> [("A0", 1189, 841), ("A1", 841, 594), ...]
    """
    
    # Initial dimensions of A0 (in mm)
    width = 1189
    height = 841
    
    sizes = [("A0", width, height)]  # Store results as tuples

    # Generate subsequent sizes A1 through A8
    for i in range(1, 9):
        # Swap width and height according to ISO rule
        width, height = height, width // 2
        sizes.append((f"A{i}", width, height))
    
    return sizes


def display_paper_sizes(sizes):
    """
    Function to display the paper sizes in a formatted way.

    Args:
        sizes (list): List of tuples containing size name and dimensions.
    """
    print("ISO 216 PAPER SIZES (A0 - A8)")
    print("=" * 35)
    print(f"{'Size':<5} {'Width (mm)':<12} {'Height (mm)':<12}")
    print("-" * 35)
    
    for name, w, h in sizes:
        print(f"{name:<5} {w:<12} {h:<12}")


def main():
    """Main driver function."""
    sizes = generate_paper_sizes()
    display_paper_sizes(sizes)


# Entry point of the program
if __name__ == "__main__":
    main()
