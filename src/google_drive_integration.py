from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

class GoogleDriveUploader:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def authenticate_google_drive(self):
        try:
            gauth = GoogleAuth()
            gauth.LocalWebserverAuth()
            drive = GoogleDrive(gauth)
            return drive
        except Exception as e:
            print(f"Authentication failed: {str(e)}")
            return None

    def upload_to_google_drive(self, file_paths):
        try:
            drive = self.authenticate_google_drive()
            if drive is not None:
                for file_path in file_paths:
                    file = drive.CreateFile({'title': os.path.basename(file_path)})
                    file.Upload()
                print("Files uploaded to Google Drive successfully.")
        except Exception as e:
            print(f"An error occurred during file upload: {str(e)}")

if __name__ == "__main__":
    google_drive_uploader = GoogleDriveUploader("output")
    google_drive_uploader.upload_to_google_drive(["output/en_to_all_translations.jsonl"])
