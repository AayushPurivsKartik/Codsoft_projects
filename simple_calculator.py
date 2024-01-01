while True:
    try:
        input1=int(input('enter the first number: '))
        input2=int(input('enter the second number: '))
        choice=input('enter the operator:- +,*,%,//,/: ')
        if choice=="+":
            print('the output is: ',input1+input2)
        elif choice=='-':
            print('the output is: ',input1-input2)
        elif choice=='*':
            print('the output is: ',input1*input2)
        elif choice=='%':
            print('the output is: ',input1%input2)
        elif choice=='//':
            print('the output is: ',input1//input2)
        elif choice=='/':
            print('the output is: ',input1/input2)
        else:
            print('please enter the correct operators in the given list')
    except:
        print("please enter the correct input to see the result: ")
    repeat=input("do you want calculate more: ")
    if repeat=="no" or repeat=="No":
        break
print("Thank you")