# Description of Dataset

## 1. Introduction to  Data Files

1. `malicious_urls.csv` and `benign_urls.csv` are malicious and benign data sets, which contain 5000 data respectively.

2. `top1m_rank.csv` contains the top 1 million URLs which are often used in people's daily life, which must be benign urls.

3. `data_urls.csv` is the training data set after we constructed and extracted features from the origin data in `malicious_urls.csv` and `benign_urls.csv`.

## 2. Data Examples

1. malicious urls examples：
   <br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405
   <br> http://businesspage.ecuaradionline.com
   <br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821

2. benign urls examples：
   <br>www.api-global.netflix.com
   <br>www.google.com
   <br>www.microsoft.com

3. top1 million urls examples：
   <br> www.apple.com
   <br> www.live.com
   <br> www.googleapis.com

4. training dataset examples:
   <br> http://www.businesspage.ecuaradionline.com/9feaf7f8354ad68ba40e29d70cd05405/|4.603980434631428|5|0|69|0|0|19|0|1|1
   <br> http://businesspage.ecuaradionline.com/|3.9056390622295662|3|0|32|0|0|0|0|1|1
   <br> http://www.lotto109.com/follow-up/eb6e30faeebb16feaf07ae96e6e2e821/|4.229085753935212|6|0|60|0|0|17|0|1|1

5. Data source:
   <br> https://openphish.com/feed.txt
   <br> https://ransomwaretracker.abuse.ch/blocklist/
   <br> https://www.phishtank.com/