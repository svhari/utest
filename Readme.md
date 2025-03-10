## Readme.md
# create and activate a virtual environment:
$ 'python3 -m venv v1'
$ source v1/bin/activate
# Then install PyTest using pip:
$ pip3 install pytest


| Method	        | Description
| test_add_task	    | Tests if tasks are added correctly
test_add_empty_task	Ensures that an empty task raises an error
test_remove_task	Checks if a task can be successfully removed
test_remove_nonexistent_task	Tests if an error is raised when trying to remove a non-existent task
test_mark_completed	Tests if tasks can be marked as completed
test_get_tasks	Retrieves all tasks and filters completed and pending tasks


# To run the tests : ensure you are in venv312 environment
# if not do $ source ./venv312/bin/activate
# $ pytest