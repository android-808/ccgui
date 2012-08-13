#!/usr/bin/env python3

"""
Configuration wizard for conky-colors.

At the moment:
All Pages use a grid based layout.
All pages are using a custom wrapper around Gtk.Grid.attach() so as to track rows.
All currently coded options are displayed when default is selected.
Clicking back on options and then forward again results in a bug.
First attempt at meeting Gnome HIG: http://developer.gnome.org/hig-book/3.0/design-window.html.en
"""

# Standard library imports
import os
# Local imports
import ccgui.common

from gi.repository import Gtk

# Global variables
# Function definitions

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
                                    yscale = 0.0)
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
    
def add_check_button(page, label):
    button = Gtk.CheckButton(label = label,
                                        hexpand = True,
                                        margin_left = 18)
    return button
    
def add_entry(page):
    entry = Gtk.Entry(halign = Gtk.Align.START,
                             hexpand=True)
    return entry
    

# Classes
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
        

class IntroPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Introduction", pagetype=Gtk.AssistantPageType.INTRO)
        l = add_label(self, "<b>Conky-Colors Configuration Wizard</b>\nThis wizard will guide you through configuring the display options of Conky-Colors.")
        l.set_vexpand(True)
        add_wide_control(self,l)
        
        
class ModePage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Mode", pagetype=Gtk.AssistantPageType.CONTENT)
                
        add_section_title(self, "Mode")
        
        l = add_label(self, "Descriptive text.\n\nLua support needs to be built into Conky to correctly display for but Default.")
        add_wide_control(self,l)
        
        l = add_label(self, "Layout Mode:")
        modes = Gtk.ListStore(str)
        modes.append(["Default"])
        modes.append(["Board"])
        modes.append(["Cairo"])
        modes.append(["Ring"])
        modes.append(["Slim"])
        modes.append(["SLS"])
        
        """
        We can hook up the combobox to the image so that the preview shows the selected mode.
        """
        self.mode = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                                   hexpand=True)
        self.mode.set_model(modes)
        self.mode.set_active(0)
                
        add_row(self, l, self.mode)
                
        image = Gtk.Image()
        #image.set_from_file("/usr/share/ccgui/conkypreview.png")
        image.set_from_file(ccgui.common.get_image("conkypreview.png"))
        add_wide_control(self,image)
        
class OptionsPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Options", pagetype=Gtk.AssistantPageType.CONTENT) 
        label = Gtk.Label(label="This section allows you to customize the selected mode.", use_markup=True)
        
    def prepare(self, wizard):
        print("In function ok")
        if wizard.mode.default.get_active():
            print("In If OK")

class GeneralPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "Language")
        
        l = add_label(self, "Select the langauge used to display labels and headings.")
        add_wide_control(self,l)
        
        l = add_label(self, "Language:")
        languages = Gtk.ListStore(str)

        languages.append(["English"])
        languages.append(["Bulgarian"])
        languages.append(["Estonian"])
        languages.append(["French"])
        languages.append(["German"])
        languages.append(["Italian"])
        languages.append(["Polish"])
        languages.append(["Portuguese"])
        languages.append(["Russian"])
        languages.append(["Spanish"])
        languages.append(["Ukrainian"])
        self.language = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                                   hexpand=True)
        self.language.set_model(languages)
        self.language.set_active(0)
        add_row(self, l, self.language)
    
        add_divider(self)
        
        add_section_title(self, "Theme")
        
        l = add_label(self, "Theme chooser")
        add_wide_control(self,l)
        

class SystemPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "System")
        
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)
        
        self.cpu = add_check_button(self, "Enable CPU usage monitor.")
        add_wide_control(self,self.cpu)
        
        self.cputemp = add_check_button(self, "Enable CPU temperature monitoring.")
        add_wide_control(self,self.cputemp)
                
        self.swap = add_check_button(self, "Enable swap usage monitor.")
        add_wide_control(self,self.swap)
        
        self.battery = add_check_button(self, "Enable battery monitor.")
        add_wide_control(self,self.battery)
        
class GMailPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "GMail")
        
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)

        w = add_check_button(self, "Enable GMail support.") 
        add_wide_control(self,w)
        
        l = add_label(self, "Username:")
        w = add_entry(self)
        add_row(self, l, w)
        
        l = add_label(self, "Password:")
        w = add_entry(self)
        add_row(self, l, w)
        
class WeatherPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "Weather")
        
        l = add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        add_wide_control(self,l)

        w = add_check_button(self, "Enable weather support.") 
        add_wide_control(self,w)
        
        l = add_label(self, "Area code:")
        w = add_entry(self)
        add_row(self, l, w)
        
"""
Board Mode
"""
class BoardPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "Board/SLIM Mode Options")
        add_divider(self)
        add_section_title(self, "Appearance")
        
        l = add_label(self, "Screen width:")
        w = add_entry(self)
        add_row(self, l, w)
        
        l = add_label(self, "Screen height:")
        w = add_entry(self)
        add_row(self, l, w)
        
        w = add_check_button(self, "Remove background.") 
        add_wide_control(self,w)
        
        l = add_label(self, "Fix ring position:")
        w = add_entry(self)
        add_row(self, l, w)
        
        add_divider(self)
        
        add_section_title(self, "Weather")
        
        l = add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        add_wide_control(self,l)

        w = add_check_button(self, "Enable weather support.") 
        add_wide_control(self,w)
        
        l = add_label(self, "Area code:")
        w = add_entry(self)
        add_row(self, l, w)

class CairoPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "Cairo Mode Options")
        
        add_divider(self)        
        add_section_title(self, "System")
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)
        
        l = add_label(self, "CPU core selector")
        add_wide_control(self,l)
        
        self.swap = add_check_button(self, "Enable swap usage monitor.")
        add_wide_control(self,self.swap)
        
        add_divider(self)        
        add_section_title(self, "Clock")
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)
        
        l = add_label(self, "Clock Mode:")
        modes = Gtk.ListStore(str)
        modes.append(["Disabled"])
        modes.append(["Cairo"])
        modes.append(["Big Cairo"])
        self.clock = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                      hexpand=True)
        self.clock.set_model(modes)
        self.clock.set_active(0)
        add_row(self, l, self.clock)
        
        add_divider(self)        
        add_section_title(self, "Media Player Support")
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)
        
        #Reuse options for each player.
        playermodes = Gtk.ListStore(str)
        playermodes.append(["Disabled"])
        playermodes.append(["Cairo"])
        playermodes.append(["Cairo-Case"])
        playermodes.append(["Cairo-CD"])
        playermodes.append(["Cairo-Glassy"])
        playermodes.append(["Lua"])
        
        l = add_label(self, "Banshee:")
        self.banshee = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                        hexpand=True)
        self.banshee.set_model(playermodes)
        self.banshee.set_active(0)
        add_row(self, l, self.banshee)
        
        l = add_label(self, "Clementine:")
        self.clementine = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                           hexpand=True)
        self.clementine.set_model(playermodes)
        self.clementine.set_active(0)
        add_row(self, l, self.clementine)
        
        l = add_label(self, "Rhythmbox:")
        self.rhythmbox = Gtk.ComboBoxText(halign = Gtk.Align.START,
                                         hexpand=True)
        self.rhythmbox.set_model(playermodes)
        self.rhythmbox.set_active(0)
        add_row(self, l, self.rhythmbox)
        
        
                
        
        
class RingPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "Ring Mode Options")
        add_divider(self)
        add_section_title(self, "Appearance")

class SLSPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        add_section_title(self, "SLS Mode Options")
        add_divider(self)
        add_section_title(self, "Appearance")
        
        self.nobg = add_check_button(self, "Remove background.") 
        add_wide_control(self,self.nobg)
        
        add_divider(self)
        
        add_section_title(self, "Weather")
        
        l = add_label(self, "Descriptive text.\n\nInclude some information on where to get the codes.")
        add_wide_control(self,l)

        w = add_check_button(self, "Enable weather support.") 
        add_wide_control(self,w)
        
        l = add_label(self, "Area code:")
        w = add_entry(self)
        add_row(self, l, w)
        
        add_divider(self)
        
        add_section_title(self, "GMail")
        
        l = add_label(self, "Descriptive text")
        add_wide_control(self,l)

        l = add_label(self, "Username:")
        self.gmailusername = add_entry(self)
        add_row(self, l, self.gmailusername)
        
        l = add_label(self, "Password:")
        self.gmailpassword = add_entry(self)
        add_row(self, l, self.gmailpassword)

       
class ConfirmationPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Confirmation", pagetype=Gtk.AssistantPageType.CONFIRM)
        l = add_label(self, "<b>Are you sure you want to continue?</b>\nApplying these changes will overide the current configuration.")
        l.set_vexpand(True)
        add_wide_control(self,l)

        
class SummaryPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Summary", pagetype=Gtk.AssistantPageType.SUMMARY) 
        l = add_label(self, "<b>Configuration Complete</b>\nSay something magical about what's happened and provide update advice.")
        l.set_vexpand(True)
        add_wide_control(self,l)
        
"""
This class is in charge of managing the wizard.
All navigation controls, apply, cancel etc. are handled here.
"""        
class Assistant(Gtk.Assistant):

    def __init__(self):
        Gtk.Assistant.__init__(self)
        self.set_resizable(False)
    	
        """
        Connect signals
        """
        #At the moment we just jump page on apply until functionality is in place.       
        self.connect("apply", self.on_apply, "Apply")
        self.connect("cancel", self.button_pressed, "Cancel")
        self.set_forward_page_func(self.forward_page, None)
        self.connect("prepare", self.prepare_action)

        """
        Set up main window.
        """
        self.set_title("Conky-Colors Configuration Wizard")

                 
        """ 
        Create the pages in the order they should be displayed.
        Put alternatives for the same page in order.
        """
        self.current_page = None  
        self.commandline = "NULL"
        self.intro    = IntroPage(self)
        self.mode   =  ModePage(self)
        self.general = GeneralPage(self)
        # Default Mode - insert all subpages together to simplify navigation.
        self.system = SystemPage(self)
        self.gmail    = GMailPage(self)
        self.weather= WeatherPage(self)
        # Board/SLIM Mode - one page, same options.
        self.board   = BoardPage(self)
        self.cairo    = CairoPage(self)
        self.ring      = RingPage(self)
        self.sls        = SLSPage(self)
        
        
        
        
        self.confirm = ConfirmationPage(self)
        self.summary = SummaryPage(self)
        
        """
        Show all controls
        """
        self.show_all()
     
    def prepare_action(self, assistant, page):
        print("Preparing page ", assistant.get_page_title(page))
        #self.current_page = assistant.get_page_title(page)

        # Configure the final page.
        if page == self.summary:
            self.connect("close", self.button_pressed, "Close")
    
    """
    Code to display correct option page(s) for each mode.
    Missing checks to jump to summary on completion.
    """
    def forward_page(self, page_number, data):
        
        if page_number == self.general.page_number:
            if self.mode.mode.get_active() == 1 or self.mode.mode.get_active() == 4 :
                return self.board.page_number
            if self.mode.mode.get_active() == 2 :
                return self.cairo.page_number
            if self.mode.mode.get_active() == 3 :
                return self.ring.page_number
            if self.mode.mode.get_active() == 5 :
                return self.sls.page_number

        return page_number + 1
    
    
    def button_pressed(self, assistant, button):
        Gtk.main_quit()
    
    """
    This is where the magic need to happen, here or generated on
    """
    def on_apply(self, assistant, button):
        self.commandline = "conky-colors"
        
        if self.mode.mode.get_active() == 5:
            self.commandline += " --sls"
            if self.sls.nobg.get_active() == True:
                self.commandline += " --nobg"
            if self.sls.gmailusername.get_text_length() > 0:
                self.commandline += " --user=" + self.sls.gmailusername.get_text()
            if self.sls.gmailpassword.get_text_length() > 0:
                self.commandline += " --passwd=" + self.sls.gmailpassword.get_text()
        
        print("Command:" + self.commandline)
        #os.system(self.commandline)
            
            
                
def main():
    print("CCGUI Version:" +  ccgui.common.get_version())
    win = Assistant()
    win.show()
    Gtk.main()

# Main
if __name__ == "__main__":
    main()
    
