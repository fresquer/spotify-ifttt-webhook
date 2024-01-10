from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(__name__)

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS_FILE = 'credentials.json'

creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

SHEET_ID = os.environ.get('SHEET_ID')
SHEET_NAME = os.environ.get('SHEET_NAME')

def format_date(date):
    date_object = datetime.strptime(date, "%B %d, %Y at %I:%M%p")
    formatted_date = date_object.strftime("%d/%m/%Y")
    return formatted_date

@app.route('/webhook/album-listened', methods=['POST'])
def webhook():
    content = request.json 
    print(content)
    worksheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

    artist = content.get('ArtistName')
    album = content.get('AlbumName')
    cover = '=IMAGE("{}"; 1)'.format(content.get('AlbumCoverURL'))
    listen_date = '=DATEVALUE("{}")'.format(format_date(content.get('SavedAt')))

    row = [
        artist,
        album,
        cover,
        listen_date
    ] 

    worksheet.append_row(row, 'USER_ENTERED')
    
    return jsonify(row), 200

if __name__ == '__main__':
    app.run(debug=False)
