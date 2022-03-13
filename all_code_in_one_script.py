# The following class defines Task object 
class Task:

  isChecked = False
  
  def __init__(self, status, priority, tasks, name):
      self.status = status
      self.priority = priority
      self.tasks = tasks
      self.name = name


# The following class defines a TaskExecutor object 
class TaskExecutor():

 def __init__(self):
     return
      
# Execution start from here, checks first for a cycle task pointer and if OK then continues with task execution. 
 def executeMain(self, tasks, option):
    if self.isCycleExist(tasks):
        return
    self.executeAllTasks(tasks, option)
 
# Runs over each task in the tree of tasks and makes sure each task was visited only once by changing the "isChecked" indicator to True on first visit.
 def isCycleExist(self,tasks):
    if not tasks:
        return False
    for x in tasks:
        if not x.isChecked:
            x.isChecked = True
            if self.isCycleExist(x.tasks):
                return True
        else:
            print('Aborted! task cycle found in tasks name ' + x.name)
            return True
    return False

# Execute the tasks in the order according to the "option" (A/B) parameter input.
 def executeAllTasks(self, tasks, option):
    if not tasks: # Exit if list of tasks empty
        return
    
    if option == 'A':
        self.execute_a(tasks, option)
    elif option == 'B':
        self.execute_b(tasks, option)
        

# Sorts the list of tasks into 2 groups (lists), with/without dependencies, and then execute the tasks with no dependencies first.
 def execute_a(self,tasks, option):
        # Sort by dependencies
        tasksWithDependencies = []
        tasksWithoutDependencies = []
        for x in tasks:
            if x.tasks :
                tasksWithDependencies.append(x)
            else:
                tasksWithoutDependencies.append(x)
     
        # Execute option 'A' logic
        for x in tasksWithoutDependencies:
            self.executeTaskAction(x)
        for x in tasksWithDependencies:
            self.executeAllTasks(x.tasks, option)
            self.executeTaskAction(x)
 
# Sorts the list of tasks by priority and execute them based on priority.
 def execute_b(self, tasks, option):
        # Sort by priority
        tasksSorted = self.sortByPriority(tasks)
        # Run option 'B' logic
        for x in tasksSorted:
            self.executeAllTasks(x.tasks, option)
            self.executeTaskAction(x)

# Sorts the list of tasks while assuming that when the value is low then its priority is higher.
 def sortByPriority(self,tasks):
        tasksByPriority = []
        while tasks:
            minimum = tasks[0]  
            for x in tasks: 
                if x.priority < minimum.priority:
                    minimum = x
            tasksByPriority.append(minimum)
            tasks.remove(minimum) 
        return tasksByPriority
  
# The task execute action: prints the task name and changes the task status to 'done'     
 def executeTaskAction(self,task):
        if not task or task.status == 'done':
            return
        print('Task ' + task.name + ' is executed!')
        task.status = 'done'
        return
    
     
if __name__ == "__main__":
    e = TaskExecutor()
     
    
    aSubTasks = [ Task(status = 'pending', priority = '5', tasks = [] , name = 'a1'),
         Task(status = 'pending', priority = '8', tasks = [] , name = 'a2'),
         Task(status = 'pending', priority = '6', tasks = [] , name = 'a3') ]
    
    
    bSubTasks = [ Task(status = 'pending', priority = '5', tasks = [] , name = 'b1'),
         Task(status = 'pending', priority = '8', tasks = [] , name = 'b2'),
         Task(status = 'pending', priority = '6', tasks = [] , name = 'b3') ]
    
    
    cSubTasks = [ Task(status = 'pending', priority = '5', tasks = [] , name = 'c1'),
         Task(status = 'pending', priority = '8', tasks = [] , name = 'c2'),
         Task(status = 'pending', priority = '6', tasks = [] , name = 'c3') ]
    
    
    dSubTasks = [ Task(status = 'pending', priority = '5', tasks = [] , name = 'd1'),
         Task(status = 'pending', priority = '8', tasks = [] , name = 'd2'),
         Task(status = 'pending', priority = '6', tasks = [] , name = 'd3') ]
    
    l = [ Task(status = 'pending', priority = '9', tasks = aSubTasks , name = 'a'),
         Task(status = 'pending', priority = '5', tasks = bSubTasks , name = 'b'),
         Task(status = 'pending', priority = '8', tasks = cSubTasks , name = 'c'),
         Task(status = 'pending', priority = '6', tasks = dSubTasks , name = 'd') ]
         #Task(status = 'pending', priority = '6', tasks = aSubTasks , name = 'd') ]   # uncomment for testing cycle pointer
    e.executeMain(l, 'A')

    
    
    
