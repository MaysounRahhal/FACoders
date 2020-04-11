grade_one= {'Sami': [19, 18, 19.5, 30, 10],
            'Ahmad': [15, 14, 16, 21, 7],
            'Faris': [18, 19, 17, 26, 9],
            'Salem': [20, 20, 19, 30, 10],
            'Mahmoud': [12, 13, 11, 18, 7]}


grade_two= {'Lana': [17, 19, 20, 28, 9],
            'Dina': [18.5, 19.5, 20, 29, 10],
            'Maha': [20, 20, 18, 26, 9],
            'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9],
              'Tala': [20, 20, 19, 29, 10],
              'Lamar': [19, 20, 18, 26, 9],
              'Rola': [15, 14, 16, 19, 7],
              'Naya': [9, 6, 11, 14, 7],
              'Dalal': [1, 5, 2, 6, 7],
              'Ola': [19.5, 20, 20, 29.5, 10]}


def students_names (gradename):

    if gradename== "grade_one":

       list_name= list ( grade_one.keys() )
       return list_name
    else:
         if gradename== "grade_two":

            list_name= list ( grade_two.keys() )
            return list_name
         else:
              if gradename== "grade_three":

                  list_name= list ( grade_three.keys() )
                  return list_name
              else:
                  print (' ***** not exit grade name ****' )
                  choose()

def student_score(gradename,stuname):
    if gradename == "grade_one" and stuname in grade_one:
        sum1=sum(grade_one.get(stuname))
        return sum1
    else:
        if gradename == "grade_two" and stuname in grade_two:
            sum1=sum(grade_two.get(stuname))
            return sum1
        else:
            if gradename == "grade_three" and stuname in grade_three:
                sum1=sum(grade_three.get(stuname))
                return sum1
            else:
                print('  ***** Not exit grade name or student name *****')

                choose()
def student_count(gradename):
    if gradename== "grade_one":
        list_count=list(grade_one.keys())
        y=len(list_count)
        return y

    else:
        if gradename== "grade_two":
            list_count=list(grade_two.keys())
            y=len(list_count)
            return y
        else:
            if gradename=="grade_three":
                list_count=list(grade_three.keys())
                y=len(list_count)
                return y
            else:
                print ('   ***** not exit grade name ****' )
                choose()

def choose():
    x=input('   *****choose one : students_names  ***  student_score  ***  student_count  ***  :  ', )
    if x =='students_names' :
        gradename= input ('  ***** choose one: grade_one  ***  grade_two  ***  grade_three  *** :  ', )
        print( '    The student name  is : ', students_names(gradename))
        finish()
    else :
         if x == 'student_score'     :
            gradename= input ('  ***** choose one: grade_one  ***  grade_two  ***  grade_three  ***  :', )
            studentname=input('  ***** Enter the student name:   ' , )
            print('    The score is  : ',student_score(gradename,studentname))
            finish()
         else :
             if x== 'student_count':
                 gradename= input ( '  ***** choose one: grade_one  ***  grade_two  ***  grade_three ***:', )
                 print('   The Count of students on this grade is :   ', student_count(gradename))
                 finish()
             else:

                 print ('    ***  Try again , data not found   ***   ')
                 choose()



def  finish():
    x=input (' ***** Do you want another data *** choose ( Done ) if your finished  or ( More ) to continue  :  ' ,  )
    if x == 'Done' or x== 'done':
        print (    '***** finished ******   ')
    else :
        if x == 'more'  or x=='More' :
            choose()
        else :
            print('***************Try again**********')
            finish()

choose()
