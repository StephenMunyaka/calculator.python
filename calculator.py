import tkinter as tk

# Define calculator class
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        # Entry widget to display results
        self.entry = tk.Entry(root, width=20, font=("Arial", 24), bd=10, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons and their layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            tk.Button(self.root, text=text, width=10, height=4, font=("Arial", 18), 
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    # Handle button clicks
    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
