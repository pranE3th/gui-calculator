import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root=root
        root.configure(bg='cyan')
        self.root.title("GUI Calculator")
        self.entry=tk.Entry(root,width=20,font=("Arial",20),bg='yellow')
        self.entry.grid(row=0,column=0,columnspan=4)
        buttons=['7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+',
                 'ac','del']
        row,col=1,0
        self.buttons=None
        for button_text in buttons:
            if button_text=='del':
                self.buttons=tk.Button(root,text=button_text,width=17,height=2,font=("Arial",20),command=lambda text=button_text:self.on_button_click(text),bg='magenta')
                self.buttons.grid(row=row,column=col,columnspan=10)
                col+=10
            else:
                self.buttons=tk.Button(root,text=button_text,width=5,height=2,font=("Arial",20),command=lambda text=button_text:self.on_button_click(text),bg='magenta')    
                self.buttons.grid(row=row,column=col,padx=5,pady=5)
            col+=1
            if col>3:
                col=0
                row+=1 
    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                #print(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text=='ac':
            self.entry.delete(0,tk.E)
        elif text=='del':
            temp=self.entry.get()
            newtext=temp[:-1]
            self.entry.delete(0,tk.E)
            self.entry.insert(tk.E,newtext)
        else:
            self.entry.insert(tk.END, text)        
        
# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()