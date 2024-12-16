import streamlit as st

st.title("Calculator Vol.1 :sunglasses:")

if "num1" not in st.session_state:
    st.session_state.num1 = None
if "num2" not in st.session_state:
    st.session_state.num2 = None
if "result" not in st.session_state:
    st.session_state.result = None

st.subheader("숫자 선택")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("1", key="btn1"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 1
        elif st.session_state.num2 is None:
            st.session_state.num2 = 1
            
    if st.button("4", key="btn4"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 4
        elif st.session_state.num2 is None:
            st.session_state.num2 = 4

    if st.button("7", key="btn7"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 7
        elif st.session_state.num2 is None:
            st.session_state.num2 = 7

with col2:
    if st.button("2", key="btn2"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 2
        elif st.session_state.num2 is None:
            st.session_state.num2 = 2

    if st.button("5", key="btn5"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 5
        elif st.session_state.num2 is None:
            st.session_state.num2 = 5

    if st.button("8", key="btn8"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 8
        elif st.session_state.num2 is None:
            st.session_state.num2 = 8
            
with col3:
    if st.button("3", key="btn3"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 3
        elif st.session_state.num2 is None:
            st.session_state.num2 = 3

    if st.button("6", key="btn6"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 6
        elif st.session_state.num2 is None:
            st.session_state.num2 = 6

    if st.button("9", key="btn9"):
        if st.session_state.num1 is None:
            st.session_state.num1 = 9
        elif st.session_state.num2 is None:
            st.session_state.num2 = 9
            
num1 = st.write(f"첫 번째 숫자: {st.session_state.num1}")
num2 = st.write(f"두 번째 숫자: {st.session_state.num2}")

if st.button("초기화"):
    st.session_state.num1 = None
    st.session_state.num2 = None
    st.session_state.result = None
    

