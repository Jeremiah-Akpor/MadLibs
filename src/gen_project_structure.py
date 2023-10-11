""" Generates the tree structure for the specified directory."""
import os


def generate_project_tree(root_dir, indent=0):
    """Generates the tree structure for the specified directory.

    Args:
        root_dir (_type_): _description_
        indent (int, optional): _description_. Defaults to 0.
    """
    # Get the list of files and subdirectories in the current directory
    items = os.listdir(root_dir)

    # Sort the items to display directories first, followed by files
    items.sort(key=lambda x: os.path.isfile(os.path.join(root_dir, x)))

    for item in items:
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            # Print file with appropriate indentation
            print("  " * indent + "- " + item)
        elif os.path.isdir(item_path):
            # Print directory with appropriate indentation
            print("  " * indent + "+ " + item)
            # Recursively generate the tree structure for subdirectories
            generate_project_tree(item_path, indent + 1)


if __name__ == "__main__":
    # Specify the root directory of your project
    root_directory = os.getcwd() + "/src"
    print("Root Directory:", root_directory)

    if os.path.exists(root_directory):
        print("Project Tree Structure:")
        generate_project_tree(root_directory)
    else:
        print("The specified root directory does not exist.")
