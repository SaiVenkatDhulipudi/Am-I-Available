from collections import defaultdict
class branch:
    def __init__(self) -> None:
        self.departments=defaultdict(lambda:'')
        self.departments['CSE']="11"
        self.departments['CIVIL']="12"
        self.departments['MECH']="13"
        self.departments['AIDS']="14"
        self.departments['ECE']="15"
        self.departments['EEE']="16"
        self.departments['BS&H']="17"
        self.departments['TP']="18"
        self.departments['EC']="19"
        self.departments['Principal']="10101"
        self.departments['Rector']="10202"
        self.departments['CEO']="10303"

