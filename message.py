########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    This class stores the notion of a message
########################################################################

import control

CONTROL = control.Control()

##################################################
# MESSAGE
# One message to be displayed to the user or not
##################################################
class Message:

    # Static variable for the next id
    _id_next = 100

    ##################################################
    # MESSAGE DEFAULT CONSTRUCTOR
    # Set a message to empty
    ##################################################
    def __init__(self):
        self._empty = True
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._id = Message._id_next
        self._asset_control = 4   # Default to Top Secret
        Message._id_next += 1

    ##################################################
    # MESSAGE NON-DEFAULT CONSTRUCTOR
    # Create a message and fill it
    ##################################################
    def __init__(self, text, author, date):
        self._text = text
        self._author = author
        self._date = date
        self._id = Message._id_next
        self._asset_control = 4   # Default to Top Secret
        Message._id_next += 1
        self._empty = False

    ##################################################
    # MESSAGE :: GET ID
    # Determine the unique ID of this message
    ##################################################
    def get_id(self):
        return self._id

    ##################################################
    # MESSAGE :: DISPLAY PROPERTIES
    # Display the attributes/properties but not the
    # content of this message
    ##################################################
    def display_properties(self, subject_control):
        if self._empty:
            return

        info = "You are not permitted to see the details of this message"
        if CONTROL.securityConditionRead(self._asset_control, subject_control):
            info = f"Message from {self._author} at {self._date}"

        print(f"\t[{self._id}]", info)

    ##################################################
    # MESSAGE :: DISPLAY TEXT
    # Display the contents or the text of the message
    ##################################################
    def display_text(self, subject_control):
        if CONTROL.securityConditionRead(self._asset_control, subject_control):
            print(f"\tMessage: {self._text}")
        else:
            print("You are not permitted to view this message")

    ##################################################
    # MESSAGE :: UPDATE TEXT
    # Update the contents or text of the message
    ##################################################
    def update_text(self, new_text, subject_control):
        if CONTROL.securityConditionWrite(self._asset_control, subject_control):
            self._text = new_text
        else:
            print("You are not permitted to update this message")

    ##################################################
    # MESSAGE :: CLEAR
    # Delete the contents of a message and mark it as empty
    ##################################################
    def clear(self, subject_control):
        if CONTROL.securityConditionWrite(self._asset_control, subject_control):
            self._text = "Empty"
            self._author = ""
            self._date = ""
            self._empty = True
        else:
            print("You are not permitted to clear this message")

    def setConfidentialLevel(self, stringLevel):
        self._asset_control = control.getLevel(stringLevel)

    def getConfidentialLevel(self):
        return self._asset_control