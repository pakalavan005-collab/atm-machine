import streamlit as st

# Initialize session state
if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "pin" not in st.session_state:
    st.session_state.pin = 1234

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🏧 ATM Management System")

# Login
if not st.session_state.logged_in:
    user_pin = st.text_input("Enter PIN", type="password")

    if st.button("Login"):
        if user_pin.isdigit() and int(user_pin) == st.session_state.pin:
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid PIN")

# ATM Menu
else:
    st.sidebar.title("ATM Menu")

    option = st.sidebar.radio(
        "Select an Option",
        ["Balance", "Deposit", "Withdraw", "Change PIN", "Logout"]
    )

    if option == "Balance":
        st.subheader("Account Balance")
        st.success(f"Balance Amount: ₹{st.session_state.balance}")

    elif option == "Deposit":
        st.subheader("Deposit Money")
        amount = st.number_input(
            "Enter Deposit Amount",
            min_value=1,
            step=1
        )

        if st.button("Deposit"):
            st.session_state.balance += amount
            st.success(f"₹{amount} deposited successfully!")
            st.info(f"New Balance: ₹{st.session_state.balance}")

    elif option == "Withdraw":
        st.subheader("Withdraw Money")
        amount = st.number_input(
            "Enter Withdraw Amount",
            min_value=1,
            step=1
        )

        if st.button("Withdraw"):
            if amount > st.session_state.balance:
                st.error("Insufficient Balance")
            else:
                st.session_state.balance -= amount
                st.success(f"₹{amount} withdrawn successfully!")
                st.info(f"Remaining Balance: ₹{st.session_state.balance}")

    elif option == "Change PIN":
        st.subheader("Change PIN")

        old_pin = st.text_input("Current PIN", type="password")
        new_pin = st.text_input("New PIN", type="password")
        confirm_pin = st.text_input("Confirm New PIN", type="password")

        if st.button("Update PIN"):
            if (
                old_pin.isdigit()
                and int(old_pin) == st.session_state.pin
            ):
                if new_pin == confirm_pin:
                    if new_pin.isdigit():
                        st.session_state.pin = int(new_pin)
                        st.success("PIN Changed Successfully!")
                    else:
                        st.error("PIN should contain only numbers.")
                else:
                    st.error("New PIN and Confirm PIN do not match.")
            else:
                st.error("Current PIN is incorrect.")

    elif option == "Logout":
        st.session_state.logged_in = False
        st.success("Logged Out Successfully!")
        st.rerun()
