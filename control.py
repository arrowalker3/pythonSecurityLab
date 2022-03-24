########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    This class stores the notion of Bell-LaPadula
########################################################################

# Map showing confidentiality levels
Level = {
    'Public': 0,
    'Confidential': 1,
    'Privileged': 2,
    'Secret': 3
}

def getLevel(stringLevel):
    if isinstance(stringLevel, int) is True:
        return stringLevel
    else:
        return Level[stringLevel]


class Control:
    def __init__(self):
        pass

    def securityConditionRead(self, assetControl, subjectControl):
        return subjectControl >= assetControl

    def securityConditionWrite(self, assetControl, subjectControl):
        return subjectControl <= assetControl