import streamlit as st

#手動初始化(程式只執行一次為初始化) 手動建立counter_key, 並設定初始值為0
if "counter" not in st.session_state:
    st.session_state.counter = 1
    #st.session_state["counter"] = 1

def increment_counter(*args):
    st.session_state.counter += args[0]
    st.session_state.counter -= args[1]

st.header(f"這頁網頁已經執行 {st.session_state.counter} 次")
st.button("再執行一次", key = 'reset', help = "按下要加1", on_click=increment_counter, args=(5,3))#自動建立reset_key, 並設定初始值為False

