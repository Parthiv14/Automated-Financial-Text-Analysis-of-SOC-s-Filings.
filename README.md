# Automated Financial Text Analysis of SOC's Filings.

Extracted the data from SEC / EDGAR financial reports using NLTK tokenizer 
model. This website contained all the financial terms that were required. Each text file consists of at least one to three subsections. We divided the subsections into three different variables  namely “Management and Discussion Analysis” , “Qualitative and Quantitative Risk Analysis” and  “Risk Factors”. All these variables contained some of the positive, negative ,constrain and uncertain terms. Humans Understand the meaning of emotions and they can segregate the terms associated with it.I created a list of words having all the positive, negative, certain and uncertain terms. While extracting it is easy for the test cell to get trained beforehand. 

## Objective

Objective of this assignment is to extract some sections (which are mentioned below) from SEC / EDGAR financial reports and perform text analysis to compute variables those are explained below. 

Link to SEC / EDGAR financial reports are given in excel spreadsheet “cik_list.xlsx”. 
The link is :- https://www.sec.gov/Archives/ is added to every cells of column F (cik_list.xlsx) to access link to the financial report. 

Example: Row 2, column F contains edgar/data/3662/0000950170-98-000413.txt
Add https://www.sec.gov/Archives/ to form financial report link i.e. 
https://www.sec.gov/Archives/edgar/data/3662/0000950170-98-000413.txt 




## Variables
Section 1.1: Positive score, negative score, polarity score

Section 2: Average Sentence Length, percentage of complex words, fog index

Section 4: Complex word count

Section 5: Word count
 
In addition to these eight variables, compute two more items: “uncertainty” and “constraining”. These variables are calculated similar to the ones in Section 1.1 or Section 4. Attached the lists of words that are classified as uncertain or constraining.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[IRJET](https://irjet.net/archives/V7/i9/IRJET-V7I937.pdf)
