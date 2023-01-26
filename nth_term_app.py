import customtkinter
from nth_term import nth_term

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("400x300")
root.title('nth term')

def calculate():
    seq = entry.get().split(',')
    seq = [float(i) for i in seq]
    formula = nth_term(seq)
    output.configure(text=formula)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Nth Term formula", font=("Helvetica", 36))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Sequence", font=("Helvetica", 24), width=300, height=50)
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Calculate!", font=("Helvetica", 24), command=calculate, width=300)
button.pack(pady=12, padx=10)

output = customtkinter.CTkLabel(master=frame, text="Un = ", font=("Helvetica", 24))
output.pack(pady=12, padx=10)

root.mainloop()