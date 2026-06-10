# prg 1
"""class BankAccount:
    def __init__(self,name,acc_no,pin):
        self.__name=name
        self.__acc_no=acc_no
        self.__pin=pin
        print('BAnk account is created')
    def get_name(self):
        print(self.__name)
    def get_accno(self):
        print(self.__acc_no)
    def get_pin(self):
        print(self.__pin)
b1=BankAccount('scott',1234567890,1234)
b1.get_name()
b1.get_accno()
b1.get_pin()
"""



# problem statement using the Application Tracking System(ATS)
class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = set(skills) # Set
        self.jobs = [] # List
class Job:
    def __init__(self, title, req_skills):
        self.title = title
        self.req_skills = set(req_skills) # Set
        self.applicants = [] # List
class Interview:
    def __init__(self):
        self.scores = {} # Dict
    def add(self, round, score):
        self.scores[round] = score
    def avg(self):
        return sum(self.scores.values()) / len(self.scores)
# Demo
c1 = Candidate("Asha", ["Python", "SQL", "Git"])
c2 = Candidate("Ravi", ["SQL", "Excel"])
job = Job("Python Dev", ["Python", "SQL"])
job.applicants = [c1, c2]
interviews = {c1: Interview(), c2: Interview()}
interviews[c1].add("Tech", 85); interviews[c1].add("HR", 90)
interviews[c2].add("Tech", 60); interviews[c2].add("HR", 65)
print(f"--- Shortlist for {job.title} ---")
for c in job.applicants:
    if job.req_skills.issubset(c.skills) and interviews[c].avg() >= 70:
        print(f"{c.name} | Score: {interviews[c].avg():.1f}")