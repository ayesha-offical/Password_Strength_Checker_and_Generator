import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""## Welcome to the eltimate Password Strength Checker!👋
Secure your account with a strong password! Use a mix of uppercase, lowercase, numbers, and symbols. 
             Avoid common words and patterns. ***Test your password strength now!🔐***
 """)

password = st.text_input("Enter your password",type="password")

feedback =[]
score = 0

# Check password length
if password:

    if len(password) >= 8:
       score += 1
    else:
       feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]',password):
       score += 1
    else:
       feedback.append("❌ Password contains both uppercase and lowercase letters.")
    if re.search(r'[0-9]', password):
        score += 1
    else:
       feedback.append("❌Password contains both numbers.")


    if re.search(r'[!@#$%*&]', password):
        score += 1
    else:
       feedback.append("❌Password contains at least one special character.(!@#$%*&)")
    if score == 4:
       feedback.append("✅Password is strong!🎉Now Genrate your Password✨")
    elif score == 3:
       feedback.append("✅Password is moderate!👍. It will never fail but it could more stronger.")   
    elif score == 2:
       feedback.append("❌Password is weak!😢. It will never fail but it could more")  

    if feedback:
     st.markdown("## Improves performance ##")    
     for tip in feedback:
        st.write(tip)
else:
   st.info("Please enter a password to check its strength.")

import streamlit as st
import random
import string #provide specific letter which is find in diffrent values of string like uppercase and lowercase etc.

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters # provide uppercase and lowercase letter(a-z,A-Z)

    if use_digits:
        characters += string.digits # provide digits (0-9) if user selected digits

    if use_special_chars:
        characters += string.punctuation # provide special characters (!@#$%^&*()_+) if user selected special characters

    return ''.join(random.choice(characters) for _ in range(length)) # provide random characters from characters and join all characters in a string   
# _ is mean python ko btata k is loop ki koi specific length nh hai 

st.title("Password Generator 🔐")

length = st.slider("Select Password Length📏", min_value=6, max_value=30, value=12) # slider for password length
use_digits = st.checkbox("Use Digits🔢", value=True) # checkbox for digits
use_special_character = st.checkbox("Use Special Character🔣", value=True) # checkbox for special     
if st.button("Generate Password🛠️"):
   password = generate_password(length, use_digits, use_special_character) # generate password

   st.write(f"Generated Password: {password})") # show password

   st.write("-------------------------")

   st.write("Build by ❤️ [Ayesha Faisal] (https://github.com/ayesha-offical)")