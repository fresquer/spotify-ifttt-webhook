# Webhook for Recording Saved Albums into Google Sheets

This project implements a webhook using Flask to record saved albums into a Google Sheets spreadsheet. It captures data from IFTTT webhook triggers, specifically when an album is saved, and logs this information into the specified Google Sheets document.

## Setup

### Prerequisites

- Installed Python 3.x
- Google API credentials and a valid `credentials.json` file
- Access to Google Sheets and Google Drive for the account associated with the credentials

### Configuration Steps

1. Clone or download this repository.

2. Install necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Define the required environment variables:

   - `SHEET_ID`: ID of the Google Sheets spreadsheet.
   - `SHEET_NAME`: Name of the sheet within the spreadsheet to store the data.

4. Run the application:
   ```bash
   python app.py
   ```

## Usage

Once the application is up and running, send a POST request to the `/webhook/album-listened` endpoint with the following data in JSON format:

```json
{
  "ArtistName": "Artist Name",
  "AlbumName": "Album Name",
  "AlbumCoverURL": "Album Cover URL",
  "SavedAt": "Date and Time of Saving (format: 'Month day, year at Hour:MinuteAM/PM')"
}
```
