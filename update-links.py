import os
import re

def update_frontmatter(directory, field, new_field, old_prefix, new_prefix):
    """
    Updates the specified field in the frontmatter of Markdown files within a directory.
    
    Args:
        directory (str): The target directory containing Markdown files.
        field (str): The frontmatter field to update (e.g., 'background_image', 'background').
        new_field (str): The new field name to replace the old field (use same as 'field' if no change).
        old_prefix (str): The prefix to be replaced in the field's value.
        new_prefix (str): The new prefix to insert into the field's value.
    """
    # Compile a regex pattern to match the specific field with the old prefix
    pattern = re.compile(rf'^({field}\s*:\s*){re.escape(old_prefix)}(.+)$', re.IGNORECASE)

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return

    files_processed = 0
    files_matched = 0
    files_updated = 0

    # Traverse through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):  # Targeting Markdown files
                files_processed += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    new_lines = []
                    file_updated = False
                    replacements_in_file = 0

                    for line in lines:
                        match = pattern.match(line)
                        if match:
                            files_matched += 1
                            replacements_in_file += 1
                            # Determine the field name to use
                            field_to_use = new_field if new_field else field
                            # Construct the new line with the updated prefix and field name
                            new_line = f"{field_to_use}: {new_prefix}{match.group(2)}\n"
                            new_lines.append(new_line)
                            file_updated = True
                        else:
                            new_lines.append(line)

                    if file_updated:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                        files_updated += 1
                        print(f'Updated: {file_path} (Replacements: {replacements_in_file})')
                    else:
                        print(f'No changes needed: {file_path}')
                except Exception as e:
                    print(f'Error processing {file_path}: {e}')

    print("\nProcessing Complete.")
    print(f"Total Markdown files processed in '{directory}': {files_processed}")
    print(f"Total files matched for update in '{directory}': {files_matched}")
    print(f"Total files updated in '{directory}': {files_updated}\n")

def main():
    # Define the update rules for each directory
    update_rules = [
        {
            'directory': '_insights',
            'field': 'background',
            'new_field': 'background_image',  # Field name change
            'old_prefix': 'posts/',
            'new_prefix': '/assets/images/posts/'
        }
    ]

    # Iterate over each rule and apply updates
    for rule in update_rules:
        update_frontmatter(
            directory=rule['directory'],
            field=rule['field'],
            new_field=rule['new_field'],
            old_prefix=rule['old_prefix'],
            new_prefix=rule['new_prefix']
        )

if __name__ == "__main__":
    main()