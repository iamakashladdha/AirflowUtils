import sys
'''
Python Program DagsGenerator to Generate Random Dags for the Given DagCount.
Usage: python3 generatedags.py <dagcount>
'''

def generateDags(dagcount):

    try: 
        x=1
        while x <=dagcount:
            FileName = f"dags/dag{x}.py"
            Data = "from airflow.decorators import dag, task" + "\nfrom datetime import datetime, timedelta" + "\nfrom airflow.operators.dummy import DummyOperator" + "\n\n@dag(start_date=datetime(2021, 1, 1),schedule_interval=\"@daily\", catchup=False)" + f"\n\ndef dag_{x}():" + "\n\top = DummyOperator(task_id=\"task\")" + f"\n\ndag = dag_{x}()"

            with open(FileName, 'w') as f:
                f.write('{}'.format(Data))
            x = x+1
        print(str(dagcount) + " number of dags generated in the folder dags.")

    except Exception as e:
        print("Got an Exception while genrating Dags, Exception: " + str(e))

if __name__ == '__main__':
    try:
        dagcount = int(sys.argv[1].lower().strip()) #param to get count of Dags
        generateDags(dagcount)

    except IndexError:
        #Rasing an Exception in case one or more required command line arguments are missing
        print(" ERROR: Please Input correct set of input parameter to start the execution of Dag Generator utility \n Required format is python3 generatedags.py <dagcount>")
        print("     <dagcount> can be an integer value")

    except ValueError:
        print("ERROR: Please enter a integer value for the DagCount, Current Value entered is " + sys.argv[1].lower().strip())

    except Exception as e:
        print("Got an Exception while genrating Dags, Exception: " + str(e))

