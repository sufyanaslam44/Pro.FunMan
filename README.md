# Pro.FunMan

A simple, elegant web page application with a homepage and periodic table viewer.

## Features

- Clean and modern design
- Responsive layout
- Interactive periodic table
- Easy to deploy on Render.com
- **Python Flask backend**

## Local Development

### Using Python (Recommended)

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

3. Open your browser and visit: `http://localhost:5000`

## Deployment on Render.com

1. Push this code to your GitHub repository
2. Go to [Render.com](https://render.com) and sign in
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository: `https://github.com/sufyanaslam44/Pro.FunMan`
5. Configure the service:
   - **Name**: pro-funman (or any name you prefer)
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"

Your app will be deployed and accessible at: `https://your-app-name.onrender.com`

## Project Structure

```
Pro.FunMan/
├── index.html          # Homepage
├── pt.html            # Periodic table page
├── app.py             # Flask backend server (Python)
├── requirements.txt   # Python dependencies
├── Procfile          # Render.com deployment config
├── runtime.txt       # Python version
└── README.md         # Documentation
```

## Pages

- **Home** (`/`) - Welcome page with navigation
- **Periodic Table** (`/pt.html`) - Interactive periodic table with all 118 elements

## License

MIT
