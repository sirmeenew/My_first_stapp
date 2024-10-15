import streamlit as st

st.title("텍스트 출력")
st.write("")
st.write("# 마크다운 H1 : st.write()")
st.write("### 마크다운 H3 : st.write()")
st.write('')

st.title("제목 : st.title()")
st.header(" 헤더 : st.header()")
st.subheader("서브헤더 : st.subheader()")
st.text("본문 텍스트 : st.text()")
st.write("")

st.markdown("## 마크다운 : st.markdowwn()")
st.markdown('''
            1. ordered item
              - unordered item
              - unordered item
            2. ordered item
            3. ordered item
            ''')
st.divider()

#마크다운
'''# (icon) Magic에 마크다운을 조합
1. ordered item
  - 강조: **unordered item**
  - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

#데이터프레임
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1,2,3], 'B':[4,5,6]})
df #차트출력

import matplotlib.pyplot as plt

x = np.linspace(0,10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)
fig #차트출력

st.sidebar.header("🪧🪧🪧사이드바")
st.sidebar.write('## 사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

#레이아웃 : 컬럼
st.header('## 1번 컬럼')
col_1, col_2, col_3 = st.columns([1,2,1])

with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')
    
with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 id를 변경해야함
col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스',['select 1', 'select 2', 'select 3']) 

#레이아웃 : 탭
st.header('탭 레이아웃')

#탭 인스턴스 생성. 3개의 탭 생성
tab_1, tab_2, tab_3 = st.tabs(['탭AAA', '탭BBB','탭CCC'])
with tab_1:
  st.write('## 탭AAAA')
  st.write('이것은 탭A의 내용입니다.')
    
with tab_2:
  st.write('## 탭BBBB')
  st.write('이것은 탭B의 내용입니다.')
  '''
  ```python
  import pandas as pd
  a=3
  b=4
  '''
  
tab_3.write('## 탭CCCCC')
tab_3.write('이것은 탭C의 내용입니다.')
