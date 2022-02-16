import Task, TaskExecutor

if __name__ == "__main__":
    e = TaskExecutor.TaskExecutor()
    t = Task.Task
     
    
    aSubTasks = [ t(status = 'pending', priority = '5', tasks = [] , name = 'a1'),
         t(status = 'pending', priority = '8', tasks = [] , name = 'a2'),
         t(status = 'pending', priority = '6', tasks = [] , name = 'a3') ]
    
    
    bSubTasks = [ t(status = 'pending', priority = '5', tasks = [] , name = 'b1'),
         t(status = 'pending', priority = '8', tasks = [] , name = 'b2'),
         t(status = 'pending', priority = '6', tasks = [] , name = 'b3') ]
    
    
    cSubTasks = [ t(status = 'pending', priority = '5', tasks = [] , name = 'c1'),
         t(status = 'pending', priority = '8', tasks = [] , name = 'c2'),
         t(status = 'pending', priority = '6', tasks = [] , name = 'c3') ]
    
    
    dSubTasks = [ t(status = 'pending', priority = '5', tasks = [] , name = 'd1'),
         t(status = 'pending', priority = '8', tasks = [] , name = 'd2'),
         t(status = 'pending', priority = '6', tasks = [] , name = 'd3') ]
    
    l = [ t(status = 'pending', priority = '9', tasks = aSubTasks , name = 'a'),
         t(status = 'pending', priority = '5', tasks = bSubTasks , name = 'b'),
         t(status = 'pending', priority = '8', tasks = cSubTasks , name = 'c'),
         t(status = 'pending', priority = '6', tasks = dSubTasks , name = 'd') ]
         #t(status = 'pending', priority = '6', tasks = aSubTasks , name = 'd') ]   # uncomment for testing cycle pointer
    e.executeMain(l, 'A')