"""CLI input/output handling for the Todo application."""

# Constants for validation
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 1000


def validate_title(title: str) -> tuple[bool, str]:
    """Validate a task title.

    Args:
        title: The title to validate.

    Returns:
        A tuple of (is_valid, error_message). If valid, error_message is empty.
    """
    stripped = title.strip()
    if not stripped:
        return False, "Error: Title cannot be empty."
    if len(stripped) > MAX_TITLE_LENGTH:
        return False, f"Error: Title must be {MAX_TITLE_LENGTH} characters or less."
    return True, ""


def validate_description(description: str) -> tuple[bool, str]:
    """Validate a task description.

    Args:
        description: The description to validate.

    Returns:
        A tuple of (is_valid, error_message). If valid, error_message is empty.
    """
    if len(description) > MAX_DESCRIPTION_LENGTH:
        return False, f"Error: Description must be {MAX_DESCRIPTION_LENGTH} characters or less."
    return True, ""


def validate_id(id_str: str) -> tuple[bool, int, str]:
    """Validate and parse a task ID string.

    Args:
        id_str: The ID string to validate.

    Returns:
        A tuple of (is_valid, parsed_id, error_message).
        If valid, parsed_id contains the integer ID and error_message is empty.
        If invalid, parsed_id is 0.
    """
    stripped = id_str.strip()
    if not stripped:
        return False, 0, "Error: Please enter a valid task ID (positive number)."
    try:
        task_id = int(stripped)
        if task_id <= 0:
            return False, 0, "Error: Please enter a valid task ID (positive number)."
        return True, task_id, ""
    except ValueError:
        return False, 0, "Error: Please enter a valid task ID (positive number)."


def print_error(message: str) -> None:
    """Print an error message to the console.

    Args:
        message: The error message to display.
    """
    print(message)


def print_success(message: str) -> None:
    """Print a success message to the console.

    Args:
        message: The success message to display.
    """
    print(message)


def format_task_created(task_id: int) -> str:
    """Format the success message for task creation.

    Args:
        task_id: The ID of the newly created task.

    Returns:
        Formatted success message string.
    """
    return f"Task created successfully with ID: {task_id}"


def handle_add_task() -> None:
    """Handle the Add Task menu option.

    Prompts user for title and description, validates input,
    and creates the task in storage.
    """
    import storage

    # Get title
    title = input("Enter task title: ")
    is_valid, error_msg = validate_title(title)
    if not is_valid:
        print_error(error_msg)
        return

    # Get description (optional)
    description = input("Enter task description (press Enter to skip): ")
    if description:
        is_valid, error_msg = validate_description(description)
        if not is_valid:
            print_error(error_msg)
            return
    else:
        description = None

    # Create the task
    task = storage.add_task(title.strip(), description)
    print_success(format_task_created(task.id))


def format_task_list(tasks: list) -> str:
    """Format the task list for display.

    Args:
        tasks: List of Task objects to format.

    Returns:
        Formatted string representation of all tasks.
    """
    lines = []
    lines.append("=" * 40)
    lines.append("              YOUR TASKS")
    lines.append("=" * 40)

    if not tasks:
        lines.append("No tasks yet. Add your first task!")
    else:
        for task in tasks:
            status = "✓" if task.completed else "✗"
            lines.append(f"[{task.id}] {status} {task.title}")
            if task.description:
                lines.append(f"    Description: {task.description}")
            else:
                lines.append("    (No description)")
            lines.append("")

        # Summary
        completed = sum(1 for t in tasks if t.completed)
        pending = len(tasks) - completed
        lines.append("=" * 40)
        lines.append(f"Total: {len(tasks)} tasks ({completed} completed, {pending} pending)")

    lines.append("=" * 40)
    return "\n".join(lines)


def handle_list_tasks() -> None:
    """Handle the List Tasks menu option.

    Retrieves all tasks from storage and displays them.
    """
    import storage

    tasks = storage.list_tasks()
    print(format_task_list(tasks))


