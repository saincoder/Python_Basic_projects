import requests

# Define your API credentials
api_key = '89e80791dec4c13d91f8'
api_secret = '836e9ebcd3278685f1e0c27e9d2b28ec86757895'
redirect_uri = 'http://localhost/'  # Redirect URI specified in your Dailymotion application settings
username = 'kancain00@gmail.com'
password = 'WtM2LKz!XR3Z9s!'


# Obtain an access token
def get_access_token(api_key, api_secret, redirect_uri, username, password):
    url = 'https://api.dailymotion.com/oauth/token'
    data = {
        'grant_type': 'password',
        'client_id': api_key,
        'client_secret': api_secret,
        'username': username,
        'password': password,
        'scope': 'manage_videos'
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()['access_token']


# Request an upload URL
def get_upload_url(access_token):
    url = 'https://api.dailymotion.com/file/upload'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['upload_url']


# Upload the video file
def upload_video_file(upload_url, video_file_path):
    with open(video_file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        return response.json()['url']


# Create the video object on Dailymotion
def create_video_object(access_token, video_url, title, description):
    url = 'https://api.dailymotion.com/me/videos'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'url': video_url,
        'title': title,
        'description': description
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()


# Main function to execute the script
def main():
    access_token = get_access_token(api_key, api_secret, redirect_uri, username, password)
    upload_url = get_upload_url(access_token)
    video_file_path = r'C:\Users\kanca\PycharmProjects\Python_Basic_projects\video.mp4'
    video_url = upload_video_file(upload_url, video_file_path)
    title = 'Islamic Video'
    description = 'Your Video Description'
    video_info = create_video_object(access_token, video_url, title, description)
    print(f'Video uploaded successfully: {video_info}')


if __name__ == '__main__':
    main()
