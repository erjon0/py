import streamlit as st

def calculator(num1,num2,oparecion):
    if oparecion=="Add":
        result=num1+num2
    elif oparecion=="Sub":
        result=num1-num2
    elif oparecion=="multi":
        result=num1*num2
    elif oparecion=="div":
        try:
            result=num1/num2
        except ZeroDivisionError:
            result="cant do that"
    return result

def main():
    st.title("calculator")

    num1=st.number_input("enter",step=1)

    num2=st.number_input("enter",step=2)

    oparecion=st.radio("select operacion",["add","sub","multi","div"])

    result=calculator(f"result of the {oparecion}    of  {num1}     and  {num2}")

if __name__=="__main__":
    main()