def display_menu() -> None:
    """Display the main menu with numbered options."""
    print()
    print("=" * 40)
    print("         TODO APPLICATION")
    print("=" * 40)
    print()
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Complete")
    print("6. Exit")
    print()


def get_menu_choice() -> int:
    """Get and validate the user's menu choice.

    Returns:
        The validated menu choice (1-6), or 0 if invalid.
    """
    choice = input("Enter your choice (1-6): ")
    stripped = choice.strip()

    if not stripped:
        print_error("Error: Invalid choice. Please enter a number between 1 and 6.")
        return 0

    try:
        num = int(stripped)
        if 1 <= num <= 6:
            return num
        else:
            print_error("Error: Invalid choice. Please enter a number between 1 and 6.")
            return 0
    except ValueError:
        print_error("Error: Invalid choice. Please enter a number between 1 and 6.")
        return 0


def format_toggle_result(task_id: int, completed: bool) -> str:
    """Format the success message for toggling task completion.

    Args:
        task_id: The ID of the toggled task.
        completed: The new completion status.

    Returns:
        Formatted success message string.
    """
    status = "complete" if completed else "pending"
    return f"Task {task_id} marked as {status}."


def handle_toggle_complete() -> None:
    """Handle the Toggle Complete menu option.

    Prompts user for task ID, validates input, and toggles the task status.
    """
    import storage

    id_str = input("Enter task ID to toggle: ")
    is_valid, task_id, error_msg = validate_id(id_str)
    if not is_valid:
        print_error(error_msg)
        return

    task = storage.toggle_complete(task_id)
    if task is None:
        print_error(f"Error: Task with ID {task_id} not found.")
    else:
        print_success(format_toggle_result(task_id, task.completed))


def format_update_result(task_id: int) -> str:
    """Format the success message for task update.

    Args:
        task_id: The ID of the updated task.

    Returns:
        Formatted success message string.
    """
    return f"Task {task_id} updated successfully."


def handle_update_task() -> None:
    """Handle the Update Task menu option.

    Prompts user for task ID and new values, validates input,
    and updates the task in storage.
    """
    import storage

    # Get task ID
    id_str = input("Enter task ID to update: ")
    is_valid, task_id, error_msg = validate_id(id_str)
    if not is_valid:
        print_error(error_msg)
        return

    # Check if task exists
    task = storage.get_task(task_id)
    if task is None:
        print_error(f"Error: Task with ID {task_id} not found.")
        return

    # Get new title (optional - press Enter to keep current)
    new_title = input("Enter new title (press Enter to keep current): ")
    if new_title:
        is_valid, error_msg = validate_title(new_title)
        if not is_valid:
            print_error(error_msg)
            return
        new_title = new_title.strip()
    else:
        new_title = None

    # Get new description (optional - press Enter to keep current)
    new_description = input("Enter new description (press Enter to keep current): ")
    if new_description:
        is_valid, error_msg = validate_description(new_description)
        if not is_valid:
            print_error(error_msg)
            return
    else:
        new_description = None

    # Update the task
    storage.update_task(task_id, new_title, new_description)
    print_success(format_update_result(task_id))


def format_delete_result(task_id: int) -> str:
    """Format the success message for task deletion.

    Args:
        task_id: The ID of the deleted task.

    Returns:
        Formatted success message string.
    """
    return f"Task {task_id} deleted successfully."


def handle_delete_task() -> None:
    """Handle the Delete Task menu option.

    Prompts user for task ID, validates input, and deletes the task.
    """
    import storage

    id_str = input("Enter task ID to delete: ")
    is_valid, task_id, error_msg = validate_id(id_str)
    if not is_valid:
        print_error(error_msg)
        return

    deleted = storage.delete_task(task_id)
    if deleted:
        print_success(format_delete_result(task_id))
    else:
        print_error(f"Error: Task with ID {task_id} not found.")
