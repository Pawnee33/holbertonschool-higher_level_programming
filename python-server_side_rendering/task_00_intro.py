#!/usr/bin/python3
import os


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise TypeError("template must be an string")
    if not template:
        raise ValueError("template is required")

    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list of dictionaries")
    if not attendees:
        raise ValueError("attendees is required")

    for index, attendee in enumerate(attendees, start= 1):
        result = template
        for key in ['name', 'event_title', 'event_data', 'event_location']:
            if value is None:
                value = "N/A"
            result = result.replace(f'{{{key}}}, str(value)')

