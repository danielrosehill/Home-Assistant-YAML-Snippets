import os
import yaml
import re

def convert_to_title(folder_name):
    # Convert folder name like 'active-lite' to 'ActiveLite'
    words = folder_name.replace('-', ' ').split()
    return ''.join(word.capitalize() for word in words)

def process_folder(folder_path):
    # Skip if demo.md already exists
    if os.path.exists(os.path.join(folder_path, 'demo.md')):
        return

    # Get all files in the current folder
    files = os.listdir(folder_path)
    
    # Find yaml file and image file
    yaml_file = None
    image_file = None
    
    for file in files:
        lower_file = file.lower()
        if lower_file.endswith(('.yaml', '.yml')):
            yaml_file = file
        elif lower_file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_file = file

    # Skip if we don't have both files
    if not yaml_file or not image_file:
        return

    # Get folder name for title
    folder_name = os.path.basename(folder_path)
    title = convert_to_title(folder_name)

    # Read yaml content
    with open(os.path.join(folder_path, yaml_file), 'r') as f:
        yaml_content = f.read()

    # Create demo.md content
    demo_content = f"""# {title}

![{title}]({image_file})

```yaml
{yaml_content}
```
"""

    # Write demo.md
    with open(os.path.join(folder_path, 'demo.md'), 'w') as f:
        f.write(demo_content)

def main():
    # Start from current directory
    root_dir = '.'
    
    # Walk through all directories
    for root, dirs, files in os.walk(root_dir):
        process_folder(root)

if __name__ == "__main__":
    main()