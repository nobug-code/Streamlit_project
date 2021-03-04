import streamlit as st


#텍스트 데이터 입력을 받을 경우
st.text_input("hello")

# 텍스트 데이터를 암호로 사용하고 싶은 경우에는 type='password' ㅊ 구ㅏ
st.text_input("password", type="password")

# 숫자를 입력하고 싶은 경우
st.number_input("nuber")

# 여러줄의 텍스트 데이터를 입력하고 싶은 경우
st.text_area("multi lines")

# 날짜를 입력하고 싶은 경우
st.date_input("date")

# 시간을 입력하고 싶은 경우
st.time_input("time")