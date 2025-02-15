from pykml import parser
from shapely.geometry import Polygon, mapping
import sys
import os
import csv
from itertools import combinations
from pathlib import Path

def read_kml_polygon(kml_file):
    """
    Read a KML file and extract the first polygon found
    Returns a Shapely polygon object
    """
    try:
        with open(kml_file, 'rt', encoding='utf-8') as f:
            # Parse KML with pykml
            doc = parser.parse(f)
            root = doc.getroot()
            
            # Find the first Polygon coordinates
            coords_elem = root.find(".//{http://www.opengis.net/kml/2.2}coordinates")
            if coords_elem is None:
                raise ValueError("No coordinates found in KML")
                
            # Parse coordinates string into list of tuples
            coords_text = coords_elem.text.strip()
            coords = []
            for coord in coords_text.split():
                x, y, z = coord.split(',')
                coords.append((float(x), float(y)))  # Ignore z coordinate
                
            return Polygon(coords)
        
    except Exception as e:
        print(f"Error reading KML file {kml_file}: {str(e)}")
        return None

def check_polygon_overlap(kml_file1, kml_file2):
    """
    Check if two KML polygons overlap and return the overlapping extent
    Returns (bool, float) tuple: (overlap status, overlap area)
    """
    # Read both KML files
    polygon1 = read_kml_polygon(kml_file1)
    polygon2 = read_kml_polygon(kml_file2)
    
    if polygon1 is None or polygon2 is None:
        return False, 0.0
    
    try:
        # Check for intersection
        if polygon1.intersects(polygon2):
            intersection = polygon1.intersection(polygon2)
            return True, intersection.area
        return False, 0.0
    except Exception as e:
        print(f"Error checking overlap between {kml_file1} and {kml_file2}: {str(e)}")
        return False, 0.0

def process_kml_folder(kml_folder, output_file):
    """
    Process all KML files in the given folder and write overlap results to CSV
    """
    # Get all KML files in the folder
    kml_files = list(Path(kml_folder).glob('*.kml'))
    total_files = len(kml_files)
    
    if not kml_files:
        print(f"No KML files found in {kml_folder}")
        return
    
    print(f"Processing {total_files} KML files...")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write results to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['KML File 1', 'KML File 2', 'Overlapping Extent'])
        
        # Calculate total number of comparisons
        total_comparisons = len(list(combinations(kml_files, 2)))
        processed = 0
        overlaps_found = 0
        
        # Check each pair of KML files
        for file1, file2 in combinations(kml_files, 2):
            processed += 1
            if processed % 10 == 0:
                print(f"Progress: {processed}/{total_comparisons} pairs checked ({(processed/total_comparisons)*100:.1f}%)")
            
            overlaps, area = check_polygon_overlap(file1, file2)
            if overlaps:
                writer.writerow([file1.name, file2.name, area])
                overlaps_found += 1
                print(f"Found overlap between {file1.name} and {file2.name} (Area: {area:.2f})")
    
    print(f"\nProcessing complete:")
    print(f"Total files processed: {total_files}")
    print(f"Total comparisons made: {total_comparisons}")
    print(f"Overlaps found: {overlaps_found}")

def main():
    kml_folder = "data/kmls"
    output_file = "data/output/kml_overlaps.csv"
    
    if not os.path.exists(kml_folder):
        print(f"Error: KML folder not found: {kml_folder}")
        sys.exit(1)
    
    process_kml_folder(kml_folder, output_file)
    print(f"\nResults written to {output_file}")
    
if __name__ == "__main__":
    main()