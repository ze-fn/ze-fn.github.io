import os
import csv
from PIL import Image

def is_red(pixel):
    """
    Check if a pixel is red. 
    Handles RGBA (transparent) and standard RGB.
    """
    if len(pixel) == 4:
        r, g, b, a = pixel
        if a == 0: return False # Completely transparent pixels are ignored
    else:
        r, g, b = pixel

    # A basic threshold for red: High R, low G and B.
    return r > 150 and g < 100 and b < 100

def is_white(pixel):
    """Check if a pixel is white (background)."""
    r, g, b = pixel[:3]
    return r > 240 and g > 240 and b > 240

def process_image(image_path):
    """Scans the image row-by-row to integrate the area of red rectangles."""
    try:
        # Convert to RGBA to ensure we handle transparency properly
        img = Image.open(image_path).convert('RGBA')
    except Exception as e:
        print(f"Error opening {image_path}: {e}")
        return None, None, None

    pixels = img.load()
    width, height = img.size
    
    # Calculate the custom image area based on the requested formula
    img_area = (width - 20) * (height - 20)
    
    red_area_sq2 = 0
    red_rows_set = set() # Using a set to keep track of unique rows containing red
    
    # Row-wise pixel check
    for y in range(height):
        start_x = None
        
        for x in range(width):
            current_pixel = pixels[x, y]
            
            if is_red(current_pixel):
                if start_x is None:
                    # 1. Record coordinate of the FIRST identified red pixel
                    start_x = x 
                    red_rows_set.add(y)
                    
            elif is_white(current_pixel) and start_x is not None:
                # 2. Pixel to the right is white, record the LAST known red pixel
                end_x = x - 1
                
                # 3. Calculate area for this segment (Integral sum)
                red_area_sq2 += (end_x - start_x + 1)
                
                # Reset for potential other rectangles in the same row
                start_x = None 
                
        # Edge case: If the red rectangle touches the right edge of the image
        if start_x is not None:
            end_x = width - 1
            red_area_sq2 += (end_x - start_x + 1)
            
    n_row_red = len(red_rows_set)
    return n_row_red, red_area_sq2, img_area

def bulk_process(input_folder, output_csv):
    """Processes all images in a folder and saves results to a CSV."""
    
    # Supported image extensions
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')
    
    # Prepare CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write headers including the new img_area column
        writer.writerow(['filename', 'n_row_red', 'red_area_sq2', 'img_area'])
        
        # Iterate through files in the directory
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(valid_extensions):
                filepath = os.path.join(input_folder, filename)
                print(f"Processing: {filename}...")
                
                n_row_red, red_area_sq2, img_area = process_image(filepath)
                
                if n_row_red is not None:
                    # Write the new img_area value to the CSV
                    writer.writerow([filename, n_row_red, red_area_sq2, img_area])
                    print(f"  -> Rows: {n_row_red}, Red Area: {red_area_sq2}px, Img Area: {img_area}px")

    print(f"\nProcessing complete! Results saved to {output_csv}")

if __name__ == "__main__":
    # --- CONFIGURATION ---
    # Replace these paths with your actual folder path and desired output file
    INPUT_DIRECTORY = "./images" 
    OUTPUT_CSV_FILE = "red_rectangle_areas.csv"
    
    # Create the folder if it doesn't exist to prevent errors on first run
    if not os.path.exists(INPUT_DIRECTORY):
        print(f"Please create a folder named '{INPUT_DIRECTORY}' and put your images inside.")
    else:
        bulk_process(INPUT_DIRECTORY, OUTPUT_CSV_FILE)