import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_file="https://raw.githubusercontent.com/AmanTewariSkoolKid/datasetforskool/main/file.csv" #link for csv from github
# data of said csv file 
# id,Districts,Confirmed,Recovered,Deaths,Active
# 100,Ant,62971,18213,2828,22312
# 101,Sab,45442,95840,1042,87618
# 102,Bel,52695,15537,4110,82891
# 103,Gua,49341,53575,3749,15238
# 104,Bur,87521,50563,4633,32818
# 105,Ber,97248,53644,1658,67188
# 106,Tou,19374,57804,1718,12291
# 107,Chi,5931,51264,1676,87389
# 108,Lim,77264,56035,3288,61663
# 109,Yuu,35467,35881,4963,10711

df=pd.read_csv(csv_file)



def Fun():
    print(":)")
    print("#1. For checking the data.")
    print("#2. Reading complete file without index.")
    print("===================")
    print("Topic - Data Visualization")
    print(" ")
    print("#3. Line Chart")
    print("    Press 1 to print the data for Confirmed cases as per Districts.")
    print("    Press 2 to print the data for Recovered cases as per Districts.")
    print("    Press 3 to print the data for Death cases as per Districts.")
    print("    Press 4 to print the data for Active cases as per Districts.")
    print("    Press 5 to print All data.")
    print(" ")
    print("#4. Bar Graph")
    print("    Press 1 to print the data for Confirmed cases as per Districts.")
    print("    Press 2 to print the data for Recovered cases as per Districts.")
    print("    Press 3 to print the data for Death cases as per Districts.")
    print("    Press 4 to print the data for Active cases as per Districts.")
    print("    Press 5 to print the data in form of stack bar chart")
    print("    Press 6 to print the data in form of multi bar chart")
    print(" ")
    print("------------------------------------------------------------")
    print("DATA MANIPULATION")
    print("#5 for inserting a new row")
    print("#6 for analysis")
    print("")
    print("#7 for exiting")
    print("===============")
    


def Read_CSV():
    print("The Data")
    
    print(df)

def No_Index():
    print("Reading the file without index")
    dnf=pd.read_csv(csv_file , index_col=0)
    print(dnf)


#FOR LINE CHART:)

