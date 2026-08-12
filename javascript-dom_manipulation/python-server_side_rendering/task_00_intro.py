cat << 'EOF' > task_00_intro.py
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    and a list of attendee dictionaries.
    """
    # Verify input types
    if not isinstance(template, str):
        print("Invalid input type: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Invalid input type: attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, 'w') as file:
                file.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
EOF
