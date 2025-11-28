import os
from pathlib import Path
import json

class FileAnalyzer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.stats = {}
        
    def get_file_size_readable(self, size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    
    def analyze(self):
        files = list(self.folder_path.rglob('*'))
        
        total_size = 0
        file_types = {}
        largest_files = []
        skipped = 0
        
        for file in files:
            if file.is_file():
                try:
                    size = file.stat().st_size
                except (PermissionError, FileNotFoundError):
                    
                    skipped += 1
                    continue
                
                extension = file.suffix or "No extension"
                total_size += size
                file_types[extension] = file_types.get(extension, 0) + 1
                
                largest_files.append({
                    'name': file.name,
                    'size': size,
                    'path': str(file)
                })
        
        largest_files.sort(key=lambda x: x['size'], reverse=True)
        
        self.stats = {
            'total_files': len([f for f in files if f.is_file()]) - skipped,
            'total_folders': len([f for f in files if f.is_dir()]),
            'file_types': file_types,
            'total_size': total_size,
            'largest_files': largest_files[:10],
            'skipped_files': skipped
        }
                
        return self.stats
    
    def show_report(self):
        if not self.stats:
            self.analyze()
        
        folder_display = str(self.folder_path.resolve())
        print("\n" + "="*60)
        print(f"FILE ANALYSIS REPORT: {folder_display}")
        print("="*60)
        
        print("\nOverview")
        print(f"   Total files    : {self.stats['total_files']}")
        print(f"   Total folders  : {self.stats['total_folders']}")
        print(f"   Total size     : {self.get_file_size_readable(self.stats['total_size'])}")
        if self.stats.get('skipped_files'):
            print(f"   Skipped files  : {self.stats['skipped_files']} (permission/missing)")
        
        print(f"\nFile Types:")
        for ext, count in sorted(self.stats['file_types'].items(), key=lambda x: x[1], reverse=True):
            print(f"   {ext}: {count} files")
            
        print(f"\nLargest Files:")
        for i, file in enumerate(self.stats['largest_files'], 1):
            print(f"   {i}. {file['name']}: {self.get_file_size_readable(file['size'])}  —  {file['path']}")
        print("\n" + "="*60)
        
    def export_report(self, output_file="report.json"):
        if not self.stats:
            self.analyze()
        
        
        export_data = self.stats.copy()
        export_data['total_size_readable'] = self.get_file_size_readable(self.stats['total_size'])
        
        
        export_data['largest_files'] = [
            { **f, 'size_readable': self.get_file_size_readable(f['size']) }
            for f in self.stats['largest_files']
        ]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
            
        print(f"Report exported to {output_file}")
        
if __name__ == "__main__":
    folder = input("Enter folder path to analyze: ").strip() or "."
    
    analyzer = FileAnalyzer(folder)
    analyzer.show_report()
    
    export = input("\nExport report to JSON? (y/n): ").strip().lower()
    if export == "y":
        filename = input("Filename (default: report.json): ").strip() or "report.json"
        analyzer.export_report(filename)
