# In Python Creating a function named ds with parameters roll_no and name
def ds(roll_no,name):
    print("The roll number is : ",roll_no)
    print("The name is : ",name)
ds(94,"Hassan")
"""
Output of Creating a function named ds with parameters roll_no and name:
The roll number is :  94
The name is :  Hassan
"""
# In Python Adding those parameters in the following data structures:list, tuple, sets and dictionaries
def ds1():
    ls=[1,2,3,4,5]
    print("The list id : ",ls)
    tup=(1,2,3,4,5)
    print("The tuple is : ",tup)
    st={1,2,3,4}
    print("The set is : ",st)
    d={
        "key1":"value1",
        "key2":"value2"
    }
    print("The dictionary is : ",d)
ds1()
"""
Output of Adding those parameters in the following data structures: list, tuple, sets and dictionaries:
The list id :  [1, 2, 3, 4, 5]
The tuple is :  (1, 2, 3, 4, 5)
The set is :  {1, 2, 3, 4}
The dictionary is :  {'key1': 'value1', 'key2': 'value2'}
"""
# In Python After adding values change the values during runtime
def run_time_change( y, *object_list ):
    x=sum( object_list )
    return x+y
eg1=run_time_change(y= 5 )
eg2=run_time_change(y= 6 )
print(eg1)
print(eg2)
"""
Output of After adding values change the values during runtime:
5
6
"""
# In Python Delete these data structures
del ds1
print("We successfully delete the data structure.")
"""
Output of Delete these data structures:
We successfully delete the data structure.
"""
"""
Output of entire program:
The roll number is :  94
The name is :  Hassan
The list id :  [1, 2, 3, 4, 5]
The tuple is :  (1, 2, 3, 4, 5)
The set is :  {1, 2, 3, 4}
The dictionary is :  {'key1': 'value1', 'key2': 'value2'}
5
6
We successfully delete the data structure.
"""