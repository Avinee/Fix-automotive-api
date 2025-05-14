# Fix Automotive API

This is a basic Flask API to handle:
- User login
- Appointment booking
- File uploads (e.g., diagnostics)

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the API:
```
python app.py
```

3. Use tools like Postman or curl to test:
- POST /auth/login
- POST /appointments
- POST /upload (form-data)

## Deployment

You can deploy this easily on:
- Render (https://render.com)
- Railway (https://railway.app)
- Vercel (with Python adapter)
