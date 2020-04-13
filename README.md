# Detection of the Malicious Websites' URL
## 0. Group-11 Members

Name | Github ID | Student ID 
:-: | :-------------------------------: | :-:
[Lei HU](https://github.com/huleipku)     |     huleipku     |     1901212585    
[Jinze HE](https://github.com/Hejinzefinance)     |     Hejinzefinance     |     1901212582    
[Yixin ZHAO](https://github.com/Zhaoyixin9705)     |     Zhaoyixin9705     |     1901212681    
[Aiyu CAO](https://github.com/caoxiaolong0521)     |     caoxiaolong0521     |     1801212821    

##  1. The Goal of our Project
In order to **detect the security of a URL** (i.e. whether the website is malicious), we try to construct some reasonable features from the urls in`malicious_urls.csv` and `benign_urls.csv` . Then we use them to train our machine learning detection model.

## 2. Framework of our Project

1. Preprocess data & extract features

2. Train model via Random Forest & Model Evaluation 

3. Model Application

   <img src="images/Framework.png" height=500 align='middle' style='margin: 0 auto'/>

## 3. Data Preprocessing & Feature Extraction

###  3.1 [Description of Dataset](data/README.md)

### 3.2 Preprocessing
* In this part, the preprocessing means that we want to **remove the prefix** like `http://` or `https://` from the URLs. The reason is that the prefix is not helpful to judge the website, or even affect the calculation of the features.
* In the code, we define a function `parse_url` to remove the prefix. If you want to see the source code, please turn to [Part-1 Create_dataset_for_training_model.ipynb](Part-1/Part-1%20Create_dataset_for_training_model.ipynb).

### 3.3 Feature Selection
Feature name | Explanations about the feature 
:-: | -
`Entropy` | Entropy was originally a concept proposed in the field of physics, which is used to *measure the degree of chaos in a system*. Then, Shannon borrowed this concept and proposed the information entropy. And many researches have shown that **malicious URLs often have a higher information entropy**. And the class `Entropy` is to calculate the information entropy.
`bag_of_words` | Research also shows that **malicious URLs usually contains more words of different categories**, so *how many different kinds of words* that have appeared in the URL can also be an effective feature. And `bag_of_words` is to calculate this feature. 
`contains_IP` | *Whether a URL contains an IP address* is also a powerful indicator. So we need to check the occurence of an IP address within a URL since the **benign URL will not contain IP** in most cases.
`url_length` | It is intuitive that **malicious URLs can often be very long** in comparison to benign URLs. For example, the official website of [Baidu](https://www.baidu.com/), [GitHub](https://github.com/), [Google](www.google.com) are all relatively short.
`special_chars` | Sometimes **malicious URLs contain a larger number of special characters**, like ';','%','!','&',':', etc. So we introduce the feature `special_chars` to reflect. 
`num_digits` | Researches also show that **malicious URLs usually contain more numbers**. So the number of digits is also a good feature.
`suspicious_strings` |  A higher number of suspicious strings would more possibly indicate a malicious URL. So we introduce `suspicious_strings` to describe the feature.
`popularity` | If a website is more popular, it means more people are willing to visit, which reflects the low chance or possibility to be malicious. So the websites contained within the top 1 million URLs dataset are not likely to be malicious.

### 3.4 Feature Calculation
* After selecting the features to use, we established a class called `URLFeatures` to calculate the value of the features. 
* The picture below shows the structure of the class. The class `URLFeatures` contains 9 function members (8 functions for calculating, 1 final function for incorporating the URL and its corresponding features into a list). 
<img src="images/Structure.jpg" height=500 align='middle' style='margin: 0 auto'/>
* Based on `parse_url` and `URLFeatures`, we defined the function `extract_features` to combine the preprocessing part and the calculation of features into one step.
* At last, we define the function `create_dataset` to calculate the 8 features of our selected data and save them into `data_urls.csv` (*it will take approximately 2-3 hours*).
* The source code is in [Part-1 Create_dataset_for_training_model.ipynb](Part-1/Part-1%20Create_dataset_for_training_model.ipynb).

### 3.5 Create Dataset ([data_urls.csv](data/data_urls.csv))

+ After loading 10000 urls and extracting their 8 features, we store the data in csv format to prepare for training model below

## 4. Train model via Random Forest & Model Evaluation
### 4.1 Train model

* After we obtain the training data (`data_urls.csv`), we need to train the model next.
* The model we chose is the **Random Forest** (we also tried other models like SVM and logistic regression, but the result is not so good). 
* The source code of training the model is in [Part-2 Train_model.ipynb](Part-2/Part-2%20Train_model.ipynb).

### 4.2 Model Evaluation

* In order to evaluate the performance of the model, we mainly used ROC curve, Confusion Matrix, explained variance components and learning curve. The figures and corresponding results are shown below.

1. **ROC curve**:  **ROC** curve is far from diagonal line and **AUC** is near from 1. Thus, our model's prediction ability is well.
<img src="images/ROC.jpg" height=500, align='middle' style='margin: 0 auto'/>
2. Confusion Matrix: PRE & REC are really high, indicating our model is doing well.
<img src="images/confusion_matrix.jpg" height=500/>
3. Explained Variance of Components: The first 6 primary components have relatively high variance ratio, which indicate that most of our features are useful.
<img src="images/explained_variance.png" height=500, align='middle' style='margin: 0 auto'/>
4. Learning Curve: From the learning curve, we can see that our model is not biased and variation is not very high.
 <img src="images/learning_curve.jpg" height=500, align='middle' style='margin: 0 auto'/>

* As for other indicators, the cross validation score is *87.30%* and F1-score is *89.53%*, the results are shown in [Part-2 Train_model.ipynb](Part-2/Part-2%20Train_model.ipynb).

## 5. Model Application (Unfinished)
* After the process above, we defined the function `classify_url` based on the trained model to classify a new website's URL. But before the prediction, we need to check whether the input URL is in a valid format using the function `check_valid_url`.
* The source code is in the last part of [Part-2 Train_model.ipynb](Part-2/Part-2%20Train_model.ipynb).
