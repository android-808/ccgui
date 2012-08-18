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
import ccgui.ui
from ccgui.ui import Page
from ccgui.ui import OptionsPage
from ccgui.default import Default
from ccgui.board import Board
from ccgui.cairo import Cairo
from ccgui.ring import Ring
from ccgui.sls import SLS

from gi.repository import Gtk

# Global variables
# Function definitions
# Classes

class IntroPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Introduction", pagetype=Gtk.AssistantPageType.INTRO)
        l = ccgui.ui.add_label(self, "<b>Conky-Colors Configuration Wizard</b>\nThis wizard will guide you through configuring the display options of Conky-Colors.")
        l.set_vexpand(True)
        ccgui.ui.add_wide_control(self,l)
        
        
class ModePage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Mode", pagetype=Gtk.AssistantPageType.CONTENT)
                
        ccgui.ui.add_section_title(self, "Mode")
        
        l = ccgui.ui.add_label(self, "Descriptive text.\n\nLua support needs to be built into Conky to correctly display for but Default.")
        ccgui.ui.add_wide_control(self,l)
        
        l = ccgui.ui.add_label(self, "Layout Mode:")
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
                
        ccgui.ui.add_row(self, l, self.mode)
                
        image = Gtk.Image()
        #image.set_from_file("/usr/share/ccgui/conkypreview.png")
        image.set_from_file(ccgui.common.get_image("conkypreview.png"))
        ccgui.ui.add_wide_control(self,image)
        
class GeneralPage(OptionsPage):
    def __init__(self, assistant):
        OptionsPage.__init__(self, assistant)
        
        ccgui.ui.add_section_title(self, "Language")
        
        l = ccgui.ui.add_label(self, "Select the langauge used to display labels and headings.")
        ccgui.ui.add_wide_control(self,l)
        
        l = ccgui.ui.add_label(self, "Language:")
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
        ccgui.ui.add_row(self, l, self.language)
    
        ccgui.ui.add_divider(self)
        
        ccgui.ui.add_section_title(self, "Theme")
        
        l = ccgui.ui.add_label(self, "Theme chooser")
        ccgui.ui.add_wide_control(self,l)
        

       
class ConfirmationPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Confirmation", pagetype=Gtk.AssistantPageType.CONFIRM)
        l = ccgui.ui.add_label(self, "<b>Are you sure you want to continue?</b>\nApplying these changes will overide the current configuration.")
        l.set_vexpand(True)
        ccgui.ui.add_wide_control(self,l)

        
class SummaryPage(Page):
    def __init__(self, assistant):
        Page.__init__(self, assistant=assistant, label="Summary", pagetype=Gtk.AssistantPageType.SUMMARY) 
        l = ccgui.ui.add_label(self, "<b>Configuration Complete</b>\nSay something magical about what's happened and provide update advice.")
        l.set_vexpand(True)
        ccgui.ui.add_wide_control(self,l)
        
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
        self.intro   = IntroPage(self)
        self.mode    =  ModePage(self)
        self.general = GeneralPage(self)
        # Default Mode - insert all subpages together to simplify navigation.
        self.default = Default(self)
        # Board/SLIM Mode - one page, same options.
        self.board   = Board(self)
        self.cairo   = Cairo(self)
        self.ring    = Ring(self)
        self.sls     = SLS(self)
        
        
        
        
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
                return self.board.GetFirstPage()
            if self.mode.mode.get_active() == 2 :
                return self.cairo.GetFirstPage()
            if self.mode.mode.get_active() == 3 :
                return self.ring.GetFirstPage()
            if self.mode.mode.get_active() == 5 :
                return self.sls.GetFirstPage()
                
        if page_number == self.default.GetLastPage():
            return self.confirm.page_number
        if page_number == self.board.GetLastPage():
            return self.confirm.page_number
        if page_number == self.cairo.GetLastPage():
            return self.confirm.page_number
        if page_number == self.ring.GetLastPage():
            return self.confirm.page_number
        if page_number == self.sls.GetLastPage():
            return self.confirm.page_number

        return page_number + 1
    
    
    def button_pressed(self, assistant, button):
        Gtk.main_quit()
    
    """
    This is where the magic need to happen, here or generated on
    """
    def on_apply(self, assistant, button):
        self.commandline = "conky-colors"
        
        if self.mode.mode.get_active() == 0:
            self.commandline += self.default.GetOptions()
        if self.mode.mode.get_active() == 1:
            self.commandline += " --board"
            self.commandline += self.board.GetOptions()
        if self.mode.mode.get_active() == 2:
            self.commandline += self.cairo.GetOptions()
        if self.mode.mode.get_active() == 3:
            self.commandline += self.ring.GetOptions()
        if self.mode.mode.get_active() == 4:
            self.commandline += " --slim"
            self.commandline += self.board.GetOptions()
        if self.mode.mode.get_active() == 5:
            self.commandline += self.sls.GetOptions()
                      
        print("Command:" + self.commandline)
        #os.system(self.commandline)
            
            
                
def main():
    print("CCGUI Dev Version:" +  ccgui.common.get_version())
    win = Assistant()
    win.show()
    Gtk.main()

# Main
if __name__ == "__main__":
    main()
    
