import instaloader

def download_photos(username):
    try:
        L = instaloader.Instaloader()

        # Load the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Create a directory to store the photos
        output_folder = f"{username}_photos"
        L.context.log('Creating directory: ' + output_folder)
        
        # Download the photos
        L.download_profile(profile, profile_pic_only=False)

        L.context.log("Download completed.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    insta_username = input("Enter Instagram username: ")
    download_photos(insta_username)
