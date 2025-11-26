import os
import shutil

def organizer_files():
    print("="*50)
    print("FILE ORGANIZER")
    print("="*50)
    
    # Kategori file
    categories = {
        "Images": ["jpg", "jpeg", "png", "gif", "bmp"],
        "Documents": ["pdf", "doc", "docx", "txt"],
        "Videos": ["mp4", "avi", "mkv"],
        "Music": ["mp3", "wav"],
        "Archives": ["zip", "rar", "7z"]
    }
    
    moved = 0
    skipped = 0
    
    items = os.listdir(".")
    
    for item in items:
        if not os.path.isfile(item):
            continue
        
        if item == "organizer.py":
            continue
        
        if "." not in item:
            continue
        
    
    
        ext = item.split(".")[-1].lower()
                
        found_category = None
        for category, extension in categories.items():
            if ext in extension:
                found_category = category
                break
            
        if found_category is None:
            found_category = "Others"
            
        if not os.path.exists(found_category):
            os.mkdir(found_category)
            
        try:
            destination = os.path.join(found_category, item)
            shutil.move(item, destination)
            print(f"Moved {item} -> {found_category}")
            moved += 1
        except Exception as e:
            print(f"Error Moving {item} : {e}")
            skipped += 1
    print("\n" + "="*50)
    print(f"Done! Moved {moved} files, skipped {skipped}")
    print("="*50)

print("This will organize all files in current folder.")
answer = input("Continue? (y/n): ")

if answer.lower() == "y":
    organizer_files()
else:
    print("cancelled")