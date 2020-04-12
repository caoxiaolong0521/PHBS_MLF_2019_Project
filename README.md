# Detection of URL of Malicious Website
## Group members
Name | Github ID | Student ID 
:-: | :-------------------------------: | :-:
[Lei HU](https://github.com/huleipku)     |     huleipku     |     1901212585    
[Jinze HE](https://github.com/Hejinzefinance)     |     Hejinzefinance     |     1901212582    
[Yixin ZHAO](https://github.com/Zhaoyixin9705)     |     Zhaoyixin9705     |     1901212681    
[Aiyu CAO](https://github.com/caoxiaolong0521)     |     caoxiaolong0521     |     1801212821    

##  The goal of our project
In order to **detect the security of a URL** (i.e. whether the website is dangerous to visit), we try to construct some reasonable features from the `malicious_urls.csv` and `benign_urls.csv` data sets, and use this to train our machine learning detection model.

##  Description of raw dataset
* `malicious_urls.csv` and `benign_urls.csv` are malicious and benign data sets, which containing 5000 data respectively.
* `top1m_rank.csv` contains the top 1 million URLs which are often used in people's daily life.
* `data_ulrs.csv` is the training data set after we construct and extract features from the raw datasets

* malicious urls examples：
<br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405
<br> http://businesspage.ecuaradionline.com
<br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821

* benign urls examples：
<br>www.api-global.netflix.com
<br>www.google.com
<br>www.microsoft.com

* top1 million urls examples：
<br> www.apple.com
<br> www.live.com
<br> www.googleapis.com

* training dataset examples:
<br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405/|4.603980434631428|5|0|69|0|0|19|0|1|1
<br> http://businesspage.ecuaradionline.com/|3.9056390622295662|3|0|32|0|0|0|0|1|1
<br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821/|4.229085753935212|6|0|60|0|0|17|0|1|1

* Data source:
<br> https://openphish.com/feed.txt
<br> https://ransomwaretracker.abuse.ch/blocklist/
<br> https://www.phishtank.com/

## Feature Choosing （The selected features are both static and external）
### Entropy
* Malicious URLs often have a higher entropy.
### bag_of_words
* It seems like Malicious URLs often contains more words, so the number of kind of words that have appeared in the url can also be a good feature.
### contains_IP 
* we need to check the occurence of an IP address within a URL since the benign URL will not contain IP in most cases, .
### url_length
* Malicious URLs can often be very long in comparrison to benign URLs.
### special_chars
* Sometimes Malicious URLs contain a higher number of special characters,like ';','%','!','&',':'.
### num_digits
* Malicious URLs often have higher entropy and can contain lots of numbers.
### suspicious_strings
* A higher number of suspicious strings would indicate a possibly malicious URL.
### popularity
* Sites contained within top1 million urls dataset are not malicious.

## Data processing
First of all,we used parse_url() function to eliminate 'http://' or 'https://' in the front of the whole URL.Then we established a class, named URLFeature, which contains 9 function members. Eight functions is used to calculate 8 features while Final function is used to incorporate the url and 8 features into a list. Besides, we also defined another create_dataset function to calculate 8 features by URLFeatures class and incorporate them into a list. Finally,the create_dataset function write the lists, row by row, into data_urls.csv to save the data for our training model.
<br>
`top_website = pd.read_csv('top1m_rank.csv', delimiter='|', usecols = ['URL'], squeeze = True)`
<br>`create_dataset()`
<br>`output:`
<br>`malicious: 100/5000
malicious: 200/5000
malicious: 300/5000
malicious: 400/5000
malicious: 500/5000
malicious: 600/5000
malicious: 700/5000
malicious: 800/5000
malicious: 900/5000
malicious: 1000/5000
malicious: 1100/5000
malicious: 1200/5000
malicious: 1300/5000
malicious: 1400/5000
malicious: 1500/5000
malicious: 1600/5000
malicious: 1700/5000
malicious: 1800/5000
malicious: 1900/5000
malicious: 2000/5000
malicious: 2100/5000
malicious: 2200/5000`



