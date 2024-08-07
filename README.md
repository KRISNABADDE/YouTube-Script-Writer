# YouTube Script Writing Tool

This Streamlit application generates YouTube video scripts based on user-provided topics, video length, and creativity levels. The app uses the Hugging Face API for language models and DuckDuckGo for search results.

## Features

- Generate engaging YouTube video titles.
- Create detailed video scripts using search engine data.
- Customizable creativity levels for script generation.
- Interactive UI for user inputs.

## Setup

### Prerequisites

- Python 3.7+
- Streamlit
- Hugging Face API token
- DuckDuckGo search integration
- `.env` file for environment variables

### Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/KRISNABADDE/YouTube-Script-Writer.git
    cd YouTube-Script-Writer
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

    Create a `.env` file in the project root directory and add your Hugging Face API token:

    ```env
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
    ```

5. **Run the application**

    ```sh
    streamlit run app.py
    ```

## Usage

1. **Provide the topic of the video**: Enter the subject or topic for the video script.
2. **Expected Video Length**: Specify the duration of the video in minutes.
3. **Creativity level**: Use the slider to set the creativity level (0 for low, 1 for high).
4. **Generate Script**: Click on the "Generate Script for me" button to generate the script.

The application will display:
- A generated title for the video.
- The detailed script for the video.
- Search engine results used for script generation.

## File Structure

- `app.py`: The main Streamlit application.
- `utils.py`: Contains the `generate_script` function.
- `requirements.txt`: List of Python packages required.
- `.env`: Environment variables file.
