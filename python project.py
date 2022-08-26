from dbconfig import*
import datetime
date=datetime.date.today()    
def getTechId():
    myCursor.execute("select * from technology")
    allTechs = myCursor.fetchall()
    #print(allTechs)
    j = 1
    for i in allTechs:
        print(j, i[1])
        j += 1

    selTech = int(input("Select Technology: "))
    techId = allTechs[selTech-1][0]
    return techId

def callAdmin():
    while True:
        print("1.Add Student")
        print("2.Add Technology")
        print("3.Add Question")
        print("4.Logout")
        ch=int(input("Enter your choice:"))
        if ch==1:
            un=input("Enter user name")
            pwd=input("Enter Password ")
            mob=input("Enter mobile number")
            age=int(input("Enter age"))

            myCursor.execute("insert into user_profile(username,PASSWORD,age,mobile,role) values('{}','{}',{},'{}','student')".format(un,pwd,age,mob))
            myDB.commit()
            print("Student Added!")
        elif ch==2:
            try:
                tname=input("Enter technology name:")
                myCursor.execute("insert into technology(tech_name) values('{}')".format(tname))
                myDB.commit()
            except:
                print("Technology Added")
        elif ch==3:
            techId = getTechId()
            
            #print(techId)
            q = input("Enter Question: ")
            a = input("Enter Option A: ")
            b = input("Enter Option B: ")
            c = input("Enter Option C: ")
            d = input("Enter Option D: ")

            correct = input("Enter Correct(A/B/C/D): ")

            myCursor.execute("insert into question(question,opta,optb,optc,optd,correct,tech_id)values('{}','{}','{}','{}','{}','{}',{})".format(q,a,b,c,d,correct,techId))
            
            myDB.commit()
            print("Question Added!")
            

        elif ch==4:
            break

def callStudent():
    while True:
        print("1. Start Test")
        print("2. Results")
        print("3. Logout")
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            techId = getTechId()
            myCursor.execute("select * from question where tech_id={}".format(techId))
            all_questions = myCursor.fetchall()
            #print(all_questions)
            j = 1
            count = 0
            for i in all_questions:
                print(j, i[1])
                print("A.", i[2])
                print("B.", i[3])
                print("C.", i[4])
                print("D.", i[5])

                ans = input("Enter Ans (A/B/C/D): ")
                if ans == i[6]:
                    count += 1

                j += 1
            #DATE=datetime.date.today()
           
            print("Results: ",count, "/", len(all_questions))
            per = (count/len(all_questions))*100
            st = None
            
            if per>=50:
        
                st = 1
                
                
            elif per<=50:
                
        
                st = 0


            curdate=print(date)
            
            myCursor.execute("insert into results(marks,resultdate,statues) values({},{},'{}')".format(per,curdate,st))
            myDB.commit()
           
        if ch==2:
            
            break

        if ch==3:
            break
    

uname=input("ENTER USER NAME")
pwd=input("ENTER PASSWORD")
myCursor.execute("select * from user_profile where username='{}' and password='{}'".format(uname,pwd))
uData=myCursor.fetchone()
if uData:
    print("welcome {}".format(uData[1].upper()))
    if uData[5] =="admin":
        callAdmin()
    elif uData[5]=="student":
        callStudent()
else:
    print("you enter invalid username or password")
