# Detection of the Malicious Website's URL
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
<br>

## Data processing
First of all,we used parse_url() function to eliminate 'http://' or 'https://' in the front of the whole URL.Then we established a class, named URLFeature, which contains 9 function members. Eight functions is used to calculate 8 features while Final function is used to incorporate the url and 8 features into a list. Besides, we also defined another create_dataset function to calculate 8 features by URLFeatures class and incorporate them into a list. Finally,the create_dataset function write the lists, row by row, into data_urls.csv to save the data for our training model.
![image](https://raw.githubusercontent.com/caoxiaolong0521/PHBS_MLF_2019_Project/master/images/Structure.jpg)

<br> `It will take approximately between 2-3 hours due to feature extraction.`
<br>
`top_website = pd.read_csv('top1m_rank.csv', delimiter='|', usecols = ['URL'], squeeze = True)`
<br>`create_dataset()`
<br>`output:`
<br>malicious: 100/5000
<br>malicious: 200/5000
<br>malicious: 300/5000
<br>malicious: 400/5000
<br>malicious: 500/5000
<br>malicious: 600/5000
<br>malicious: 700/5000
<br>malicious: 800/5000
<br>malicious: 900/5000
<br>malicious: 1000/5000
<br>malicious: 1100/5000
<br>...
<br>benign: 100/5000
<br>benign: 200/5000
<br>benign: 300/5000
<br>benign: 400/5000
<br>benign: 500/5000
<br>benign: 600/5000
<br>benign: 700/5000
<br>benign: 800/5000
<br>benign: 900/5000
<br>...

## Model training
After we get the training data,we defined several functions in the part2.ipynb:
<br>
<br> train_model():This function trains a classifier on the URL dataset. 
<br>
<br> get_learning_curve()、plot_confusion_matrix() and plot_ROC_CURVE() are all evaluation indicators of the model
<br>
<br> `The following sections can be used to determine whether a newly entered URL is malicious or not:`
<br> get_url_info(): Get URL information function extracts features from a user supplied URL. The function extracts all features similarly to extract_features() and saves the extracted features in the form of a dictionary. 
<br> check_valid_url(): Check valid URL function checks whether or not the input URL to classify is in a valid format.
<br> classify_url(): Classify URL function passes in the input URL and classifies it as malicious or benign.

we have try some other algorithms we learned in class,like svm or lr,however,the result is not acceptable for us, we finally choose to use the RandomForest to train the classifier in the train_model() function.

## Model evaluation 
Due to the suitable feature selection,our URL prediction model has obtained relatively good indicators with Cross Validation Score:  92.6 % and F1 Score:  92.72 %

![image](https://github.com/caoxiaolong0521/PHBS_MLF_2019_Project/blob/master/images/ROC.jpg)
![image](https://github.com/caoxiaolong0521/PHBS_MLF_2019_Project/blob/master/images/confusion_matrix.jpg)


