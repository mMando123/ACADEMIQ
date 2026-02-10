# ACADEMIQ - Professional Academic Services Platform

A modern, responsive Django website for ACADEMIQ - a premium academic services platform providing thesis preparation, research paper reviewing, statistical analysis, scientific translation, and academic formatting.

![ACADEMIQ Logo](static/images/logo.jpeg)

## Features

### Design & UI
- **Modern SaaS Landing Page**: Clean, professional design with glassmorphism cards
- **Smooth Animations**: AOS.js and GSAP-powered scroll animations
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **Dark Mode**: Toggle between light and dark themes
- **Loading Screen**: Animated loading screen with progress bar
- **Scroll Progress Bar**: Visual indicator of scroll position

### Pages
1. **Home**: Hero section, services cards, why choose us, process steps, testimonials, CTA
2. **About Us**: Company story, mission/vision, core values, team section
3. **Services**: Detailed service descriptions for all 5 academic services
4. **Order Now**: Form with file upload for service requests
5. **Contact**: Contact form with FAQ accordion
6. **Privacy Policy**: Comprehensive privacy policy page
7. **Success Page**: Animated confirmation with confetti effect
8. **404 Page**: Custom error page with helpful links

### Technical Features
- **Django 4+**: Modern Django framework with best practices
- **SQLite Database**: Easy deployment configuration
- **Django Forms**: Contact and Order forms with validation
- **Admin Panel**: Full CRUD for Contact, Order, Testimonial, and Service models
- **Email Notifications**: Form submissions trigger email notifications
- **SEO Optimized**: Meta tags, descriptions, and structured data
- **Static Files**: Properly configured for production deployment

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Tailwind CSS (via CDN)
- **Animations**: AOS.js, GSAP
- **Icons**: Font Awesome 6
- **Fonts**: Inter, Playfair Display (Google Fonts)
- **Database**: SQLite (production-ready)
- **Deployment**: PythonAnywhere compatible

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Local Development

1. **Clone or download the project**:
```bash
cd academiq
```

2. **Create a virtual environment**:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run migrations**:
```bash
python manage.py migrate
```

5. **Create a superuser** (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. **Run the development server**:
```bash
python manage.py runserver
```

7. **Access the website**:
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

### PythonAnywhere Deployment

1. **Upload files to PythonAnywhere**:
   - Upload the entire `academiq` folder to your PythonAnywhere account
   - Or use Git to clone the repository

2. **Create a virtual environment**:
```bash
mkvirtualenv --python=/usr/bin/python3.10 academiq
pip install -r requirements.txt
```

3. **Configure Web App**:
   - Go to the Web tab on PythonAnywhere
   - Create a new web app with Manual Configuration
   - Select Python 3.10
   
4. **Set WSGI file**:
   - Edit the WSGI configuration file
   - Replace with:
```python
import sys
path = '/home/yourusername/academiq'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'academiq.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. **Set environment variables**:
   - In the Web tab, set these environment variables:
     - `DJANGO_SECRET_KEY`: Generate a secure secret key
     - `DJANGO_DEBUG`: False (for production)
     - `DJANGO_ALLOWED_HOSTS`: yourusername.pythonanywhere.com

6. **Run migrations**:
```bash
cd ~/academiq
python manage.py migrate
```

7. **Collect static files**:
```bash
python manage.py collectstatic
```

8. **Reload the web app**

## Project Structure

```
academiq/
├── academiq/               # Project settings
│   ├── __init__.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL configuration
│   └── wsgi.py            # WSGI application
├── core/                  # Main application
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Contact and Order forms
│   ├── models.py          # Database models
│   ├── urls.py            # App URL patterns
│   └── views.py           # View functions
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Home page
│   ├── about.html         # About page
│   ├── services.html      # Services page
│   ├── contact.html       # Contact page
│   ├── order.html         # Order form page
│   ├── privacy.html       # Privacy policy
│   ├── success.html       # Success confirmation
│   └── 404.html           # Custom 404 page
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Custom CSS
│   ├── js/
│   │   └── main.js        # Custom JavaScript
│   └── images/
│       ├── logo.jpeg      # ACADEMIQ logo
│       └── background.jpeg # Hero background
├── media/                 # User uploads (created automatically)
├── db.sqlite3             # Database file
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Environment Variables

For production deployment, set these environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key (required for production) | Change in production |
| `DJANGO_DEBUG` | Debug mode (True/False) | True |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | localhost,127.0.0.1 |
| `ADMIN_EMAIL` | Email for admin notifications | admin@academiq.com |
| `EMAIL_USER` | SMTP username (optional) | - |
| `EMAIL_PASSWORD` | SMTP password (optional) | - |

## Admin Panel

Access the admin panel at `/admin/` with your superuser credentials.

### Manageable Content:
- **Contact Messages**: View and manage contact form submissions
- **Order Requests**: Track and update order status
- **Testimonials**: Add/edit customer testimonials
- **Services**: Manage service listings

## Customization

### Colors
Edit the Tailwind config in `base.html` to change the color scheme:
```javascript
colors: {
    'academiq-navy': '#1e3a5f',
    'academiq-gold': '#c9a227',
    // ...
}
```

### Content
Update text content directly in the HTML templates. All templates are well-organized with clear section comments.

### Images
Replace images in `static/images/` with your own assets. Keep the same filenames or update references in templates.

## Features for Users

### Students & Researchers Can:
1. Browse academic services offered
2. Submit contact inquiries
3. Place service orders with file uploads
4. View company information and team
5. Read privacy policy

### Admin Can:
1. View all contact messages
2. Manage order requests and update status
3. Add/edit testimonials
4. Update service descriptions
5. Export data

## Security Features

- CSRF protection on all forms
- XSS protection headers
- Secure cookie settings
- File upload validation
- Input sanitization
- Clickjacking protection

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+
- Opera 67+

## License

This project is proprietary software created for ACADEMIQ.

## Support

For support or inquiries, please contact:
- Email: info@academiq.com
- Website: https://www.academiq.com

---

**Built with ❤️ by ACADEMIQ Team**
# ACADEMIQ
