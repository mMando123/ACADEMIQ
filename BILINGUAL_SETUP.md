# ACADEMIQ Bilingual Setup Instructions (English & Arabic)

## Overview
This Django project is now fully configured for bilingual support (English & Arabic) with RTL layout support.

## What's Been Implemented

### 1. Django i18n Configuration
- ✅ `LocaleMiddleware` added to settings.py
- ✅ `LANGUAGES` setting with English and Arabic
- ✅ `LOCALE_PATHS` configured
- ✅ `USE_I18N = True` enabled
- ✅ i18n context processor added

### 2. URL Configuration
- ✅ `i18n_patterns` for language-prefixed URLs
- ✅ `set_language` view for language switching
- ✅ URLs: `/` (English), `/ar/` (Arabic)

### 3. Models & Forms
- ✅ All models use `gettext_lazy` for field labels
- ✅ All choices translated (Service types, Status, etc.)
- ✅ Form field labels and placeholders translated

### 4. Templates
- ✅ All templates have `{% load i18n %}`
- ✅ All user-facing text wrapped with `{% trans %}`
- ✅ RTL support with `dir="rtl"` attribute
- ✅ Language switcher in navbar (desktop & mobile)
- ✅ Arabic font (Tajawal) loaded conditionally

### 5. RTL Styling
- ✅ `style-rtl.css` with complete RTL overrides
- ✅ Flipped margins, paddings, text alignment
- ✅ Icons flipped for RTL context
- ✅ AOS animations adjusted for RTL

### 6. Translation Files
- ✅ `locale/ar/LC_MESSAGES/django.po` created with 100+ translations
- ✅ Ready for compilation to `.mo` files

## File Structure

```
academiq/
├── academiq/
│   ├── settings.py          # i18n config, LANGUAGES, LOCALE_PATHS
│   └── urls.py              # i18n_patterns, set_language view
├── core/
│   ├── models.py            # All fields use gettext_lazy
│   └── forms.py             # All labels translated
├── templates/               # All templates have {% load i18n %}
│   ├── base.html            # Language switcher, RTL support
│   ├── home.html
│   ├── about.html
│   ├── services.html
│   ├── contact.html
│   ├── order.html
│   ├── privacy.html
│   ├── success.html
│   └── 404.html
├── static/
│   └── css/
│       ├── style.css        # Base styles
│       └── style-rtl.css    # RTL overrides
└── locale/
    └── ar/
        └── LC_MESSAGES/
            └── django.po      # Arabic translations
```

## How to Use

### Switching Languages
1. **Language Switcher**: Click the globe icon in the navbar
2. **Direct URL**:
   - English: `http://localhost:8000/`
   - Arabic: `http://localhost:8000/ar/`

### Adding New Translations

1. **Add trans tags in templates**:
   ```html
   {% trans "Your text here" %}
   ```

2. **Add trans tags in Python code**:
   ```python
   from django.utils.translation import gettext_lazy as _
   
   message = _("Your text here")
   ```

3. **Update translation files**:
   ```bash
   python manage.py makemessages -l ar
   ```

4. **Edit translations** in `locale/ar/LC_MESSAGES/django.po`

5. **Compile translations**:
   ```bash
   python manage.py compilemessages
   ```

## PythonAnywhere Deployment Instructions

### Step 1: Upload Project
Upload the project files to your PythonAnywhere account.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations
```bash
python manage.py migrate
```

### Step 4: Compile Translations (IMPORTANT)
```bash
# On PythonAnywhere Bash console:
python manage.py compilemessages
```

This creates the `.mo` binary files needed for translations to work.

### Step 5: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 6: Configure WSGI
Ensure your WSGI file points to the correct settings:
```python
import sys
path = '/home/yourusername/academiq'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'academiq.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 7: Environment Variables (Optional)
Set these in the Web tab:
- `DJANGO_SECRET_KEY`: Your secure secret key
- `DJANGO_DEBUG`: False (for production)
- `DJANGO_ALLOWED_HOSTS`: yourusername.pythonanywhere.com

### Step 8: Reload Web App
Click the "Reload" button in the Web tab.

## Language-Specific Features

### Arabic (RTL) Layout
When Arabic is selected:
- Page direction changes to RTL
- Arabic font (Tajawal) is loaded
- `style-rtl.css` is included
- Margins/paddings are flipped
- Icons are mirrored where appropriate

### English (LTR) Layout
When English is selected:
- Page direction is LTR
- Inter/Playfair Display fonts loaded
- Only base CSS is used

## SEO Features

- ✅ `hreflang` tags for both languages
- ✅ `lang` attribute on HTML tag
- ✅ Translated meta descriptions
- ✅ Proper URL structure for indexing

## Troubleshooting

### Translations not showing?
1. Ensure `.mo` files are compiled:
   ```bash
   python manage.py compilemessages
   ```

2. Check that `LOCALE_PATHS` is correct in settings.py

3. Restart the Django server

### RTL not working?
1. Check `style-rtl.css` is being loaded (see browser dev tools)
2. Verify `dir="rtl"` attribute on HTML tag
3. Check `LANGUAGE_CODE` is 'ar'

### Language switcher not working?
1. Ensure `set_language` URL is in urls.py
2. Check CSRF token is in the form
3. Verify `next` parameter is set correctly

## Additional Resources

- Django i18n Documentation: https://docs.djangoproject.com/en/4.2/topics/i18n/
- Arabic Typography: https://fonts.google.com/specimen/Tajawal
- RTL Styling Guide: https://rtlstyling.com/

## Summary

Your ACADEMIQ website is now fully bilingual with:
- ✅ 100+ translated strings
- ✅ RTL support for Arabic
- ✅ Working language switcher
- ✅ SEO-optimized multilingual structure
- ✅ Production-ready for PythonAnywhere

The website will automatically detect and apply the correct language based on user selection, with proper RTL layout for Arabic and LTR for English.
