"""Module 6: Individual Git and GitHub Practice.

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Git Practice Lab"
    version = "1.2"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()

    # TODO 1 (done): Changed project_name and version in show_project_info().
    # TODO 2 (done): Why saving code changes with Git is useful.
    print("Git keeps a history of every saved change, so I can see what changed, "
          "when it changed, and go back to an earlier working version if something breaks.")
    # TODO 3 (done): One difference between git commit and git push.
    print("git commit saves a snapshot of my changes in my local repository, "
          "while git push uploads those commits to the remote repository on GitHub.")


if __name__ == "__main__":
    main()
