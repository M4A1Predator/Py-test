from xml.etree.ElementTree import Element, SubElement, ElementTree

import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from Lib.tkinter import *
from Lib.tkinter.ttk import *
from XmlReader import *
import webbrowser



class App(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.grid(row=0)
        self.create_text_field()
        self.drawnote()
        self.create_add_field()

    def create_text_field(self):
        self.window = tkinter.Frame(self.master)
        self.window.configure(bg="#000000")
        self.window.grid(row=1, column=0)

        self.head = tkinter.Label(self.master)
        self.head['text'] = "Note"
        self.head.configure(bg="#000000", fg="#FFFFFF", anchor=CENTER)
        self.head.grid(row=0,  column=0, columnspan=2)

    def create_add_field(self):
        self.window2 = tkinter.Frame(self.window)
        self.window2.grid()

        ahead = tkinter.Label(self.window2)
        ahead['text'] = "Add Link"
        ahead.grid(row=0, columnspan=2)

        head_label = tkinter.Label(self.window2)
        head_label['text'] = "Head : "
        head_label.grid(column=0, row=1)

        add_head = tkinter.Text(self.window2)
        add_head.configure(width=30, height=1)
        add_head.grid(column=1, row=1)

        url_label = tkinter.Label(self.window2)
        url_label['text'] = "URL : "
        url_label.grid(column=0, row=2)

        add_url = tkinter.Text(self.window2)
        add_url.insert(END, "")
        add_url.configure(width=30, height=2, highlightthickness=5)
        add_url.grid(column=1, row=2)

        add_but = tkinter.Button(self.window2, command=lambda: self.add_link(add_head.get("1.0", CURRENT),
                                                                             add_url.get("1.0", CURRENT)))
        add_but['text'] = "Add"
        add_but.grid()

    def drawnote(self):
        et = ElementTree()
        et.parse("fx1.xml")
        links = et.getroot()
        for h, u in links:
            lhead= tkinter.Label(self.window)
            lhead.configure(fg="cyan", bg="black", cursor="hand2")
            lhead['text'] = h.text
            lhead.grid()
            lhead.bind("<Button-1>", lambda e, ur=u.text: self.open_link(ur))
            lhead.bind("<Button-3>", lambda e, he=h.text, ur=u.text: self.popup_menu(e, he, ur))

    def open_link(self, url):
        webbrowser.open(url)

    def add_link(self, h, ur):
        # print(h)
        if h == "" or ur == "":
            messagebox.showinfo("Error", "Head and url muse be enter")
            return
        et = ElementTree()
        et.parse("fx1.xml")
        note = et.getroot()

        link = SubElement(note, "link")

        head = SubElement(link, "head")
        head.text = h
        link_url = SubElement(link, "URL")
        link_url.text = ur

        et.write("fx1.xml")
        self.refresh_window()

    def refresh_window(self):
        self.window.destroy()
        self.create_text_field()
        self.drawnote()
        self.create_add_field()

    def popup_menu(self, e, h, ur):
        iid = tkinter.Menu()
        iid.add_command(label="Remove Link : {}".format(h), command=lambda: self.remove_link(h, ur))
        iid.post(e.x_root, e.y_root)

    def remove_link(self, h, ur):
        # print(h, ur)
        et = ElementTree()
        et.parse("fx1.xml")
        note = et.getroot()
        for link in note.findall('link'):
            hd = link.find('head').text
            ud = link.find('URL').text
            if hd == h and ud == ur:
                note.remove(link)

        et.write("fx1.xml")
        self.refresh_window()


root = tkinter.Tk()
root.resizable(0, 0)
# root.geometry("%dx%d+0+0" % (0, 300))
app = App(master=root)
app.mainloop()