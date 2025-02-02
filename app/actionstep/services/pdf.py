from datetime import datetime

import weasyprint
from django.template.loader import render_to_string

from core.models import FileUpload, Issue, Tenancy


def _format_datetime(dt):
    return datetime.strftime(dt, "%d %B %Y")


def create_pdf(issue: Issue):
    """
    Returns a PDF file string.
    """
    client = issue.client
    uploads = FileUpload.objects.filter(issue=issue)
    tenancy = (
        Tenancy.objects.select_related("landlord", "agent").filter(client=client).last()
    )

    client_info = [
        {"name": "Client name", "answers": [client.get_full_name()]},
        {"name": "Client email", "answers": [client.email]},
        {
            "name": "Client DOB",
            "answers": [_format_datetime(client.date_of_birth)]
            if client.date_of_birth
            else [],
        },
        {"name": "Client phone", "answers": [client.phone_number]},
        {"name": "Client call times", "answers": [client.call_times]},
        {
            "name": "Client special circumstances",
            "answers": [client.special_circumstances],
        },
    ]
    tenancy_info = [
        {"name": "Tenancy address", "answers": [tenancy.address]},
        {
            "name": "Tenancy started",
            "answers": [_format_datetime(tenancy.started)] if tenancy.started else [],
        },
        {"name": "Client is on lease", "answers": [tenancy.is_on_lease]},
    ]

    people = []
    people_info = []
    if tenancy.agent:
        people.append(["Agent", tenancy.agent])
    if tenancy.landlord:
        people.append(["Landlord", tenancy.landlord])

    for title, person in people:
        if person.full_name:
            people_info.append({"name": f"{title} name", "answers": [person.full_name]})
        if person.email:
            people_info.append({"name": f"{title} email", "answers": [person.email]})
        if person.address:
            people_info.append({"name": f"{title} address", "answers": [person.address]})
        if person.phone_number:
            people_info.append(
                {"name": f"{title} phone number", "answers": [person.phone_number]}
            )

    sub_info = []
    for name, answer in issue.answers.items():
        sub_info.append(
            {
                "name": name.lower().replace("_", " ").capitalize(),
                "answers": answer if type(answer) is list else [answer],
            }
        )

    answers = [
        *client_info,
        *tenancy_info,
        *people_info,
        *sub_info,
    ]
    context = {
        "issue": issue,
        "answers": answers,
        "uploads": uploads,
    }
    pdf_html_str = render_to_string("actionstep/client-intake.html", context=context)
    pdf_bytes = weasyprint.HTML(string=pdf_html_str).write_pdf()
    return pdf_bytes
