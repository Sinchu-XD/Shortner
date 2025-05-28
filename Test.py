import requests

def shorten_url(long_url, api_key):
    api_endpoint = "https://inshorturl.com/api"
    params = {
        "api": api_key,
        "url": long_url
    }

    try:
        response = requests.get(api_endpoint, params=params)
        data = response.json()

        if data.get("status") == "success":
            print("✅ URL Shortened Successfully!")
            print("Original URL:", long_url)
            print("Shortened URL:", data["shortenedUrl"])
        else:
            print("❌ Failed to shorten URL.")
            print("Reason:", data.get("message", "Unknown error"))

    except Exception as e:
        print("⚠️ Error occurred:", e)

if __name__ == "__main__":
    # 🔁 Replace with your values here
    api_key = "c092dcb46ea7cf7c52357f4321655f5940d65dba"
    long_url = "https://t.me/StreeStuffBot?start=683684af39e6e3cbd2bfa4dd"

    shorten_url(long_url, api_key)
  
