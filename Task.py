# The following class defines a Task object 
class Task:

  isChecked = False
  
  def __init__(self, status, priority, tasks, name):
      self.status = status
      self.priority = priority
      self.tasks = tasks
      self.name = name