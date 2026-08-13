import streamlit as st

st.set_page_config(
    page_title="About · Nth Term of a Sequence",
    page_icon="📖",
    layout="centered",
)


st.title("About")

st.write(
    "Nth Term of a Sequence is a simple tool for identifying common "
    "types of sequences and calculating their nth-term formulas."
)


st.header("Background")

st.write(
    "This project was originally inspired by sequence patterns covered "
    "in Grade 9 mathematics. While learning how linear, quadratic, cubic, "
    "and exponential sequences could be identified and represented using "
    "nth-term formulas, I became interested in whether the process could "
    "be automated with code."
)

st.write(
    "The original version of the project was built as a small desktop "
    "application using CustomTkinter. This version is a complete rewrite "
    "with a focus on cleaner Python architecture, exact mathematical "
    "calculations, automated testing, and a simple web interface built "
    "with Streamlit."
)


st.header("Supported Sequence Types")

st.markdown(
    """
    The calculator currently supports four types of sequences:

    - **Linear:**
      $$U_n = an + b$$

    - **Quadratic:**
      $$U_n = an^2 + bn + c$$

    - **Cubic:**
      $$U_n = an^3 + bn^2 + cn + d$$

    - **Exponential:**
      $$U_n = ar^{n-1}$$
    """
)


st.header("How It Works")

st.write(
    "Enter the terms of a sequence, and the calculator analyzes the "
    "differences between consecutive terms or their common ratio to "
    "determine whether the sequence matches one of the supported types. "
    "It then calculates the coefficients of the corresponding "
    "nth-term formula."
)


st.header("Limitations")

st.write(
    "The calculator only recognizes linear, quadratic, cubic, and "
    "exponential sequences. A sequence that does not match one of these "
    "patterns may be reported as unsupported, even if another mathematical "
    "rule could describe it."
)


st.header("Technology")

st.write(
    "Built with Python and Streamlit."
)


st.header("Credits")

st.write(
    "Created by Devin Lin as a personal programming and mathematics project."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "https://github.com/devinlin89/nth-term-of-a-sequence",
        label="Source Code",
        icon=":material/code:",
        use_container_width=True,
    )

with col2:
    st.page_link(
        "https://github.com/devinlin89",
        label="GitHub Profile",
        icon=":material/person:",
        use_container_width=True,
    )

with col3:
    st.page_link(
        "https://github.com/devinlin89/nth-term-of-a-sequence/issues",
        label="Report an Issue",
        icon=":material/bug_report:",
        use_container_width=True,
    )