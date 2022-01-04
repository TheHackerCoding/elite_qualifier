from functions import *
from time import sleep
def main():
    google = google_trends()
    github = github_trends()
    print(f"There's currently {len(google)} Google trends.")
    for x in google:
        print(f"  * {x}")
    sleep(.25)
    print(f"There's currently {len(github)} Github repos using Python that are trending")
    for x in github:
        print(f"  * {x['author']}/{x['name']} | {x['url']}")

if __name__ == '__main__':
    main()
