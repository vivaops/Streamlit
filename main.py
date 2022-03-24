import streamlit as st

st.title("hello Streamlit")

st.header("header")

st.subheader("subheader")

st.text("textt ttexttttex ttttexttttexttttext tttexttttexttttext  tttexttttexttttexttttexttttexttttexttttexttttexttttexttttexttttexttttexttttexttt")

st.markdown("""
# h1 tag
## h2 tag
:moon: <br>
:sunglasses:
 """, True)

st.latex(r'''
a +ar+ a r^2''')

st.write("Yo", "123", "# new")

