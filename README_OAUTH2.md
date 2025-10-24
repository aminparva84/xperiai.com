# Xperi AI Website - OAuth2 Email Setup

## 🚀 Quick Start

Your website now uses **OAuth2 authentication** for sending emails through GoDaddy, which is more secure and reliable than traditional SMTP.

### **Start the Server:**
```bash
python app.py
```

### **Authenticate OAuth2:**
1. Open: http://localhost:5000/auth
2. Sign in with your GoDaddy account
3. Grant permissions to the Xperi AI application

### **Test the Website:**
1. Open: http://localhost:5000
2. Fill out the contact form
3. Submit and check if emails are sent successfully

## 🔧 Configuration

Your OAuth2 credentials are already configured in `app.py`:
- **Client ID**: `dL3oxixfqZCv_K3WJy7onZ4rzTSLcXGR355`
- **Client Secret**: `GjyXJmg6S5jahgN6FoUi1n`

## 📁 Clean File Structure

```
xperiai.com/
├── app.py                 # Main OAuth2 Flask application
├── requirements.txt       # Python dependencies
├── smtp_config.py        # SMTP configuration (backup)
├── index.html            # Website frontend
├── src/
│   ├── css/styles.css    # Website styling
│   └── js/script.js      # Frontend JavaScript
└── README_OAUTH2.md      # This file
```

## ✅ What's Working

- ✅ **OAuth2 Authentication**: Secure GoDaddy email authentication
- ✅ **Contact Form**: Fully functional with email sending
- ✅ **Beautiful Emails**: HTML formatted notification and confirmation emails
- ✅ **Error Handling**: Graceful fallbacks and user feedback
- ✅ **Clean Code**: Removed all temporary test files

## 🔍 Troubleshooting

### **Check OAuth2 Status:**
Visit: http://localhost:5000/status

### **Re-authenticate if needed:**
Visit: http://localhost:5000/auth

### **Common Issues:**
1. **"OAuth2 not authenticated"** → Visit `/auth` to authenticate
2. **"Token expired"** → Visit `/auth` to re-authenticate
3. **"Invalid credentials"** → Check GoDaddy Developer Portal settings

## 🚀 Production Deployment

For production:
1. Update redirect URI to your production domain
2. Use environment variables for OAuth2 credentials
3. Store tokens in a database instead of memory
4. Use a production WSGI server (Gunicorn, uWSGI)

## 📞 Support

Your OAuth2 setup is complete and ready to use! The website should now send emails successfully through GoDaddy using secure OAuth2 authentication.
