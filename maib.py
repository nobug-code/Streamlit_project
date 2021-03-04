import streamlit as st
import pandas as pd
import numpy as np

# 제목 정하기
st.title("Title_nk")
st.header("Header_nk")
st.subheader("subheader_nk")

st.write("write nk")


# 캐시
# 특정 버튼을 눌렀을때 데이터를 불러 오고 싶을때
# 아래 코드를 이용하면 캐싱을 진행

'''
1. 함수 이름확인
2. 함수를 구성하는 코드 확인
3. 삼수 호출시 사용한 매개변수 

위 3개를 학인하여 로컬에 저장하고 다시 호출시 캐싱을 사용할 수 있으면 그대로 사용함

'''
@st.cache
def load_data():
    pass

# 버튼 만들기
if st.button("click button"):
    st.write("Data loading")

checkbox_btn = st.checkbox("Checkbox button")

if checkbox_btn:
    st.write("hhhhh")

# 라디오 버튼 만들기
select_item = st.radio("Raido part ", ("A", "B", "C"))

if select_item == "A":
    st.write("A")
else:
    st.write("KKKK")


# 선택박스 만들기
option = st.selectbox("Pleaset select selct boc", ("kkk", "dddd", "hhhh"))

st.write("YOu select", option)

# 다중 선택 박스 만들기
multi_select = st.multiselect("pleact selct mulit", ['a','b','c','d'])
st.write("you selected", multi_select)

# 슬라이더 만들기

values = st.slider("selct a range of values", 0.0, 100, (25.0, 75.0))
st.write("values", values)