def line_plot():
    
    
    District=df["Districts"]
    Confirmed=df["Confirmed"]
    Recovered=df["Recovered"]
    Deaths=df["Deaths"]
    Active=df["Active"]
    plt.xlabel("Districts")

    
    user_input = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if user_input == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("Districts Wise Confirmed Cases")
        plt.plot(District, Confirmed, color='b')
        plt.show()
    elif user_input == 2:
        plt.ylabel("Recovered Cases")
        plt.title("Districts Wise Recovered Cases")
        plt.plot(District, Recovered, color='g')
        plt.show()
    elif user_input == 3:
        plt.ylabel("Death Cases")
        plt.title("Districts Wise Death Cases")
        plt.plot(District, Deaths, color='r')
        plt.show()
    elif user_input == 4:
        plt.ylabel("Active Cases")
        plt.title("Districts Wise Active Cases")
        plt.plot(District, Active, color='c')
        plt.show()
    elif user_input == 5:
        plt.ylabel("Number of cases")
        plt.plot(District, Confirmed, color='b', label = "Districts Wise Confirmed Cases")
        plt.plot(District, Recovered, color='g', label = "Districts Wise Recovered Cases")
        plt.plot(District, Deaths, color='r', label = "Districts Wise Death Cases")
        plt.plot(District, Active, color='c', label = "Districts Wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:)

def bar_plot():
    
    
    District = df["Districts"]
    Confirmed = df["Confirmed"]
    Recovered = df["Recovered"]
    Deaths = df["Deaths"]
    Active = df["Active"]
    plt.xlabel("Districts")


    user_input = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    
    if user_input == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("Districts Wise Confirmed Cases")
        plt.bar(District, Confirmed, color='b', width = 0.5)
        plt.show()
    elif user_input == 2:
        plt.ylabel("Recovered Cases")
        plt.title("Districts Wise Recovered Cases")
        plt.bar(District, Recovered, color='g', width = 0.5)
        plt.show()
    elif user_input == 3:
        plt.ylabel("Death Cases")
        plt.title("Districts Wise Death Cases")
        plt.bar(District, Deaths, color='r', width = 0.5)
        plt.show()
    elif user_input == 4:
        plt.ylabel("Active Cases")
        plt.title("Districts Wise Active Cases")
        plt.bar(District, Active, color='c', width = 0.5)
        plt.show()
    elif user_input == 5:
        plt.bar(District, Confirmed, color='b', width = 0.5, label = "Districts Wise Confirmed Cases")
        plt.bar(District, Recovered, color='g', width = 0.5, label = "Districts Wise Recovered Cases")
        plt.bar(District, Deaths, color='r', width = 0.5, label = "Districts Wise Death Cases")
        plt.bar(District, Active, color='c',width = 0.5, label = "Districts Wise Active Cases")
        plt.legend()
        plt.show()
    elif user_input == 6:
        D=np.arange(len(District))
        width=0.25
        plt.bar(D,Confirmed, width, color='b', label = "Districts Wise Confirmed Cases")
        plt.bar(D+0.25, Recovered, width, color='g', label = "Districts Wise Recovered Cases")
        plt.bar(D+0.50, Deaths, width, color='r', label = "Districts Wise Death Cases")
        plt.bar(D+0.75, Active ,width, color='c', label = "Districts Wise Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
    
Fun()
# adds the rows
def insert_row():
    col=df.columns
    print(col)
    print(df.head(1))
    j=0
    ninsert={}
    for i in col:
        print("Enter ", col[j], " value")
        nval=input()
        ninsert[col[j]]=nval
        j=j+1
        print(ninsert)
        df = df.append(ninsert, ignore_index=True)
        print("New row inserted")
    
# does analysis
def analysis():
    print("Data Frame Analysis")
    print(''' 1. Top record
    \n 2. Bottom Records
    \n 3. To print particular column
    \n 4. To print multiple columns
    \n 5. To display complete statitics of the dataframe
    \n 6. To display complte information about dataframe
    \n 7. To apply and display the data group by with count function
    \n 8. To apply and display the data using group by with more functions
    \n 9.To appying aggregate function
    \n Press enter to go back''')
    
    user_input=int(input("Enter your choice"))
    if user_input==1:
        n=int(input("Enter the number of records to be displayed"))
        print("Top ", n," records from the dataframe")
        print(df.head(n))
        
    elif user_input==2:
        n=int(input("Enter the number of records to be displayed"))
        print("Bottom ", n," records from the dataframe")
        print(df.tail(n))
        
    elif user_input==3:
        print("Name of the columns\n",df.columns)
        co=input("Enter the column name to be displayed")
        print(df[co])
        
    elif user_input==4:
        print("Name of the columns\n",df.columns)
        co=eval(input("Enter the column names as list in square bracket"))
        print(df.columns)
        
    elif user_input==5:
        print("Complete Statistics")
        print(df.describe())
        
    elif user_input==6:
        print("Information about dataframe")
        print(df.info())
        
    elif user_input==7:
        print("Name of the columns\n",df.columns)
        co=eval(input("Enter the column names as list in square bracket"))
        print(df[co])
        co1=input("Enter the column name to be displayed")
        print("Grouped columm ",co1)
        dfgroup=df[co].groupby(co1).count()
        print(dfgroup)
        
    elif user_input==8:
        print("Name of the columns\n",df.columns)
        co=eval(input("Enter the column names as list in square bracket"))
        print(df[co])
        co1=input("Enter the column name to be displayed")
        print("Grouped columm",co1,' max',' min',' count',' sum',' mean')
        dfgroup=df[co].groupby(co1).agg(['max','min','count','sum','mean'])
        print(dfgroup)
        
    elif user_input==9:
        print("Applying aggregate functions")
        print("Name of the columns\n",df.columns)
        co=eval(input("Enter the column names as list in square bracket"))
        print('Print the maximum values of the ',co,' columns')
        print(df[co].max())
        
    else:
        print("invalid data")

#program interaction starts here

user_input=int(input("Enter Your Choice: "))

while user_input == 1 or 2 or 3 or 4 or 5 or 6 or 7:

    if user_input == 1:
        Read_CSV()
        break
    elif user_input == 2:
        No_Index()
        break
    elif user_input == 3:
        line_plot()
        break
    elif user_input == 4:
        bar_plot()
        break
    elif user_input == 5:
        insert_row()
    elif user_input ==6:
        analysis()
    elif user_input==7:
        print("thank you for using...")
        break 
    else:
        print("Enter valid input")
        break
