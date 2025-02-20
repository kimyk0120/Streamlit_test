

import streamlit as st

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader 22')

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ')

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write('hello')

with tab2:
    # tab B를 누르면 표시될 내용
    st.write('hi')

#st.sidebar는

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')
# 사이드바에 체크박스, 버튼등 추가할 수 있습니다!

print('test')