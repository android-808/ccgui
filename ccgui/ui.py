from gi.repository import Gtk

"""
This function allows the page to keep track of the number of rows added to the grid.
Using add will mess it up though.
"""
def add_control(page, widget, width, height):
    page.attach(widget, 0, page.rows, width, height)
    page.rows += 1

"""
Used when adding an item to a grid that you want to take up the entire row.
Useful for adding titles, labels, pictures etc.
Increments row counter.
"""
def add_wide_control(page, widget):
    page.attach(widget, 0, page.rows, 2, 1)
    page.rows += 1
 
"""
Adds a label and a control to a new row, incrementing the counter.
In normal usage a label would be passed, but it could be any control.
"""    
def add_row(page, label, control):
    page.attach(label, 0, page.rows, 1, 1 )
    page.attach(control, 1, page.rows, 1, 1)
    page.rows += 1

"""
Adds a blank row to divide to separate sections within a page.
"""
def add_divider(page):
    divider = Gtk.Alignment(xalign = 0.0,
                                    yalign = 0.0,
                                    xscale = 0.0,
                                    yscale = 0.0,
                                    margin_left = 18)
    divider.set_size_request(0, 6)
    add_wide_control(page, divider)
    return divider

"""
Adds a title to identify a section of the page.
Automatically formats the string so that it is displayed in bold.
"""
def add_section_title(page, title):
    title = Gtk.Label(label = "<b>" + title + "</b>",
                           use_markup = True,
                           halign = Gtk.Align.START)
    add_wide_control(page, title)
    return title

"""
The following *do not* increase the row counter.
They are used to apply standard settings to all controls displayed on a page.
"""
def add_label(page, label):
    label = Gtk.Label(label = label,
                           use_markup = True,
                           halign = Gtk.Align.START,
                           margin_left = 18)
    return label

def add_wrapped_label(page, label):
    # margin_left seems to break alignment. I don't fully understand the layout yet.
    label = Gtk.Label(label = label,
                           use_markup = True,
                           halign = Gtk.Align.START,
                           margin_left = 18,
                           wrap = True)
                          
    return label
    
def add_check_button(page, label):
    button = Gtk.CheckButton(label = label,
                                        hexpand = True,
                                        margin_left = 18)
    return button
    
def add_entry(page):
    entry = Gtk.Entry(halign = Gtk.Align.START,
                             hexpand=True)
    return entry

"""
Base class for pages within the assistant.
Derived from Gtk.Grid, it automatically applies standard options to create a standard look and feel.
Adds itself to the supplied assistant and configures the display
"""
class Page(Gtk.Grid):
    def __init__(self, assistant, label, pagetype):
        Gtk.Grid.__init__(self, orientation=Gtk.Orientation.VERTICAL, 
                                border_width=12,
                                row_spacing=6,
                                column_spacing=12)
                             
        self.assistant = assistant
        self.page_number = self.assistant.append_page(self)
        self.assistant.set_page_type(self, pagetype)
        self.assistant.set_page_title(self, label)
        # This needs to be removed.
        self.assistant.set_page_complete(self, True)
        self.rows = 0

"""
Derived class used as a base for all options pages.
Basically just sets the title and page type automatically.
"""
class OptionsPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Options", pagetype=Gtk.AssistantPageType.CONTENT)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

