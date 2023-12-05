<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🚀 Introduction

This repository contains a versatile Bing image-scraping tool adapted from [this original project](https://github.com/hardikvasa/google-images-download). The Ultralytics team has enhanced it for improved functionality.

# 📋 Requirements

To use this image scraper, you need Python 3.8 or later. Ensure all dependencies listed in [requirements.txt](https://github.com/ultralytics/google-images-download/blob/master/requirements.txt) are installed. `selenium` is one such required package. To install all necessary packages, execute the following command:

```bash
$ pip install -r requirements.txt
```

# 💾 Installation

Clone the repository and install the required Python packages with these commands:

```bash
$ git clone https://github.com/ultralytics/google-images-download
$ cd google-images-download
$ pip install -r requirements.txt
```

# 🏃‍♂️ How to Run the Scraper

To get started with the image scraper, please follow these steps:

1. Make sure you have Google Chrome installed. If not, download it here: https://www.google.com/chrome/

2. You need a compatible version of Chromedriver. Download it here: https://chromedriver.chromium.org/

3. Time to run the scraper! You can download up to `--limit` number of images. Use the `--url` flag if you have a specific webpage or the `--search` flag for terms you wish to query. The images will be saved in the `./images` directory. 

Download images from a URL:

```bash
$ python3 bing_scraper.py --url 'https://www.bing.com/images/search?q=flowers' --limit 10 --download --chromedriver /path/to/your/chromedriver
```

or using search terms:

```bash
$ python3 bing_scraper.py --search 'honeybees on flowers' --limit 10 --download --chromedriver /path/to/your/chromedriver

# You will see output similar to the following, which indicates the progress of the download.
```

Please note: Images that cause errors during download may be automatically skipped to ensure a smooth scraping process.

<!-- Example image -->
<img src="https://user-images.githubusercontent.com/26833433/75287228-dcf2ca80-57ce-11ea-9557-cc13abaff453.jpg" width="">

# 📜 Citing

If our image scraper contributes to your projects or research, we would appreciate citations to the following [source](https://github.com/hardikvasa/google-images-download).

# 🤝 Contributing

Your contributions make the open-source community a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. Check out our [Contributing Guide](https://docs.ultralytics.com/help/contributing) for more information on how to get started, and don't forget to fill out the [Ultralytics Survey](https://ultralytics.com/survey) to provide feedback on your experience. A huge **thanks** goes out to all our contributors!

<!-- SVG image showing contributors -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

# ⚖️ License

Ultralytics is pleased to offer dual license options tailored to fit developer needs:

- **AGPL-3.0 License**: This ISI-approved license is well-suited for developers who are studying, experimenting, or collaborating on open-source projects. For more details, see the full [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) document.
- **Enterprise License**: Those looking to incorporate Ultralytics software within their commercial products are invited to consider this license, which allows for the integration of our solutions into commercial offerings without the standard obligations of the AGPL-3.0. For such applications, please inquire through [Ultralytics Licensing](https://ultralytics.com/license).

# ✉️ Contact

Got suggestions, bug reports, or feature requests? We're all ears! Drop by our [GitHub Issues](https://github.com/ultralytics/google-images-download/issues) page to let us know. And join our vibrant [Discord](https://ultralytics.com/discord) community for engaging discussions!

<br>
<div align="center">
  <!-- Social Icons Section -->
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <!-- Additional spacing between icons -->
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <!-- ... repeating the pattern for each social media link -->
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
