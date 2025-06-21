import instaloader

def scrape_instagram_profile(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        print(f"\n Profile: {profile.username}")
        print(f" Full Name: {profile.full_name}")
        print(f" Bio: {profile.biography}")
        print(f" External URL: {profile.external_url}")
        print(f" Followers: {profile.followers}")
        print(f" Following: {profile.followees}")
        print(f" Total Posts: {profile.mediacount}")
        print(f" Is Private: {profile.is_private}")
        print(f" Is Verified: {profile.is_verified}")
    except Exception as e:
        print(f" Error fetching profile: {e}")

if __name__ == "__main__":
    username = input("Enter Instagram username: ").strip()
    scrape_instagram_profile(username)
