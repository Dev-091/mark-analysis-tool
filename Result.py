import pandas as pd
import matplotlib.pyplot as plt

# Initialize result variable
result = None

# Main Menu
while(True):
    print("Main Menu")
    print("1. Fetch data")
    print("2. Dataframe Statistics")
    print("3. Display Records")
    print("4. Working on Records")
    print("5. Working on Columns")
    print("6. Search specific row/column")
    print("7. Data Visualization")
    print("8. Data analystics")
    print("9. Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        result=pd.read_csv("C:\\Users\\Dev\\Desktop\\Mark Analysis\\result.csv", index_col=0)
    elif ch==2:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while (True):
            print("Dataframe Statistics Menu")
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Exit")
            ch2=int(input("Enter choice"))
            if ch2==1:
                print(result.T)
            elif ch2==2:
                print(result.columns)
            elif ch2==3:
                print(result.index)
            elif ch2==4:
                print(result.shape)
            elif ch2==5:
                print(result.ndim)
            elif ch2==6:
                print(result.dtypes)
            elif ch2==7:
                print(result.size)
            elif ch2==8:
                break
    elif ch==3:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Display Records Menu")
            print("1. Top 5 Resords")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Details of a specific Subject")
            print("6. Display details of all subjects")
            print("7. Exit")
            ch3=int(input("Enter choice"))
            if ch3==1:
                print(result.head())
            elif ch3==2:
                print(result.tail())
            elif ch3==3:
                n=int(input("Enter how many records you want to display from the top"))
                print(result.head(n))
            elif ch3==4:
                n=int(input("Enter how many records you want to display from the bottom"))
                print(result.tail(n))
            elif ch3==5:
                st=input("Enter the subject name for which you want to see the details")
                print(result.loc[st])
            elif ch3==6:
                print("Results of XYZ school for the session 2018-19")
                print(result)
            elif ch3==7:
                break
    elif ch==4:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Working on Records Menu")
            print("1. Insert a specific subject Detail")
            print("2. Delete a specific subject Detail")
            print("3. Update a specific subject detail")
            print("4. Exit")
            ch4=int(input("Enter choice"))
            if ch4==1:
                a=input("Enter subject name")
                b=int(input("Enter number of students appeared:"))
                c=int(input("Enter highest marks obtained:"))
                d=int(input("Enter average marks obtained"))
                e=int(input("Enter number of A1's"))
                f=int(input("Enter number of A2's"))
                g=int(input("Enter percentage of A1 and A2's"))
                h=int(input("Enter number of B1's"))
                i=int(input("Enter number of B2's"))
                j=int(input("Enter number of C1's"))
                k=int(input("Enter number of C2's"))
                l=int(input("Enter number of D's"))
                m=int(input("Enter number of E's"))
                result.loc[a,:]=[b,c,d,e,f,g,h,i,j,k,l,m,0]
                print("Data successfully inserted")
            elif ch4==2:
                a=input("Enter subject name whose data needs to be deleted")
                result.drop([a],inplace=True)
                print("Data successfully deleted")
            elif ch4==3:
                a=input("Enter subject name whose data needs to be updated")
                b=int(input("Enter number of students appeared:"))
                c=int(input("Enter highest marks obtained:"))
                d=int(input("Enter average marks obtained"))
                e=int(input("Enter number of A1's"))
                f=int(input("Enter number of A2's"))
                g=int(input("Enter percentage of A1 and A2's"))
                h=int(input("Enter number of B1's"))
                i=int(input("Enter number of B2's"))
                j=int(input("Enter number of C1's"))
                k=int(input("Enter number of C2's"))
                l=int(input("Enter number of D's"))
                m=int(input("Enter number of E's"))
                result.loc[a]=[b,c,d,e,f,g,h,i,j,k,l,m,0]
                print("Data successfully updated")
            elif ch4==4:
                break
    elif ch==5:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Working on Columns Menu")
            print("1. Insert a new column data")
            print("2. Delete a specific column")
            print("3. Exit")
            ch5=int(input("Enter choice"))
            if ch5==1:
                print("Enter details")
                h=input("Enter column/heading name")
                det=eval(input("Enter details corresponding to all subject:(enclosed in [ ])"))
                result[h]=pd.Series(data=det,index=result.index)
                print("Column inserted")
            elif ch5==2:
                a=input("Enter column name which needs to be deleted")
                result.drop([a],axis=1,inplace=False)
                print("Column Temporary deleted")
            elif ch5==3:
                break
    elif ch==6:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Search Menu")
            print("1. Search for the details of a specific subject")
            print("2. Search details of a specific as per a specific column heading")
            print("3. Exit")
            ch6=int(input("Enter choice"))
            if ch6==1:
                st=input("Enter the name of the subject whose details you want to see")
                print(result.loc[st])
            elif ch6==2:
                col=input("Enter column/heading name whose details you want to see")
                print(result[col])
            elif ch6==3:
                break
    elif ch==7:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Data Visualization Menu")
            print("1. Line Plot")
            print("2. Vertical Bar Plot")
            print("3. Horizontal Bar Plot")
            print("4. Histogram")
            print("5. Exit")
            ch7=int(input("Enter choice"))
            if ch7==1:
                while(True):
                    print("Line Plot Sub Menu")
                    print("1. Subject wise Highest marks")
                    print("2. Subject wise number of students appeared")
                    print("3. Subject wise Average marks")
                    print("4. Subject wise comparison of percentage of A1 & A2")
                    print("5. Exit")
                    chline=int(input("Enter choice"))
                    if chline==1:
                        plt.plot(result.index,result['highest'],label="Highest Marks")
                        plt.title("SUBJECTWISE HIGHEST MARKS")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("HIGHEST MARKS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==2:
                        plt.plot(result.index,result['appeared'],label="Number of students appeared")
                        plt.title("SUBJECTWISE NUMBER OF STUDENTS APPEARED")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("NUMBER OF STUDENTS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==3:
                        plt.plot(result.index,result['average'],label="Average Marks obtained")
                        plt.title("SUBJECT WISE AVERAGE MARKS")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("AVERAGE MARKS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==4:
                        plt.plot(result.index,result['per'],label="Percentage of A1 and A2")
                        plt.title("SUBJECT WISE PERCENTAGE OF A1 AND A2")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("PERCENTAGE OF A1 AND A2")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==5:
                        break
            elif ch7==2:
                while(True):
                    print("Vertical Bar Plot Sub Menu")
                    print("1. Subject wise Highest marks")
                    print("2. Subject wise number of students appeared")
                    print("3. Subject wise Average marks")
                    print("4.  Subject wise comparison of percentage of A1 & A2")
                    print("5. Exit")
                    chbar=int(input("Enter choice"))
                    if chbar==1:
                        plt.bar(result.index,result['highest'],label="Highest Marks", color="green")
                        plt.title("SUBJECTWISE HIGHEST MARKS")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("HIGHEST MARKS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==2:
                        plt.bar(result.index,result['appeared'],label="Number of students appeared",color="yellow")
                        plt.title("SUBJECTWISE NUMBER OF STUDENTS APPEARED")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("NUMBER OF STUDENTS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==3:
                        plt.bar(result.index,result['average'],label="Average Marks obtained",color="orange")
                        plt.title("SUBJECT WISE AVERAGE MARKS")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("AVERAGE MARKS")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==4:
                        plt.bar(result.index,result['per'],label="Percentage of A1 and A2",color="green")
                        plt.title("SUBJECT WISE PERCENTAGE OF A1 AND A2")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("PERCENTAGE OF A1 AND A2")
                        plt.xticks(rotation=30)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==5:
                        break
            elif ch7==3:
                while(True):
                    print("Horizontal Bar Plot Sub Menu")
                    print("1. Subject wise Highest marks")
                    print("2. Subject wise number of students appeared")
                    print("3. Subject wise Average marks")
                    print("4. Subject wise comparison of percentage of A1 & A2")
                    print("5. Exit")
                    chbar=int(input("Enter choice"))
                    if chbar==1:
                        plt.barh(result.index,result['highest'],label="Highest Marks", color="green")
                        plt.title("SUBJECTWISE HIGHEST MARKS")
                        plt.ylabel("SUBJECTS")
                        plt.xlabel("HIGHEST MARKS")
                        plt.legend()
                        plt.show()
                    elif chbar==2:
                        plt.barh(result.index,result['appeared'],label="Number of students appeared",color="yellow")
                        plt.title("NUMBER OF STUDENTS APPEARED")
                        plt.ylabel("SUBJECTS")
                        plt.xlabel("NUMBER OF STUDENTS")
                        plt.legend()
                        plt.show()
                    elif chbar==3:
                        plt.barh(result.index,result['average'],label="Average Marks obtained",color="orange")
                        plt.title("SUBJECT WISE AVERAGE MARKS")
                        plt.ylabel("SUBJECTS")
                        plt.xlabel("AVERAGE MARKS")
                        plt.legend()
                        plt.show()
                    elif chbar==4:
                        plt.barh(result.index,result['per'],label="Percentage of A1 and A2",color="green")
                        plt.title("SUBJECT WISE PERCENTAGE OF A1 AND A2")
                        plt.ylabel("SUBJECTS")
                        plt.xlabel("PERCENTAGE OF A1 AND A2")
                        plt.legend()
                        plt.show()
                    elif chbar==5:
                        break
            elif ch7==4:
                while(True):
                    print("Histogram Sub Menu [Showing 5 bins] ")
                    print("1. Highest marks")
                    print("2. Average Marks")
                    print("3. Percentagae of A1 and A2")
                    print("4. Exit")
                    chbar=int(input("Enter choice"))
                    if chbar==1:
                        plt.hist(result['highest'],bins=5,label="Highest marks",color="green",edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF HIGHEST MARKS ")
                        plt.xlabel("HIGHEST MARKS")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    elif chbar==2:
                        plt.hist(result['average'],bins=5,label="Average Marks",color="yellow",edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF AVERAGE MARKS")
                        plt.xlabel("AVERAGE MARKS")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    elif chbar==3:
                        plt.hist(result['per'],bins=5,label="Percentage of A1 & A2",color="orange",edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF PERCENTAGE OF A1 & A2")
                        plt.xlabel("PERCENTAGE OF A1 and A2")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    elif chbar==4:
                        break
            elif ch7==5:
                break
    elif ch==8:
        if result is None:
            print("Please fetch data first (Option 1)")
            continue
        while(True):
            print("Data Analytics Menu")
            print("1. Subject with maximum average marks")
            print("2. Subject with minimum average marks")
            print("3. Subject with maximum highest marks")
            print("4. Subject with minimum highest marks")
            print("5. Subject with maximum percentage of A1 and A2")
            print("6. Subject with minimum percentage of A1 and A2")
            print("7. Exit")
            chana=int(input("Enter choice:"))
            if chana==1:
                m=result['average'].max()
                s=result.loc[result.average==m]
                print("Subject with maximum average marks of ",m," is\n ",s.index)
            elif chana==2:
                m=result['average'].min()
                s=result.loc[result.average==m]
                print("Subject with minimum average marks of ",m," is\n ",s.index)
            elif chana==3:
                m=result['highest'].max()
                s=result.loc[result.highest==m]
                print("Subject with maximum highest marks of ",m," is\n ",s.index)
            elif chana==4:
                m=result['highest'].min()
                s=result.loc[result.highest==m]
                print("Subject with minimum highest marks of ",m," is\n ",s.index)
            elif chana==5:
                m=result['per'].max()
                s=result.loc[result.per==m]
                print("Subject with maximum percentage of A1 and A2",s.index,"\n Percentage being",m)
            elif chana==6:
                m=result['per'].min()
                s=result.loc[result.per==m]
                print("Subject with minimum percentage of A1 and A2",s.index,"\n Percentage being",m)
            elif chana==7:
                break
    elif ch==9:
        break


