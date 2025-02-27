import os
import time

# Simulate scanning files (harmless)
def scan_files(directory):
    print(f"[SIMULATION] Scanning files in: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"[SIMULATION] Accessed: {file_path}")
            time.sleep(0.1)  # Simulate processing time

# Create a fake ransom note (harmless)
def create_ransom_note(directory):
    ransom_note_path = os.path.join(directory, "README_TEST.txt")
    with open(ransom_note_path, "w") as f:
        f.write("SIMULATION: This is a fake ransom note for educational testing.\n")
        f.write("Your files have NOT been encrypted. This is just a test.\n")
    print(f"[SIMULATION] Created fake ransom note: {ransom_note_path}")

# Main function
def simulate_ransomware(directory):
    print("[SIMULATION] Starting ransomware simulation...")
    scan_files(directory)
    create_ransom_note(directory)
    print("[SIMULATION] Simulation complete. No files were harmed.")

# Test in a safe directory (e.g., a dummy folder with test files)
test_directory = "C:\\Users\\ACER\\Documents\\ransomware"  # Replace with a non-critical path
if os.path.exists(test_directory):
    simulate_ransomware(test_directory)
else:
    print(f"Error: Directory '{test_directory}' does not exist. Please create it and add dummy files.")