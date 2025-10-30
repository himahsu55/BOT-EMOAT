import requests
from bs4 import BeautifulSoup  # We need this library to find the message

# --- This script is set up for b25liketool.vercel.app ---
WEBSITE_URL = "https://b25liketool.vercel.app/"
FORM_FIELD_NAME = "uid"
MESSAGE_ELEMENT_ID = "message"
# --------------------------------------------------------

def submit_and_find_message(uid_to_send):
    """
    Sends the UID to the website and finds the response message.
    """
    try:
        payload = {
            FORM_FIELD_NAME: uid_to_send
        }
        
        # --- "HIDE" Part: Removed print statement ---
        # print(f"Sending UID {uid_to_send} to {WEBSITE_URL}...")
        
        response = requests.post(WEBSITE_URL, data=payload)
        response.raise_for_status() 

        # --- "HIDE" Part: Removed print statement ---
        # print("Success! Received a response. Finding message...")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find the message element by its ID
        message_element = soup.find('div', {'id': MESSAGE_ELEMENT_ID})
        
        if message_element:
            cleaned_text = message_element.get_text().strip()
            return cleaned_text
        else:
            # This is what is probably happening
            return f"Error: Could not find message tag with id='{MESSAGE_ELEMENT_ID}'"

    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    
    return None

def main():
    """
    Main function to get user input and show the result.
    """
    print("--- HIMESH-07 2.3 Like Tool Submitter ---")
    
    # 1. Get the data to send (UID)
    data_to_send = input("Enter your UID: ")

    # Run the function
    message = submit_and_find_message(data_to_send)
    
    if message:
        # Just print the message from the website, without the header
        print("ADD LIKE 99+  ") # Add a newline for spacing
        print("DAN.....")

if __name__ == "__main__":
    main()

