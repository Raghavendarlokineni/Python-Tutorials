class school():
    '''intializing the school members'''
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)
    def Print(self):
        print("%s, you are the member now" %self.name)

class student(school):
    def __init__(self,name,age,grade):
        school.__init__(self,name,age)
        self.grade = int(grade)
    def Print(self):
        if self.grade <= 1:
            print("Hey %s, you are in kindergarten " %self.name)
        elif 1 < self.grade <= 5:
            print("Hey %s, you are below 5 " %self.name)
        elif 5 < self.grade <= 10:
            print("Hey %s, good going " %self.name)

class teacher(school):
    def __init__(self,name,age,salary):
        school.__init__(self,name,age)
        self.salary = int(salary)
    def Print(self):
        if self.salary <= 10000:
            print("Hey %s, its ok  " %self.name)
        elif 10000 < self.salary <= 20000:
            print("Hey %s, good salary " %self.name)
        elif 20000 < self.salary <= 50000:
            print("Hey %s, awesome earning " %self.name)

s = school('Raghu', '1')
s.Print()
print(s.age)

st = student('Ishaan', '1', '1')
st.Print()
print(s.age, s.name)

t = teacher('Gopi', '58', '20000')
t.Print()
print(t.age, t.name)

      

            
            
