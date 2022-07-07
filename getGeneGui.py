import pandas as pd
import tkinter as tk

root = tk.Tk() #init Gui window
root.geometry('500x270')
root.title(' Gene Symbols to Affymetrix Converter')
root.config(bg='#323232')


df = pd.read_csv('GeneTable.csv', sep=';'  , engine='python') #read csv

def buttonpressed() :  #button 
    label.configure(state="normal")
    global df
    ID = Geneid.get()
    ex = df.loc[df['Gene Symbol'] == ID]
    
    if ex.empty:
     text.set("Invalid Gene ID or no match found")
     label.delete(1.0,"end")
     label.insert(1.0,text.get())
    else:
     text.set(ex[['ID', 'Sequence Type']].to_string(index=False))
     label.delete(1.0,"end")
     label.insert(1.0,text.get())
    label.configure(state="disabled")
     


### Gui elements

text = tk.StringVar()
text.set("Alexis")
entry_text = tk.StringVar()
entry_text.set("Insert Gene ID")

label = tk.Text(root,height = 12 , width = 45,  bg ="#f5f5f5" ,fg = "black" , relief="flat" , state = "disabled") #information label
label.grid(row=4, column=0, padx= 10, pady= 10)
label.pack()



Geneid = tk.Entry(textvariable = entry_text, font=('calibre',10, 'bold'))

Geneid.pack()

btn = tk.Button(root, text = 'Convert',  bg = '#f5f5f5' , command = buttonpressed) 

btn.pack()

### End of Gui Elements

root.mainloop()

