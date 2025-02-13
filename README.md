# OVERVIEW

This is the homepage of the ICS course at Xi'an Jiaotong University, which is available for members of the ICS team at Xi'an Jiaotong University to edit.

# USAGE

## ADD PROFILE

Create a JSON file for your personal information in the following format.

```json
{
    "homepage_url": "https://example.com",
    "name": "your name",
    "email": "your email",
    "office": "your office",
    "intro": "your intro",
}
```

Then compress the JSON file and the profile picture file into a ZIP file according to the following directory structure. If no image is added, a default profile picture will be used.

The name of the ZIP file is the abbreviation of your name (such as jndu).

```
yourname
├── example.json
└── avatar.png (File formats such as JPG, PNG, and JPEG are available.)
```

Submit your ZIP file to `data/profile-ta`. GitHub Actions will automatically parse it and update it on the website.

## GENERATE EVENTS

Use the `make g-events` command to generate the schedule for all courses and store it in `docs/static/events.json`. The specific content can be modified in the Makefile.

## ADD EVENTS

You can use the `make a-events` command to add events and store them in `docs/static/events.json`. The specific usage is as follows.

## MODIFY EVENTS

For the time being, modifications can only be made manually in `docs/static/events.json`.