# webpage-to-pdf

This script batch exports webpages to pdf files.

## Dependency
- [Pandas](https://pandas.pydata.org/getting_started.html) 
- [Serenium](https://pypi.org/project/selenium/)
- [Google Chrome](https://www.google.com/chrome/)
- [Chrome Webdriver](https://chromedriver.chromium.org/downloads)\
Notice: Version of webdriver and browser shall match. 

## Usage
1. Paste the links to webpages and name of downloaded files to `reference.csv`.
2. In `download.py`, edit `PDF_savepath`, `webdriver_path` and `reference`.
3. Execute `download.py`.

# webpage-to-pdf

这个脚本能批量导出网页为pdf文件。

## 依赖
- [Pandas](https://pandas.pydata.org/getting_started.html) 
- [Serenium](https://pypi.org/project/selenium/)
- [Google Chrome](https://www.google.com/chrome/)
- [Chrome Webdriver](https://chromedriver.chromium.org/downloads)\
注意：webdriver和浏览器版本建议相同。

## 用法
1. 将链接和下载文件名粘入`reference.csv`。
2. 编辑`download.py`中的 `PDF_savepath`、`webdriver_path`和`reference`。
3. 运行`download.py`。
