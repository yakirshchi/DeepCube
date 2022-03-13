# Coding Assignment - Short description of my solution:
1. I've created a class for "Task" object with attributes: "status", "priority", "tasks" (list of dependant task objects), "name" (for recognizing the task) and isChecked (used for recognizing if there is a cycle task pointer). 
2. I've created a class for "TaskExecutor" with the following methods:
   * `executeMain` - Execution start from here, checks first for a cycle task pointer and if OK then continues with task execution.
      * `isCycleExist` - Runs over each task in the tree of tasks and makes sure each task was visited only once by changing the "isChecked" indicator to True on first visit.
	  * `executeAllTasks` - Execute the tasks in the order according to the "option" ('A'/'B') parameter input.
	     * `execute_a` - Sorts the list of tasks into 2 groups (lists), with/without dependencies, and then execute the tasks with no dependencies first.
		 * `execute_b` - Sorts the list of tasks by priority and execute them based on the priority.
			* `sortByPriority` -  Sorts the list of tasks while assuming that when the value is low then its priority is higher.
	     * `executeTaskAction` - The task execute action: prints the task name and changes the task status to 'done'

Notes: Kindly notice the testing example in the script, showing 4 tasks named ('a','b','c','d') each one with 3 dependant subtasks. you can manually change the option parameter ('A'/'B'), add additional sub-subtask, direct to existing subtasks (cycle) and run to see the results. 

Thank you for taking the time reviewing my assignment :)
Yakir Shchigelski.

 
