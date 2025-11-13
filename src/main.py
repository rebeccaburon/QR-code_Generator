import streamlit as st


def main():

    st.set_page_config(
    page_title="CERoS QR Generator",
    layout="wide",
)

st.switch_page("pages/choose_batch_view.py")


if __name__ == "__main__":
    main()
