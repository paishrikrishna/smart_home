from datetime import datetime
from django.shortcuts import render
from .models import ongoing_task , coffee_recipei , machine_info , machine_log , coffee_logs , machine_tasks
from django.http import JsonResponse
# Create your views here.
objects = []
def main(request):
    return render(request,"index.html")

def task_main(request):
    return render(request,"task.html")

class coffee:
    #adding item in coffee log
    def __init__(self,name):
        self.name = name
        self.task_counter = 0
        self.object = coffee_logs(coffee = coffee_recipei.objects.get(name=self.name))
        self.object.save()
        print("added")
        self.tasks_values = {
        "powder" : self.object.coffee.powder,
        "sugar" : self.object.coffee.sugar,
        "water" : self.object.coffee.water,
        "milk" : self.object.coffee.milk,
        "temperature" : self.object.coffee.temperature,
        "mixer" : self.object.coffee.mixer,
        }
        self.tasks_coffee_logs = {
        "powder" : self.object.powder,
        "sugar" : self.object.sugar,
        "water" : self.object.water,
        "milk" : self.object.milk,
        "temperature" : self.object.temperature,
        "mixer" : self.object.mixer,
        }

    #return values
    def return_values(self,task_name):
        return self.tasks_values[task_name]

    def asssign_machines(self,task_name):
        self.selected_machine = list(machine_tasks.objects.filter(task = task_name))
        for i in self.selected_machine:
            if i.machine.status == False:
                # machine_info object is passed
                i.machine.status = True
                i.machine.save()
                self.machine = machine_log(
                                            machine = i.machine,
                                            task_id = self.object,
                                            task = task_name,
                                            value = self.tasks_values[task_name]
                                            )
                self.machine.save()
                # sucess code
                return 200
        # error for no vaccant or eligible machine found
        if len(self.selected_machine) > 0:
            return 404
        else:
            return 405

    def set_completed_status(self):
        self.object = coffee_logs.objects.get(id=self.object.id)
        self.object.status = True
        self.object.save()

    def check_status(self):
        try:
            # if no machine is assigned then it will raise error
            self.machine = machine_log.objects.get(id=self.machine.id)
            self.status =  self.machine.status
            print(self.status)
        except:
            return 2
        else:
            if self.status == True:
                if self.task_counter == 0:
                    self.machine.task_id.powder = True
                elif self.task_counter == 1:
                    self.machine.task_id.sugar = True
                elif self.task_counter == 2:
                    self.machine.task_id.water = True
                elif self.task_counter == 3:
                    self.machine.task_id.milk = True
                elif self.task_counter == 4:
                    self.machine.task_id.temperature = True
                elif self.task_counter == 5:
                    self.machine.task_id.mixer = True
                self.machine.task_id.save()
                self.task_counter += 1
                return 1
            else:
                return 0

def add_task(request):
    objects.append(coffee("black"))

def loop_task(request):
    #check task check_status
    global objects
    print(len(objects))
    del_objs = []
    for i in objects:
        print(i)
        if i.check_status() == 0:
            print("task in progress")
            continue

        try:
            #checks if task_counter is greater than total tasks
            task_name = list(i.tasks_values.keys())[i.task_counter]
        except:
            # if tasks_counter > total_tasks then delete its obj for list of object
            del_objs.append(i)
        else:
            # task_counter <= total_tasks assign machine
            machine_code = i.asssign_machines(task_name)

            if machine_code  == 404 :
                i.task_counter -= 1
                print("No vacant machine found")
            elif machine_code == 405:
                i.task_counter -= 1
                print("No device found")
            else:
                print(i.machine.task)
                print(i.machine.machine.name)

    for i in del_objs:
        i.set_completed_status()
        objects.remove(i)

    return JsonResponse({'status':True})
