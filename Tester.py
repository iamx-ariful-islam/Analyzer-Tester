import time
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


__normal_font  = ('Ubuntu', 11, 'bold')
__updated_date = '10.02.2025'

# connect button main function
def main_func():
    option_type  = type_options.current()

    if btn_process.cget('text') == 'Connect':
        add_log_msg(f"Please enter {"'Port Name' and 'Baudrate' for 'Serial'" if option_type else "'IP Address' and 'Port No' for 'Network'"} communication")


# remain check status
def change_state():
    add_log_msg(f"Bidirectional connection mode '{'On' if mode_var.get() else 'Off'}'")

# add log msg function
def add_log_msg(log_msg):
    byte_text_box.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {log_msg}\n")

# set placeholder text
def set_placeholder(widget, __text):
    widget.delete(0, tk.END)
    def __action(event=None):
        current_text = widget.get()
        if event and current_text == __text:  # focus in
            widget.delete(0, tk.END)
            widget.config(fg='black')
        elif not event and not current_text.strip():  # focus out
            widget.insert(0, __text)
            widget.config(fg='gray')
    # initialize placeholder
    widget.insert(0, __text)
    widget.config(fg='gray')
    widget.bind('<FocusIn>', __action)
    widget.bind('<FocusOut>', lambda _: __action(None))
        
# show current time
def show_time():
    global current_time1
    current_time1 = current_time1
    current_time2 = time.strftime('%I:%M:%S%p').lower()
    if current_time2 != current_time1:
        current_time1 = current_time2
        time_label.config(text=current_time2)
    time_label.after(200, show_time)


# root
if __name__ == '__main__':
    window = tk.Tk() # create GUI window
    window.title('Python Analyzer Tester')

    label  = tk.Label(window, text='Application output logger', font=('ubuntu', 16, 'bold'))
    label1 = tk.Label(window, text=time.strftime('%B %d|%Y (%A)'), font=__normal_font)
    label.grid(row=0, column=0, columnspan=3, padx=15, pady=(5, 0), sticky='w')
    label1.grid(row=1, column=0, columnspan=3, padx=15, pady=0, sticky='w')

    mode_var        = tk.IntVar(window)
    bytes_size      = tk.Entry(window, width=8, font=__normal_font, fg='red')
    connection_mode = tk.Checkbutton(window, text='Bidirectional Mode', cursor='hand2', variable=mode_var, onvalue=1, offvalue=0, font=__normal_font, width=15, anchor='w', command=change_state)
    time_label      = tk.Label(window, text='', font=__normal_font)
    bytes_size.grid(row=0, column=5, columnspan=2, padx=(0, 190), pady=(5, 0), sticky='e')
    connection_mode.grid(row=0, column=5, columnspan=2, padx=(0, 15), pady=(5, 0), sticky='e')
    time_label.grid(row=1, column=6, padx=15, pady=0, sticky='e')
    bytes_size.delete(0, tk.END)
    bytes_size.insert(0, '1024')
    
    byte_text_box = scrolledtext.ScrolledText(window, width=70, height=25)
    byte_text_box.grid(row=2, column=0, columnspan=7, padx=15, pady=5, sticky='nsew')
    add_log_msg(f"Application Started [updated: {__updated_date}]\n----------------------------------------------------")

    type_options = ttk.Combobox(window, values=['Network', 'Serial'], width=12, cursor='hand2', state='readonly', font=__normal_font)
    ip_com_port  = tk.Entry(window, width=15, font=__normal_font)
    port_baud_no = tk.Entry(window, width=15, font=__normal_font)
    type_options.grid(row=3, column=0, padx=(15, 0), pady=5, sticky='ew')
    ip_com_port.grid(row=3, column=1, padx=(5, 0), pady=5, sticky='ew')
    port_baud_no.grid(row=3, column=2, padx=(5, 0), pady=5, sticky='ew')
    type_options.current(0)
    [*map(set_placeholder, [ip_com_port, port_baud_no], ['Enter IP/COM', 'Port/Baudrate'])]

    empty_label = tk.Label(window, width=24)
    empty_label.grid(row=3, column=3, padx=25, pady=5, sticky='ew')

    btn_process = tk.Button(window, text='Connect', width=15, cursor='hand2', font=__normal_font, command=main_func, background='green', foreground='white')
    clear_logs  = tk.Button(window, text='Clear Logs', width=15, cursor='hand2', font=__normal_font)
    output_file = tk.Button(window, text='Output File', width=15, cursor='hand2', font=__normal_font)
    btn_process.grid(row=3, column=4, padx=(0, 5), pady=5, sticky='e')
    clear_logs.grid(row=3, column=5, padx=(0, 5), pady=5, sticky='e')
    output_file.grid(row=3, column=6, padx=(0, 15), pady=5, sticky='e')


    current_time1 = ''; show_time()
    __width_size  = 1115
    __height_size = 530

    x_axis = (window.winfo_screenwidth() / 2) - (__width_size / 2)
    y_axis = (window.winfo_screenheight() / 2) - (__height_size / 2)
    window.geometry('%dx%d+%d+%d' % (__width_size, __height_size, x_axis, y_axis-50))
    window.resizable(0, 0)
    window.mainloop()