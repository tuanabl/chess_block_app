import streamlit as st

def getChessSquareColor(row: int, column: int) -> str:
	sum_row_colum = row + column
	if (row in range(0, 8)) & (column in range(0, 8)):
		if sum_row_colum % 2 == 0:
			return 'white'
		else:
			return 'black'
	else:
		return ''
    
st.title("First Calculator Apps :smile:")

num_1 = st.number_input("Please enter a number",min_value=0,max_value=7,step=1,key=1)
num_2 = st.number_input("Please enter a number",min_value=0,max_value=7,step=1,key=2)

result = getChessSquareColor(num_1,num_2)

st.write("The result is",result)
