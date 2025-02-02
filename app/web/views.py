import random

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import BlogListPage
from .forms import ContactForm


@require_http_methods(["GET"])
def robots_view(request):
    """robots.txt for web crawlers"""
    return render(request, "web/robots.txt", content_type="text/plain")


@require_http_methods(["GET"])
def landing_view(request):
    form = ContactForm()
    return render(
        request, "web/landing.html", {"form": form, "testimonials": TESTIMONIALS}
    )


@require_http_methods(["GET"])
def blog_search_view(request):
    blog_parent = BlogListPage.objects.get(slug="blog")
    context = blog_parent.get_context(request)
    return render(request, "web/htmx/_blog_results.html", context)


@require_http_methods(["POST"])
def landing_contact_form_view(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Contact request submitted")

    return render(request, "web/htmx/_contact_form.html", {"form": form})


@require_http_methods(["GET"])
def team_view(request):
    return render(
        request,
        "web/about/team.html",
        {"members": TEAM_MEMBERS, "advisors": ADVISORS, "board": BOARD},
    )


def shuffle(l):
    l2 = l.copy()
    random.shuffle(l2)
    return l2


BOARD = [
    {
        "image": "web/img/photos/board/dennis.jpeg",
        "name": "Denis Nelthorpe",
        "title": "Board Member",
        "brags": [
            "Denis has worked in the community legal centre sector for over 40 years including as the CEO of West Justice, Consumer Credit Legal Service, Footscray and Wyndham CLCs, and is the Chair of St Kilda Legal Service."
        ],
    },
    {
        "image": "web/img/photos/board/marcia.jpeg",
        "name": "Marcia Pinskier",
        "title": "Board Member",
        "brags": [
            "Marcia (FAICD) is an expert on good governance in the not-for-profit sector. She is a Fellow of the Australian Institute of Company Directors and has chaired numerous not-for-profit boards. She has experience in leadership roles including as a Victorian Multicultural Commissioner, liaison to the Victoria Police Multicultural Advisory Unit and a member of the Victorian Mental Health Reform Council."
        ],
    },
    {
        "image": "web/img/photos/team/tessa.jpeg",
        "name": "Tessa Ramanlal",
        "title": "Board Member & Co-founder",
        "brags": [
            "Tessa previously volunteered as co-founder and Head of User at Anika. Tessa has practiced as a Corporate lawyer / Innovation lawyer at Herbert Smith Freehills and is an Enterprise Partnerships Associate at DoorDash."
        ],
    },
    {
        "image": "web/img/photos/team/michael.jpeg",
        "name": "Michael Choong",
        "title": "Board Member",
        "brags": [
            "Michael previously volunteered as the Head of Strategy at Anika. He is now a Strategy Manager at Seek."
        ],
    },
    {
        "image": "web/img/photos/team/noel.jpeg",
        "name": "Noel Lim",
        "title": "Board Member & CEO",
        "brags": ["Noel is the full-time CEO and co-founder of Anika Legal."],
    },
]


ADVISORS = [
    {
        "image": "web/img/photos/advisors/jane-prior.jpeg",
        "name": "Jane Prior",
        "title": "General Manager at WT Partnership",
        "brags": [
            "Jane has significant leadership experience in higher education and operations across strategy, marketing, IT, HR and finance. She serves as a non-executive director in the not-for-profit sector",
            "Jane has been a mentor to the Anika leadership team since the business idea was created",
        ],
    },
    {
        "image": "web/img/photos/advisors/brendan-lacota.jpeg",
        "name": "Brendan Lacota",
        "title": "Not-for-profit and for-purpose consultant",
        "brags": [
            "Brendan is an emerging leader in designing innovative ways to provide community legal services",
            "Brendan was the Head of Community Programs at Justice Connect and the 2020 President Elect of the Law Institute of Victoria",
        ],
    },
    {
        "image": "web/img/photos/advisors/clyde-fernandez.jpeg",
        "name": "Clyde Fernandez",
        "title": "Regional Vice President, Platform & Revenue Cloud at Salesforce",
        "brags": [
            "Clyde is a career technologist who has spent time working in many sectors in Australia, Asia & the UK",
            "Clyde also likes to share his perspectives on 'The future of the work', 'How to succeed in a constantly growing VUCA world' and 'Why Equity & Ethics matter, now more than ever'",
        ],
    },
]


TEAM_MEMBERS = [
    {
        "image": "web/img/photos/team/noel.jpeg",
        "name": "Noel Lim",
        "title": "Chief Executive Officer",
        "brags": [
            "Noel drives the direction of our organisation and ensures that each portfolio is successfully managed",
            "Noel is the full-time CEO and co-founder of Anika Legal",
        ],
    },
    {
        "image": "web/img/photos/team/cam.jpeg",
        "name": "Cameron Horn",
        "title": "Principal Lawyer",
        "brags": [
            "Cameron is our Principal Lawyer and is responsible for issuing our legal advice",
            "Cameron was previously the Principal Solicitor of Tenants Victoria and a Legal Counsel at Victoria Legal Aid",
        ],
    },
    {
        "image": "web/img/photos/team/lucy.jpeg",
        "name": "Lucy Majstorovic",
        "title": "Head of Partnerships & Philanthropy",
        "brags": [
            "Lucy is our full-time Head of Partnerships & Philanthropy, working with our trusted partners to maximise Anika’s impact.",
        ],
    },
    {
        "image": "web/img/photos/team/dan.jpeg",
        "name": "Dan Poole",
        "title": "Head of Finance",
        "brags": [
            "Dan leads our Finance portfolio, ensuring Anika’s finances are well managed",
            "Dan is also a pro-bono lawyer at Hall & Wilcox and Co-founder of Society Melbourne ",
        ],
    },
    {
        "image": "web/img/photos/team/gwylim.jpeg",
        "name": "Gwilym Temple",
        "title": "Head of Operations",
        "brags": [
            "Gwilym leads our Operations portfolio, which keeps the engine of our legal practice running",
            "Gwilym has experience in workforce management, analysis and process optimisation at Uber",
        ],
    },
    {
        "image": "web/img/photos/team/kate.jpeg",
        "name": "Kate Robinson",
        "title": "Head of User",
        "brags": [
            "Kate leads our User Portfolio, which ensures that Anika’s marketing and services are user-focused",
            "Kate is also a Digital producer at Conversion Digital and has extensive marketing and project management experience",
        ],
    },
    {
        "image": "web/img/photos/team/edward.jpeg",
        "name": "Edward Sinclair",
        "title": "Head of Strategy",
        "brags": [
            "Edward leads our Strategy portfolio, which keeps us focused on success",
            "Edward is a Management Consultant at McKinsey & Company. Before this he worked as a solicitor at Herbert Smith Freehills.",
        ],
    },
    {
        "image": "web/img/photos/team/jess.jpeg",
        "name": "Jess Nashed",
        "title": "Head of Product",
        "brags": [
            "Jess leads our Product portfolio which builds the processes and materials used by our clients and students",
            "Jess is a law graduate at Herbert Smith Freehills",
        ],
    },
    {
        "image": "web/img/photos/team/matt.jpeg",
        "name": "Matthew Segal",
        "title": "Head of Technology",
        "brags": [
            "Matt leads our Technology portfolio and is responsible for our technical infrastructure",
            "Matt is a full-stack software developer with experience in eCommerce, fintech and online media",
        ],
    },
    {
        "image": "web/img/photos/team/george.jpeg",
        "name": "George Hamilton",
        "title": "Head of People & Culture",
        "brags": [
            "George leads our People & Culture portfolio, which supports Anika’s functions to build aligned, effective and engaged teams",
            "George is a Senior Analyst (Strategy) at Coles Group",
        ],
    },
]

TESTIMONIALS = [
    {
        "name": "Gabrielle",
        "testimonial": "After months of getting nowhere with my landlord I was beginning to think I was overreacting to a number of faults in my house, namely heating that didn't work. Contacting Anika to get some advice and legal support was super easy and super fast. I was able to have a chat on the phone to a staff member, voice my concerns and ask questions, which was followed up by timely legal advice. Suffice to say, my heating ended up getting fixed the following week without going to VCAT, and I was able to maintain a relationship with my agent and landlord which was something I was anxious about. It is amazing to have free support for tenants who have very little idea about their rights. Anika has filled a very large gap in the system and I couldn't recommend them enough. Thanks again to the team!",
        "image": "web/img/testimonials/gabrielle.jpg",
    },
    {
        "name": "Hieu",
        "testimonial": "[Anika] was really quick with everything, like the follow-up, and also tried their best to help out. I feel like I at least had someone else on my side who helped me work things out.. If it wasn’t for Anika I don’t think I would have pursued the negotiations on my own. Now [my rent] is actually reduced.",
        "image": "web/img/testimonials/hieu.jpg",
    },
    {
        "name": "Erica",
        "testimonial": "I would give Anika a 10! I didn’t have any issues at all and I thought the service went super well. It was exactly what I needed. Having the law on your side makes you feel way more comfortable with dealing with these things, especially because in the past I have been told that I am just a young renter who doesn’t have any rights. I didn’t realise that as a renter I actually had some power!",
        "image": "web/img/testimonials/erica.jpg",
    },
    {
        "name": "Louise",
        "testimonial": "Anika was exactly the service I needed - I couldn’t have asked for anything better. I was so used to everyone else that I’d dealt with letting me down - agents, landlords, even law firms. Sam (the Anika law student) was just that one solid person I could completely count on when I needed him. The empathy that everyone at Anika showed for our situation was amazing, and with Sam taking over, everything just became so much easier for me.",
        "image": "web/img/testimonials/louise.jpg",
    },
    {
        "name": "Mary",
        "testimonial": "Big thank you to Anika Legal and the team. Without their legal advice I would not have been able to get my repairs done. I am very thankful, the communication and help received was incredible.",
        "image": "web/img/testimonials/mary.jpg",
    },
]
