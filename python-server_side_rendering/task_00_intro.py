#!/usr/bin/python3
import os


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start= 1):
        if not isinstance(attendee, dict):
            print("Error: each attendee must be a dictionary")
            return

        result = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            result = result.replace(f'{{{key}}}', str(value))

        filename = f"output_{index}.txt"

        with open(filename, "w") as f:
            f.write(result)
