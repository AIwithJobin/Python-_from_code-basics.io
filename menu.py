Indian=["samosa",'idali','sambar','tali']
chineese=['noodles','raman','fried rice']
italian=['pizza','pasta','risotto']

dish=input("Enter the dish")
if dish in Indian :
    print("The dish is Indian ")
elif dish in chineese:
    print("the dish is chineese")
elif dish in italian:
    print("the dish is italian")
else:
    print("wrong choice")