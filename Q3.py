import tkinter as tk

class ToDoApp(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title("To-Do List")
       self.geometry("300x400")


       # Create frame
       self.frame = tk.Frame(self)
       self.frame.pack(expand=True, fill="both")


       # Create form for adding tasks
       self.task_form = tk.Frame(self.frame)
       self.task_form.pack(fill="x", padx=10, pady=10)
       self.task_label = tk.Label(self.task_form, text="Task:")
       self.task_label.pack(side="left")
       self.task_entry = tk.Entry(self.task_form)
       self.task_entry.pack(side="left", fill="x", expand=True)
       self.add_button = tk.Button(self.task_form, text="Add", command=self.add_task)
       self.add_button.pack(side="right")
       self.clear_button = tk.Button(self.task_form, text="Clear", command=self.clear_form)
       self.clear_button.pack(side="right")


       # Create listbox for displaying tasks
       self.task_list = tk.Listbox(self.frame)
       self.task_list.pack(expand=True, fill="both", padx=10, pady=10)


       # Create buttons for editing and deleting tasks
       self.edit_button = tk.Button(self.frame, text="Edit", command=self.edit_task)
       self.edit_button.pack(side="left", padx=10)
       self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete_task)
       self.delete_button.pack(side="right", padx=10)


   def add_task(self):
       task = self.task_entry.get()
       self.task_list.insert("end", task)
       self.clear_form()


   def clear_form(self):
       self.task_entry.delete(0, "end")


   def edit_task(self):
       current_selection = self.task_list.curselection()
       if current_selection:
           task = self.task_list.get(current_selection)
           self.task_entry.delete(0, "end")
           self.task_entry.insert(0, task)
           self.task_list.delete(current_selection)


   def delete_task(self):
       current_selection = self.task_list.curselection()
       if current_selection:
           self.task_list.delete(current_selection)




app = ToDoApp()
app.mainloop()
