"""Main entry point for the Todo application."""

import cli


def main() -> None:
    """Main function that runs the Todo application menu loop."""
    while True:
        cli.display_menu()
        choice = cli.get_menu_choice()

        match choice:
            case 1:
                cli.handle_add_task()
            case 2:
                cli.handle_list_tasks()
            case 3:
                cli.handle_update_task()
            case 4:
                cli.handle_delete_task()
            case 5:
                cli.handle_toggle_complete()
            case 6:
                print("Thank you for using Todo App. Goodbye!")
                break
            case _:
                # Invalid choice already handled by get_menu_choice
                pass


if __name__ == "__main__":
    main()
