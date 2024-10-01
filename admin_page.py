import streamlit as st
import os
st.title("어드민 페이지")
# 이 폴더에 있는 png파일 리스트 보여주기
# Get the list of files in the directory
file_list = os.listdir('/Users/gooya/Documents/Coding/maedongei')

# Filter the list to include only PNG files
png_files = [file for file in file_list if file.endswith('.png')]

# Display the list of PNG files
for file in png_files:
    st.write(file)

# Allow the user to delete a file
selected_files = st.multiselect("삭제할 파일", png_files)
if st.button("전체삭제"):
    for file in png_files:
        os.remove(os.path.join('/Users/gooya/Documents/Coding/maedongei', file))
    st.success("모든 파일이 삭제되었습니다!")
if st.button("삭제하기"):
    for file in selected_files:
        os.remove(os.path.join('/Users/gooya/Documents/Coding/maedongei', file))
    st.success("선택한 파일들이 삭제되었습니다!")
