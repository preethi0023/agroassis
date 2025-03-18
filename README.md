# Agro Assis - Agricultural Assistant

An AI-powered agricultural assistant for crop management and disease detection.

## Features
- Irrigation recommendations based on climate and soil conditions
- Plant disease detection using AI analysis
- Expert connection platform

## Installation

1. First, make sure you have Python installed on your computer.

2. Create a new folder and save all the project files there:
   - app.py
   - utils/openai_helper.py
   - utils/data_helper.py
   - data/mock_data.py
   - .streamlit/config.toml

3. Install required packages:
```bash
pip install streamlit openai pillow pandas numpy
```

4. Set up your OpenAI API key:
   - Get your API key from OpenAI (https://platform.openai.com/api-keys)
   - Set it as an environment variable named `OPENAI_API_KEY`

5. Run the application:
```bash
streamlit run app.py
```

6. Open your web browser and go to: http://localhost:5000

## Usage

1. **Irrigation Advisor**
   - Select your soil type
   - Enter temperature and humidity
   - Input recent rainfall data
   - Get personalized irrigation recommendations

2. **Disease Detection**
   - Upload a photo of your plant
   - Get AI-powered disease analysis
   - Receive treatment recommendations

3. **Expert Connect**
   - Browse agricultural experts
   - Send messages to experts
   - Get professional advice

## Support
If you need help, please use the contact form in the Expert Connect section.
