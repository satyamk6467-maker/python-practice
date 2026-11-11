class student:
    schoolname ="abc school "
    def __init__(self,name,course):
        #print("wenever a new object is created i am called automatically")
        #print(self)
        self.name= name 
        self.course=course


student1= student("satyam","btech",)
print("student1 name-",student1.name)
print("student1 course-",student1.course)

student2= student("shivam","neet")
print("student2 name-",student2.name)
print("student2 course-", student2.course)
