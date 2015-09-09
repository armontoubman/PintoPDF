#!/usr/env/python3

"""
    PintoPDF is a GUI tool for 1) extracting pages from PDF files and 2) merging PDF files.
    Copyright (C) 2015, Armon Toubman <armon@armontoubman.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import platform
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import threading
import subprocess
import os

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


class ExtractFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self['padding'] = "10 10"

        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()

        self.input_entry = ttk.Entry(self, width=50, textvariable=self.input_var)
        self.input_entry.grid(column=2, row=1, sticky=tk.W, columnspan=3)

        self.select_input_button = ttk.Button(self, text="Select PDF...", command=self.select_pdf_command)
        self.select_input_button.grid(column=1, row=1, sticky=tk.W)

        self.from_page = tk.StringVar()
        self.to_page = tk.StringVar()

        self.from_page_label = ttk.Label(self, text='From page: ')
        self.from_page_entry = ttk.Entry(self, width=10, textvariable=self.from_page)

        self.to_page_label = ttk.Label(self, text='To page: ')
        self.to_page_entry = ttk.Entry(self, width=10, textvariable=self.to_page)

        self.from_page_label.grid(column=1, row=2, sticky=tk.W)
        self.from_page_entry.grid(column=2, row=2, sticky=tk.W)
        self.to_page_label.grid(column=1, row=3, sticky=tk.W)
        self.to_page_entry.grid(column=2, row=3, sticky=tk.W)

        self.output_entry = ttk.Entry(self, width=50, textvariable=self.output_var)
        self.output_entry.grid(column=2, row=4, sticky=tk.W, columnspan=3)

        self.save_as_button = ttk.Button(self, text="Save as...", command=self.save_as_command)
        self.save_as_button.grid(column=1, row=4, sticky=tk.W)

        self.extract_button = ttk.Button(self, text="Extract pages", command=self.extract)
        self.extract_button.grid(column=1, row=5, sticky=tk.W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        for i in range(0, 99):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

    def select_pdf_command(self):
        options = {}
        options['defaultextension'] = '.pdf'
        options['filetypes'] = [('PDF', '*.pdf'), ('All files', '.*')]
        options['initialdir'] = '~'
        filename = filedialog.askopenfilename(**options)
        if filename != '':
            self.input_var.set(filename)

    def save_as_command(self):
        options = {}
        options['defaultextension'] = '.pdf'
        options['filetypes'] = [('PDF', '*.pdf')]
        options['initialdir'] = '~'
        filename = filedialog.asksaveasfilename(**options)
        if filename != '':
            self.output_var.set(filename)

    def extract(self):
        input_string = self.input_var.get()
        output_string = self.output_var.get()
        from_page = int(self.from_page.get())
        to_page = int(self.to_page.get())

        def run():
            reader = PdfFileReader(open(input_string, 'rb'))
            writer = PdfFileWriter()

            for i in range(from_page - 1, to_page):
                writer.addPage(reader.getPage(i))

            with open(output_string, 'wb') as f:
                writer.write(f)

            messagebox.showinfo("Pages extracted", "New file saved as " + output_string)

        thread = threading.Thread(target=run)
        thread.start()


class MergeFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.pdf_icon = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAADAFBMVEUEBARaWlhkZGNvb3h6eoKEBASEhIKEhI2PBASPj42ampekpKyvBASvr7e6ure6usHExMHPT07PZGPPz8zPz9baBATaGhnaOjnaT07ahILaurfa2tba2uHkREPkRE7kWljkb23kj43kmqLkr6zk5OHk7+vvT07venjvr6zvusHvz9bv2uHv5OHv7+vv7/b6BAT6Dw/6Dxn6Ghn6JCT6JC76Ly76Ojn6OkP6REP6T1j6ZGP6b236b3j6eoL6+gT6+vYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///8CvJHcAAABAHRSTlP///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8AU/cHJQAAAAlwSFlzAAALEgAACxIB0t1+/AAAALNJREFUGJVNzNkOgjAUBNAq7hvVVkVbBeS624KoiFv6/1+FxULiJPMw52FQlmWoWjFB+ciLbdvud5u8oxf6vB5pek+S26SheBtl6J1c4igKw3HPUrmg5zU+6x2OW23LqmmYtIrUgeABRr9TSggfMmAUMwPAuHRAACNQgmDTlRRASwC1lf5OAStAiIMTBMvFZiYNSOnuj1Kt5yNh4OT6+gD0KTfgeRKAM0IwNaCUELnQEv7zBc4yPuudaxuRAAAAAElFTkSuQmCC")

        self['padding'] = "10 10"

        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.output_var = tk.StringVar()

        self.input_frame = ttk.Frame(self)
        self.input_frame['padding'] = "0"

        self.input_list = ttk.Treeview(self.input_frame, height=3, columns=(), show='tree headings')
        self.input_list.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S), columnspan=4)
        self.input_list.heading('#0', text='Files to merge')

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.input_list_y = tk.Scrollbar(self.input_frame, orient=tk.VERTICAL)
        self.input_list_y.grid(column=5, row=1, sticky=tk.N + tk.S)

        self.input_list.config(yscrollcommand=self.input_list_y.set)
        self.input_list_y.config(command=self.input_list.yview)

        self.input_list.bind("<Delete>", lambda e: self.remove_pdf_command())

        self.input_frame.grid(column=1, row=1, sticky=(tk.N, tk.W, tk.E, tk.S), columnspan=4)
        self.input_frame.grid_columnconfigure(1, weight=1)
        self.input_frame.grid_rowconfigure(1, weight=1)

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(column=6, row=1, sticky=tk.N)

        self.add_pdf_button = ttk.Button(self.button_frame, text="Add...", command=self.add_pdf_command)
        self.add_pdf_button.grid(column=0, row=0, sticky=tk.N)
        self.add_pdf_button.bind("+", lambda e: self.add_pdf_command())

        self.remove_pdf_button = ttk.Button(self.button_frame, text="Remove", command=self.remove_pdf_command)
        self.remove_pdf_button.grid(column=0, row=1, sticky=tk.N)

        self.move_up_button = ttk.Button(self.button_frame, text="Move up", command=self.move_up_command)
        self.move_up_button.grid(column=0, row=2, sticky=tk.N)

        self.move_down = ttk.Button(self.button_frame, text="Move down", command=self.move_down_command)
        self.move_down.grid(column=0, row=3, sticky=tk.N)

        self.view_pdf = ttk.Button(self.button_frame, text="View PDF", command=self.view_pdf_command)
        self.view_pdf.grid(column=0, row=4, sticky=tk.N)

        self.output_frame = ttk.Frame(self)
        self.output_frame.grid(column=1, row=4, sticky=tk.W)

        self.output_entry = ttk.Entry(self.output_frame, width=50, textvariable=self.output_var)
        self.output_entry.grid(column=2, row=1, sticky=tk.W, padx=(10, 20))

        self.save_as_button = ttk.Button(self.output_frame, text="Save as...", command=self.save_as_command)
        self.save_as_button = ttk.Button(self.output_frame, text="Save as...", command=self.save_as_command)
        self.save_as_button.grid(column=1, row=1, sticky=tk.W)

        self.merge_button = ttk.Button(self, text="Merge files", command=self.merge)
        self.merge_button.grid(column=1, row=5, sticky=tk.W)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def add_pdf_command(self):
        filenames = self.askopenfilenames()
        if filenames != '':
            for filename in filenames:
                self.input_list.insert('', 'end', image=self.pdf_icon, text=filename, values=('"' + filename + '"'))

    def askopenfilename(self):
        options = {}
        options['defaultextension'] = '.pdf'
        options['filetypes'] = [('PDF', '*.pdf'), ('All files', '.*')]
        options['initialdir'] = '~'
        filename = filedialog.askopenfilename(**options)
        return filename

    def askopenfilenames(self):
        options = {}
        options['defaultextension'] = '.pdf'
        options['filetypes'] = [('PDF', '*.pdf'), ('All files', '.*')]
        options['initialdir'] = '~'
        filenames = filedialog.askopenfilenames(**options)
        return self.tk.splitlist(filenames)

    def remove_pdf_command(self):
        if self.input_list.focus() != '':
            self.input_list.delete(self.input_list.focus())
        pass

    def move_up_command(self):
        focus = self.input_list.focus()
        index = self.input_list.index(focus)
        self.input_list.move(focus, '', index - 1)
        pass

    def move_down_command(self):
        focus = self.input_list.focus()
        index = self.input_list.index(focus)
        self.input_list.move(focus, '', index + 1)
        pass

    def view_pdf_command(self):
        if self.input_list.focus() != '':
            filename = self.input_list.item(self.input_list.focus())['text']
            if sys.platform.startswith('darwin'):
                subprocess.call(('open', filename))
            elif os.name == 'nt':
                os.startfile(filename)
            elif os.name == 'posix':
                subprocess.call(('xdg-open', filename))

    def save_as_command(self):
        filename = self.asksaveasfilename()
        if filename != '':
            self.output_var.set(filename)

    def asksaveasfilename(self):
        options = {}
        options['defaultextension'] = '.pdf'
        options['filetypes'] = [('PDF', '*.pdf')]
        options['initialdir'] = '~'
        filename = filedialog.asksaveasfilename(**options)
        return filename

    def merge(self):
        inputs = [self.input_list.item(item)['text'] for item in self.input_list.get_children()]
        output = self.output_var.get()

        def run():
            merger = PdfFileMerger()
            for input_string in inputs:
                if input_string != '':
                    merger.append(PdfFileReader(open(input_string, 'rb')))
            if output != '':
                merger.write(output)

            messagebox.showinfo("Files merged", "New file saved as " + output)

        thread = threading.Thread(target=run)
        thread.start()


class PintoPDF(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        style = ttk.Style()
        if platform.system() == 'Linux':
            style.theme_use('clam')

        self.master.option_add('*tearOff', False)  # disable all tearoff's
        self._menu = Menu(self.master, name='menu')
        self.master.config(menu=self._menu)

        file_menu = Menu(self._menu, name='file_menu')
        self._menu.add_cascade(label='File', menu=file_menu, underline=0)
        exit_label = 'Exit'
        if sys.platform.startswith('darwin'):
            exit_label = 'Quit'
        file_menu.add_command(label=exit_label, command=self.exit_command, underline=1)

        help_menu = Menu(self._menu, name='help_menu')
        self._menu.add_cascade(label='Help', menu=help_menu, underline=0)
        help_menu.add_command(label='About PintoPDF', command=self.about_command, underline=0)

        self['padding'] = "10 10"

        self.notebook = ttk.Notebook(self)

        self.extract_frame = ExtractFrame(self.notebook)
        self.notebook.add(self.extract_frame, text="Extract pages")

        self.merge_frame = MergeFrame(self.notebook)
        self.notebook.add(self.merge_frame, text="Merge files")

        self.notebook.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    def exit_command(self):
        self.master.destroy()

    def about_command(self):
        messagebox.showinfo("About PintoPDF", """PintoPDF by Armon Toubman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.""")


def main(argv):

    name = "PintoPDF"

    root = tk.Tk(className=name)
    root.title(name)

    PintoPDF(root).grid(sticky=tk.N + tk.S + tk.E + tk.W)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()


if __name__ == "__main__":
    main(sys.argv)
