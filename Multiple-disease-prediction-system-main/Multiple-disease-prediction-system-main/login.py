import streamlit as st

def login():
    # Check if the user is already logged in
    
        
    if 'is_logged_in' in st.session_state and st.session_state.is_logged_in:
        return True
    
    background_image_style = """
        <style>
        .stApp {
            background-image: url('https://i.imgur.com/Alp3jnX.jpg');
            background-size: cover;
        }
        
        </style>
        """
    st.markdown(background_image_style, unsafe_allow_html=True)
    
    
    st.markdown('<h1 style="font-size:4vw; font-family:Times New Roman ; text-align: center; ">MEDSCAN</h1>',unsafe_allow_html=True)
    st.markdown('<h4 style=" font-size:1.9vw; text-align: center; font-family:Times New Roman">Login</h4>', unsafe_allow_html=True)

    with st.container() as login_container:
        # Input fields for patient details
        name = st.text_input("Name", key="name")
        age = st.number_input("Age", min_value=0, step=1, key="age")
        sex = st.selectbox("Sex", ["Male", "Female", "Other"], key="sex")
        mobile_number = st.text_input("Mobile Number", max_chars=10, key="mobile_number")
        email = st.text_input("Email", key="email")
        
        # Login button
        if st.button("Login"):
            # Validate input fields (add your own validation logic)
            if name and age and sex and mobile_number and email:
                # Successful login message
                st.success("Login Successful!")
                # Update session state
                st.session_state.is_logged_in = True
                return True
            else:
                # Display error message if any field is empty
                st.error("Please fill in all the details.")

    return False

def logout():
    st.session_state.is_logged_in = False
    st.experimental_rerun()
