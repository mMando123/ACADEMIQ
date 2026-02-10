from django.core.management.base import BaseCommand
from core.models import Service, Testimonial
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed the database with sample premium academic data'

    def handle(self, *args, **kwargs):
        # Clear existing
        # Service.objects.all().delete()
        # Testimonial.objects.all().delete()

        # 1. Seed Services
        services_data = [
            {
                'title': "Master's & PhD Thesis Preparation",
                'short_description': "Comprehensive guidance for high-impact postgraduate research.",
                'description': "Full support for thesis chapters, methodology, and literature reviews.",
                'icon': "fas fa-pen-nib",
                'order': 1
            },
            {
                'title': "Statistical Analysis",
                'short_description': "Advanced data interpretation using SPSS, R, and Python.",
                'description': "Professional statistical modeling and data visualization for scholars.",
                'icon': "fas fa-chart-pie",
                'order': 2
            },
            {
                'title': "Scientific Translation",
                'short_description': "Precise academic translation preserving technical nuances.",
                'description': "Expert translation services for research papers and textbooks.",
                'icon': "fas fa-language",
                'order': 3
            },
            {
                'title': "Academic Formatting",
                'short_description': "Perfect compliance with APA, MLA, Chicago, and Harvard.",
                'description': "Ensuring your manuscript meets all stylistic requirements of your institution.",
                'icon': "fas fa-align-left",
                'order': 4
            }
        ]

        for s in services_data:
            Service.objects.get_or_create(
                slug=slugify(s['title']),
                defaults={
                    'title': s['title'],
                    'short_description': s['short_description'],
                    'description': s['description'],
                    'icon': s['icon'],
                    'display_order': s['order'],
                    'is_active': True
                }
            )

        # 2. Seed Testimonials
        testimonials_data = [
            {
                'name': "Dr. Emily Roberts",
                'title': "Assistant Professor",
                'institution': "Stanford University",
                'content': "ACADEMIQ provided exceptional support for my complex data analysis. Highly recommended!",
                'rating': 5
            },
            {
                'name': "Ahmed Al-Farsi",
                'title': "PhD Candidate",
                'institution': "Oxford University",
                'content': "The thesis preparation service was life-changing. I passed my viva with minor corrections.",
                'rating': 5
            },
            {
                'name': "Maria Garcia",
                'title': "Senior Researcher",
                'institution': "MIT",
                'content': "Professional, confidential, and incredibly precise translation work.",
                'rating': 5
            }
        ]

        for t in testimonials_data:
            Testimonial.objects.get_or_create(
                name=t['name'],
                defaults={
                    'title': t['title'],
                    'institution': t['institution'],
                    'content': t['content'],
                    'rating': t['rating'],
                    'is_active': True
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded ACADEMIQ sample data'))
