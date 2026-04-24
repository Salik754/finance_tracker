import sys

def count_reel_occurrences():
    print("Paste your text below. Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) when done:\n")
    
    # Read unlimited input
    text = sys.stdin.read()
    
    # Convert to lowercase for case-insensitive counting
    text_lower = text.lower()
    
    # Split into words
    words = text_lower.split()
    
    # Count exact matches of "reel"
    count = words.count("url")
    
    print(f'\nYou have liked {count} reels.')

if __name__ == "__main__":
    count_reel_occurrences()