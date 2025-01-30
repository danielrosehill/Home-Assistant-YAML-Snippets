import os
import yaml
import re

def convert_to_title(folder_name):
    # Convert folder name like 'hebrew-date-and-time' to 'Hebrew Date And Time'
    words = folder_name.replace('-', ' ').split()
    return ' '.join(word.capitalize() for word in words)

def get_folder_content(folder_path):
    # Get all files in the folder
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
        return None

    # Get folder name for title
    folder_name = os.path.basename(folder_path)
    title = convert_to_title(folder_name)

    # Read yaml content
    with open(os.path.join(folder_path, yaml_file), 'r') as f:
        yaml_content = f.read()

    # Create content block with extra spacing
    content = f"""

## {title}

![{title}]({folder_name}/{image_file})

```yaml
{yaml_content}
```
"""
    return content

def main():
    # Read existing README.md
    with open('README.md', 'r') as f:
        readme_content = f.read()

    # Find the content between placeholders
    start_placeholder = "<!-- START_THEMES -->"
    end_placeholder = "<!-- END_THEMES -->"
    
    if start_placeholder not in readme_content or end_placeholder not in readme_content:
        print("Error: Placeholders not found in README.md")
        return

    # Get all theme folders
    theme_contents = []
    for item in sorted(os.listdir('.')):  # sorted for alphabetical order
        if os.path.isdir(item) and not item.startswith('.'):  # ignore hidden directories
            content = get_folder_content(os.path.join('.', item))  # Use full path
            if content:
                theme_contents.append(content)

    # Combine all theme contents
    all_themes_content = "\n".join(theme_contents)

    # Replace content between placeholders
    pattern = f"{start_placeholder}.*?{end_placeholder}"
    new_content = f"{start_placeholder}\n{all_themes_content}\n{end_placeholder}"
    new_readme = re.sub(pattern, new_content, readme_content, flags=re.DOTALL)

    # Write updated README.md
    with open('README.md', 'w') as f:
        f.write(new_readme)

if __name__ == "__main__":
    main()