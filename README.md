<br>
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320">

# 🚀 Introduction

Welcome to the Bing image scraping tool, updated and maintained by Ultralytics. This repository contains updated code originally from [https://github.com/hardikvasa/google-images-download](https://github.com/hardikvasa/google-images-download), enabling users to efficiently scrape and download images from Bing for various applications like machine learning, data analysis, or personal projects.

## 📋 Requirements

To use this software, ensure you have Python 3.8 or later and all the necessary dependencies installed. Dependencies can be installed by running the following command in your terminal:

```bash
$ pip install -r requirements.txt
```

The `requirements.txt` file is located [here](https://github.com/ultralytics/google-images-download/blob/master/requirements.txt), which includes `selenium` among others.

## ⚙️ Installation

To set up the image scraper on your machine, clone this repository and install the dependencies as shown below:

```bash
$ git clone https://github.com/ultralytics/google-images-download
$ cd google-images-download
$ pip install -r requirements.txt
```

## 🖥️ How to Run

Run the image scraper following these steps:

1. Ensure Google Chrome is installed on your machine. If not, download and install from [here](https://www.google.com/chrome/).

2. Download and update chromedriver corresponding to your version of Chrome [here](https://chromedriver.chromium.org/).

3. Execute the script. Use the `--url` parameter to download images from a specific Bing URL or the `--search` parameter for Bing search terms. By default, the images will be saved in the `./images` directory. Note that any images that cause errors will be skipped during the download process.

Example usage to download images using a URL:
```bash
$ python3 bing_scraper.py --url 'https://www.bing.com/images/search?q=flowers' --limit 10 --download --chromedriver /path/to/your/chromedriver
```

Example usage to download images using search terms:
```bash
$ python3 bing_scraper.py --search 'honeybees on flowers' --limit 10 --download --chromedriver /path/to/your/chromedriver

# Expect output logs showing the download process and any errors encountered.
```
<img src="https://user-images.githubusercontent.com/26833433/75287228-dcf2ca80-57ce-11ea-9557-cc13abaff453.jpg" width="">

## 📜 Citing the Project

To acknowledge the use of this software in your works, please reference the original repository, which can be found [here](https://github.com/hardikvasa/google-images-download).

## 🤝 Contributing

We warmly welcome contributions from the community. Your support and contributions are invaluable in making this open-source software greater. Whether you've found a bug, have a feature suggestion, or want to contribute code, please have a look at the [Contributing Guide](https://docs.ultralytics.com/help/contributing). Furthermore, take a moment to fill out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey); your feedback helps us improve continuously. A big thank you 🙏 goes to all the contributors!

<!-- Image to showcase our contributors -->
<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

## 🔏 License

We offer two types of licensing to cater for a variety of use cases:

### AGPL-3.0 License

This license is ideal for individuals or teams working on non-commercial projects. It encourages openness, collaboration, and the sharing of knowledge and improvements. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) for all the details.

### Enterprise License

For commercial applications, the Enterprise License provides a solution that enables the integration of Ultralytics software into your products without the restrictions of AGPL-3.0. This license is suited for commercial offerings where the specifics of AGPL-3.0 are not appropriate. If you are interested in an enterprise solution, please reach out to us for more information through [Ultralytics Licensing](https://ultralytics.com/license).

## 📬 Contact

If you encounter any issues or have features you'd like to request, please visit our [GitHub Issues](https://github.com/ultralytics/google-images-download/issues) page. For general discussions, questions, or to connect with the community, join our vibrant [Discord](https://ultralytics.com/discord) community.

<br>
<div align="center">
  <!-- Social media and contact icons -->
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
  <a href="https://www.instagram.com/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="3%" alt="Ultralytics Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
```

* The above markdown enhancement adds some emojis to increase friendliness, provides additional context in section introductions for better clarity, and ensures that technical steps are explained in a concise but thorough manner. The updates adhere to the AGPL-3.0 license and maintain a professional yet accessible tone. Links and images have not been removed but rather used to ensure continued recognition of the original repository and its contributors.
