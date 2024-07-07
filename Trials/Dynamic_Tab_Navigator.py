'''
Introduction:
In this problem, you are tasked with simulating a browser's tab management system. Modern web browsers allow users to open, close, and switch between multiple tabs. Your goal is to implement a system that not only allows these operations but also keeps track of the "originating" tab—a tab from which a new tab was opened.

Objective:
Develop a class, TabManager, that manages a list of open tabs and simulates the behavior of opening, closing, and switching tabs. Additionally, your system should remember which tab was active when a new tab was opened and allow returning to the originating tab when a tab is closed.

Requirements:

Class Initialization:

The TabManager class should initialize with a single tab opened (tab index 0) and set as the current active tab.
Opening a New Tab:

Implement a method open_tab() that opens a new tab. The new tab should be added to the end of the list of tabs and should become the new current tab.
The new tab should record the index of the tab from which it was opened (the originating tab).
Switching Tabs:

Implement a method switch_tab(newTab) where newTab is the index of the tab to switch to. This method should change the current active tab to newTab.
Closing a Tab:

Implement a method close_tab(tabToClose) where tabToClose is the index of the tab to be closed.
If the tab to be closed is the current tab, the browser should try to switch back to the originating tab if it still exists. If the originating tab does not exist or if tabToClose is not the current tab, the next available tab to the right should become the current tab. If no right tab exists, switch to the left tab.
If the last tab is closed, the browser should indicate that no tabs are open.
Display State:

Implement a method display_tabs() that prints the current list of tabs and the index of the current active tab.
Example Operations and Expected Output:

plaintext
Copy code
manager = TabManager()
manager.open_tab()  # Opens second tab, index 1, originating from tab 0
manager.open_tab()  # Opens third tab, index 2, originating from tab 1
manager.switch_tab(0)  # Switches to first tab, index 0
manager.close_tab(2)  # Closes third tab, no need to switch tabs as it is not current
manager.display_tabs()  # Should display: Tabs: [0, 1], Current Tab: 0
Constraints:

Tab indices should always be integers.
Operations should handle invalid indices gracefully by printing an error message.

'''

from collections import defaultdict

class TabManager:
    def __init__(self):
        self.currentTab = 0
        self.origin = defaultdict(list)
        self.totalTabs = [0] # [0,1]
    
    def open_tab(self):
        currentTab = len(self.totalTabs)
        self.totalTabs.append(currentTab)
        self.origin[self.currentTab].append(currentTab) # {0:[1]}
        self.currentTab = currentTab
        print(self.origin)
    
    def switch_tab(self,currentTab):
        if currentTab in self.totalTabs:
            self.currentTab = currentTab
    
    def close_tab(self,tabToClose):
        if tabToClose in self.totalTabs:
            index = self.totalTabs.index(tabToClose)
            
            # Remove the tab from the list
            del self.totalTabs[index]
            
            # If the current tab is the one being closed, determine the new current tab
            if self.currentTab == tabToClose:
                if len(self.origin[tabToClose]) > 0:
                    # If the tab has originating tabs, revert to the most recent originating tab
                    self.currentTab = self.origin[tabToClose][-1]
                elif len(self.totalTabs) > index:
                    # Otherwise, move to the next right tab if it exists
                    self.currentTab = self.totalTabs[index] if index < len(self.totalTabs) else self.totalTabs[-1]
                else:
                    # Or move to the last available tab
                    self.currentTab = self.totalTabs[-1] if self.totalTabs else -1
            # print(self.currentTab)
            # Clean up any originating references if needed
            if tabToClose in self.origin:
                del self.origin[tabToClose]

            # Update origin lists to remove closed tab
            for origin_tabs in self.origin.values():
                if tabToClose in origin_tabs:
                    origin_tabs.remove(tabToClose)
            print(self.origin)
            print(self.currentTab)

def test_tab_manager():
    manager = TabManager()
    manager.open_tab()  # Opens second tab, index 1
    manager.open_tab()  # Opens third tab, index 2
    # manager.switch_tab(1)  # Switches to second tab
    manager.open_tab()  # Opens fourth tab, index 3
    # manager.close_tab(2)  # Closes third tab
    # assert manager.totalTabs == [0, 1], "Failed: Tabs should be [0, 1]"
    assert manager.currentTab == 3, "Failed: Current tab should be 1"
    manager.switch_tab(1)  # Switches to second tab
    manager.close_tab(1)  # Closes second tab
    # assert manager.totalTabs == [0], "Failed: Only tab 0 should remain"
    # assert manager.currentTab == 0, "Failed: Current tab should switch to 0"
    print("All tests passed!")

test_tab_manager()

'''

[0,1] # origin = {0:[1]} currentab = 1
[0,1,2] # origin = {0:[1],1:[2]} current tab  = 2
close_tab()
 jump to 1
 
 2
 switch tab = 1
 close_tab(1):- 1
 
'''