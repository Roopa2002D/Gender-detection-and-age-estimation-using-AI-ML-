import os
import urllib.request
import zipfile

def download_and_extract(url, zip_name="gender_age_models.zip"):
    if not os.path.exists("age_net.caffemodel") or not os.path.exists("gender_net.caffemodel"):
        print("Downloading models...")
        urllib.request.urlretrieve(url, zip_name)
        print("Download complete. Extracting...")
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall()
        print("Extraction complete.")
    else:
        print("Model files already exist.")

# 🔽 Replace with your actual direct download link
model_zip_url = "https://drive.google.com/file/d/1dd0Wo7BFm05XYp8YK3R_yPn7boQ6D9bH/view?usp=drive_link","https://drive.google.com/file/d/18_7v-ibwInox7tHLDLhd_E3GZczrTuAH/view?usp=drive_link"
download_and_extract(model_zip_url)
