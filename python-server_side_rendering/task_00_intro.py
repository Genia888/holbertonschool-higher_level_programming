#!/usr/bin/python3
import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print(f"Invalid template type: expected str, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Invalid attendees type: expected list of dicts, got {type(attendees).__name__}")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        data = {}
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            # Treat None or missing as "N/A"
            if value is None or (isinstance(value, str) and not value.strip()):
                data[key] = "N/A"
            else:
                data[key] = str(value)

        try:
            content = template.format(**data)
        except Exception as e:
            print(f"Error formatting template for attendee #{idx}: {e}")
            continue

        filename = f"output_{idx}.txt"
        # Check if file exists
        if os.path.exists(filename):
            print(f"File '{filename}' already exists, overwriting.")

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file '{filename}': {e}")
            continue

    print(f"Generated {idx} invitation file(s).")
