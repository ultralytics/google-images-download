<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Introduction

Welcome to the Bing Image Scraper, a tool updated and maintained by Ultralytics. This repository provides enhanced code, originally based on the [google-images-download](https://github.com/hardikvasa/google-images-download) project by hardikvasa, specifically adapted for scraping images from Bing. It allows users to efficiently download images for various purposes, such as building datasets for [machine learning](https://www.ultralytics.com/glossary/machine-learning-ml), performing [data analysis](https://en.wikipedia.org/wiki/Data_analysis), or curating collections for personal projects. Explore more tools and models at [Ultralytics](https://www.ultralytics.com/).

[![Ultralytics Actions](https://github.com/ultralytics/google-images-download/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/google-images-download/actions/workflows/format.yml)
[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

## 🐳 Docker Run

For easy deployment using Docker, visit the dedicated GitHub repository: [google-images-download-by-docker](https://github.com/SaitamaTechno/google-images-download-by-docker).

You can run the scraper within a Docker container using the following command:

```bash
docker run -d -p 80:80 --name image_searcher saitamatechno/google_images_download:v1.0
```

## 📋 Requirements

To use this software effectively, please ensure you have [Python](https://www.python.org/) 3.8 or later installed. You also need to install the necessary dependencies listed in the `requirements.txt` file, which includes libraries like [Selenium](https://www.selenium.dev/documentation/). Install them using pip:

```bash
pip install -r requirements.txt
```

You can find the `requirements.txt` file [here](https://github.com/ultralytics/google-images-download/blob/main/requirements.txt).

## ⚙️ Installation

To set up the Bing image scraper on your local machine, clone this repository and install the required dependencies:

```bash
git clone https://github.com/ultralytics/google-images-download
cd google-images-download
pip install -r requirements.txt
```

## 🖥️ How to Run

Follow these steps to run the image scraper:

1.  **Install Google Chrome**: Ensure Google Chrome is installed on your system. If not, download it from the official [Google Chrome website](https://www.google.com/chrome/).
2.  **Download ChromeDriver**: Get the correct version of ChromeDriver that matches your installed Chrome version. Download links and instructions are available on the [ChromeDriver documentation page](https://developer.chrome.com/docs/chromedriver/). Make sure to note the path to the downloaded `chromedriver` executable.
3.  **Execute the Script**: Run the `bing_scraper.py` script using Python. You can specify a Bing Images search results URL using the `--url` argument or provide search terms directly with the `--search` argument. Images will be saved to the `./images` directory by default. The script is designed to skip images that cause errors during download. For insights into data collection best practices, check out our blog post on [exploring data labeling](https://www.ultralytics.com/blog/exploring-data-labeling-for-computer-vision-projects).

**Example using a URL:**

```bash
python3 bing_scraper.py --url 'https://www.bing.com/images/search?q=wildflowers' --limit 20 --download --chromedriver /path/to/your/chromedriver
```

**Example using search terms:**

```bash
python3 bing_scraper.py --search 'bees collecting pollen' --limit 15 --download --chromedriver /path/to/your/chromedriver

# Output logs will show download progress and any encountered errors.
```

The downloaded images can be useful for creating custom [computer vision datasets](https://docs.ultralytics.com/datasets/).

<img src="https://user-images.githubusercontent.com/26833433/75287228-dcf2ca80-57ce-11ea-9557-cc13abaff453.jpg" width="800" alt="Example output showing downloaded images in a folder">

## 📜 Citing the Project

If you use this software in your research or projects, please acknowledge the original work by citing the [hardikvasa/google-images-download](https://github.com/hardikvasa/google-images-download) repository.

## 🤝 Contributing

Contributions from the community are highly encouraged and appreciated! Your input helps make this open-source tool better for everyone. Whether it's reporting a bug, suggesting a new feature, or submitting code improvements, please refer to our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) for details on how to get started.

We also invite you to participate in our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) to share your feedback, helping us understand your needs and improve our offerings. A heartfelt thank you 🙏 to all our contributors for their dedication and support!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 🔏 License

Ultralytics provides two licensing options to accommodate different usage needs:

- **AGPL-3.0 License**: Ideal for students, researchers, and enthusiasts working on open-source projects. It promotes collaboration and knowledge sharing. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for full details.
- **Enterprise License**: Designed for commercial use cases, this license allows integration of Ultralytics software into proprietary products and services without the open-source requirements of AGPL-3.0. For more information, visit [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📬 Contact

For bug reports, feature requests, or any issues related to this repository, please use the [GitHub Issues](https://github.com/ultralytics/google-images-download/issues) tracker. For broader questions, discussions, and community interaction, join our [Discord](https://discord.com/invite/ultralytics) server.

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
