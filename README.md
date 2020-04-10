# Group Project for MLF_2019
## Detection of URL of Malicious Website
### Group members
Name | Github ID | Student ID 
:-: | :-------------------------------: | :-:
[Lei HU](https://github.com/huleipku)     |     huleipku     |     1901212585    
[Jinze HE](https://github.com/Hejinzefinance)     |     Hejinzefinance     |     1901212582    
[Yixin ZHAO](https://github.com/Zhaoyixin9705)     |     Zhaoyixin9705     |     1901212681    
[Aiyu CAO](https://github.com/caoxiaolong0521)     |     caoxiaolong0521     |     1801212821    

###  Description of dataset
* `malicious_urls.csv` and `benign_urls.csv` are malicious and benign data sets, which containing 5000 data respectively.
* `top1m_rank.csv` contains the top 1 million URLs which are often used in people's daily life.
* `data_ulrs.csv` is the training data set after we construct and extract features from the raw datasets
<br>

* malicious urls examples：
<br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405
<br> http://businesspage.ecuaradionline.com
<br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821

* benign urls examples：
<br>api-global.netflix.com
<br>www.google.com
<br>microsoft.com

* top1 million urls examples：
<br> apple.com
<br> live.com
<br> www.googleapis.com

* training dataset examples:
<br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405/|4.603980434631428|5|0|69|0|0|19|0|1|1
<br> http://businesspage.ecuaradionline.com/|3.9056390622295662|3|0|32|0|0|0|0|1|1
<br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821/|4.229085753935212|6|0|60|0|0|17|0|1|1

* Data source:
<br> https://openphish.com/feed.txt
<br> https://ransomwaretracker.abuse.ch/blocklist/
<br> https://www.phishtank.com/

###  The goal of our project
In order to **detect the security of a URL** (i.e. whether the website is dangerous to visit), we try to construct some reasonable features from the `malicious_urls.csv` and `benign_urls.csv` data sets, and use this to train our machine learning detection model.

