# Google Photos Takeout Organizer

This is a python script that formats media file names into a referenceable date format (Date/Time taken), making it easy to review your own media in your native file explorer.

`e.g WA00135.HEIC can be converted to 2022-06-21_082259_WA00135.HEIC`

The problem with Google Takeout is that the `Date Modified` will not be date of photo creation, but instead date of unzipping the compressed photo dump. This makes it difficult to sort by photo-taken date.

Since each media file typically comes paired with a JSON metadata file for that media, we can use it to rename the target media file and update the JSON metadata file accordingly.


### New File Format

Files will be reformatted to:

`YYYY-MM-DD_hhmmss_originalFileName.extension`

### Usage

| Step | Description |
| ----------- | ----------- |
| 1 | Download python script `file-rename.py` |
| 2 | Copy and paste script into destination folder |
| 3 | Open terminal in destination folder |
| 4 | Run `python file-rename.py` |
