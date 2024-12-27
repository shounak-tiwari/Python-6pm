# inheritance 
# single inheritance 
# multilevel inheritance 

class enquiry:
    def __init__(self):
        self.name = input('enter the name of student : ')
        self.contact = input('enter the contact of student : ')
        self.course = input('enter the course of student : ')
    def display(self):
        print('the name of student : ',self.name)
        print('the contact of student : ',self.contact)
        print('the course of student : ',self.course)
    

class intermediate(enquiry): 
    def __init__(self):
        enquiry.__init__(self)
        self.email = input('enter the mail : ')
        self.details_emer = input('enter the emergency details : ')

    def display(self):
        print('email of student :',self.email)
        print('emergency details of student : ',self.details_emer)
        return enquiry.display(self)

class Report_card(intermediate):
    marks = list()
    def __init__(self):
        for x in range(1,6):
            mark= float(input(f'the marks of student MCA 30{x}'))

            self.marks.append(mark)
        intermediate.__init__(self)
    
    def display(self):
        for marks in self.marks:
            print(marks)
        return super().display(self)
    

x = Report_card()

x.display()