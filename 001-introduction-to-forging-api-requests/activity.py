"""
To check if your implementation is correct run test.py

*NOTE: Don't change the method names, as that's what's used in the tester.
        but, feel free to add anything else to test and debug your code.
"""

def extract_feed():
    """
        Return an array of all the post objects on the feed page.
    """
def extract_feed():

    """
        Return an array of all the post objects on the feed page.
    """
    posts = []
    page = 0 
    while True:
       r = requests.get(f'https://upgraded-capybara-r9g7954r9g6c5w77-8080.app.github.dev/feed/{page}')
       page +=1 
       new_page_posts = r.json()["posts"]
    
       if len(new_page_posts) == 0: 
          break

       posts.extend(new_page_posts)

    
    return posts
    

def extract_emails():
    """
        Return an array of all the emails on the discover page.
    """
    email =[]
    page = 0
    while True: 
        r= requests.get(f'https://upgraded-capybara-r9g7954r9g6c5w77-8080.app.github.dev/discover/profiles/{page}')
        page += 1
        new_profiles = r.json()["profiles"]

        if len(new_profiles) == 0: 
            break 

        for profile in new_profiles: 
            email.append(profile["email"])



    return email

    

def username_exists(username):
    """
        username - The username to check if exists,  without @ (ex: username="davidteather")
        This function will return True if the provided username already exists, and false if it doesn't
    """
username = "jennifer62"
    r = requests.get(f'https://upgraded-capybara-r9g7954r9g6c5w77-8080.app.github.dev/profile/{username}/feed/0')
    resp = r.json()
    if resp.get("error","") == ('"USER_DOES_NOT_EXIST"'):
        return False 
    return True
   
    return False

if __name__ == "__main__":
    # Optional: You can call your methods here if you want to test them without running the tester
    # print(extract_feed())
    pass
