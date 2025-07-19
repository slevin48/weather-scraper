import os, requests, tempfile, zipfile, io, glob, json, datetime
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
token = os.getenv('GITHUB_TOKEN')

# Download the artifact as a zip file using requests
data = []
for artifact_info in artifacts_info:
# artifact_info = artifacts_info[0]
    artifact = artifact_info["artifact_obj"]
    download_url = artifact.archive_download_url
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    response = requests.get(download_url, headers=headers)
    if response.status_code == 200:
        zip_bytes = response.content
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(io.BytesIO(zip_bytes), 'r') as zip_ref:
                zip_ref.extractall(tmpdir)
                json_files = glob.glob(f"{tmpdir}/**/*.json", recursive=True)
                if json_files:
                    json_file = json_files[0]
                    # print(json_file)
                    with open(json_file, encoding="utf-8") as f:
                        json_data = json.load(f)
                        # print(jason)
                        weather_info = json_data['main']
                        # weather_info.update(json_data['wind'])
                        # weather_info.update(json_data['coord'])
                        # weather_info['city'] = json_data['name']
                        # add current date and time
                        weather_info['time'] = datetime.datetime.fromtimestamp(json_data['dt'])
                        data.append(weather_info)

df = pd.DataFrame(data)
df = df.set_index('time')