<a name="readme-top"></a>
<br />
<div align="center">

  # 🍁 Estimate Your Chances to Get a PR in Canada 🍁
  ### Data Analysis and Machine Learning for Immigration Strategy
  <img src="docs/1.jpg" alt="Logo" width="600" height="600">
  </a>

</div>

## 🔎 Project Overview 

This project utilizes data analysis and machine learning techniques to improve the understanding and prediction of obtaining Permanent Residency (PR) in Canada based on various personal and professional criteria.

## Project stage for now

1. Gradio provides a simple UI that any user can run on their own machine and even make it accessible to other users from the internet.
2. Users can input certain characteristics and understand their chances of receiving Permanent Residency (PR) in Canada based on historical data.
3. Notebooks contain Exploratory Data Analysis (EDA) and basic data cleaning. I didn't realize modeling in Jupyter notebooks. Modeling is realized in the Python code.

### The initiative aims to address:

"How can we leverage data and machine learning to inform potential immigrants of their chances of obtaining PR in Canada?"

## 📖 Table of Contents
  
  <ol>
    <li><a href="#motivation">Project Motivation</a></li>
    <li><a href="#data">The Data</a></li>
    <li><a href="#dict">Data Dictionary</a></li>
    <li><a href="#roadmap">Project Roadmap</a></li>
    <li><a href="#learnings">Learnings</a></li>
    <li><a href="#conclusions">Conclusions</a></li>
    <li><a href="#next">Next Steps</a></li>
    <li><a href="#license">License</a></li>
  </ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="motivation"> 💪🏽 Project Motivation </h2>

The motivation behind this project is to provide a comprehensive tool that helps potential immigrants to Canada to assess their chances of obtaining PR, making the immigration process more transparent and informed.

<h2 id="data">📊 The Data</h2>
The data for this project is derived from various public sources and immigration reports, focusing on factors known to influence PR application outcomes in Canada.

Publisher - Current Organization Name: Immigration, Refugees and Citizenship Canada

<a href="https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda">Data</a>

<h2 id="dict"> 📖 Data Dictionary</h2>
  
The data is 12 stand alone csv files with one common field which is landing_year.

| Column                                        | DataType | Description                                                         |
|-----------------------------------------------|----------|---------------------------------------------------------------------|
| persons_count                                 | int64    | The number of individuals (consideration for non-numeric entries needed). |
| landing_year                                  | int64    | The year individuals landed.                                        |
| education_qualification_eng_desc              | object   | Description of the individual's educational qualification in English. |
| permit_holders                                | int64    | The number of permit holders.                                       |
| citizenship_country                           | object   | The country of citizenship of the permit holders.                   |
| birth_country                                 | object   | The country of birth of the permit holders.                         |
| person_age_level1_eng_desc                    | object   | Description of the age range of the individuals in English.         |
| gender_eng_desc                               | object   | Description of the gender of the individuals.                       |
| main_category_eng_desc                        | object   | The main category of immigration.                                   |
| group_eng_desc                                | object   | The group description within the main category.                     |
| component_eng_description                     | object   | The component description within the group.                         |
| marital_status_eng_desc                       | object   | Description of the marital status of the individuals.               |
| noc_2011_level4_eng_desc                      | object   | Description of the National Occupational Classification (NOC) 2011 at level 4. |
| preferred_language_eng_desc                   | object   | Description of the preferred language of the individuals.           |
| province_long_eng_desc                        | object   | Description of the province where the individuals landed.           |
| skill_level1_eng_desc                         | object   | Description of the skill level (broad category) of the individuals. |
| skill_level2_eng_desc                         | object   | Description of the skill level (more specific category) of the individuals. |



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="roadmap"> 🚙 Project Roadmap </h2>
# Road Map

Estimate your chances to get a PR in Canada and choose the most effective strategy.

## The Problem Area

- Immigrants to Canada struggle to understand their chances to get PR.
- They struggle to choose the criteria that leads to a PR in an appropriate terms.
- There are lots of programs a newcomer can apply to get a PR so people struggle to choose the most suitable program.

## Challenges and Opportunities

- My project can reduce time for understanding newcomers' chances to get PR.
- Choose the best strategy to get a PR.
- Prioritize newcomers' efforts.
- Can we predict if a person receives PR or not by entering a certain criteria?
- Based on Government historical data for the last 10 years of receiving PR, can we predict if a newcomer likely get PR or not.

## The User

- Thousands of newcomers benefit from knowing their chances of receiving PR in Canada.
- Some of them can also reject the idea of receiving a PR in a certain place and save money and time moving to another province or leaving Canada.

## The Big Idea

- How can we use machine learning to predict the likelihood of newcomers obtaining permanent residency (PR) in Canada so we can more effectively support them in achieving their PR goals?
- Machine learning can estimate the probability of receiving a PR onto given personal criteria. It might be Numerical prediction and Categorical predictions. Next is Point Forecast if enough data and time for capstone project.

### Input

- Personal criteria

### Output

- Probability to receive a PR by entered criteria
- Best strategy
- Most suitable province
- Most suitable program
- Better to reconsider ability to stay in Canada

## The Impact

- Save Canada government money by reducing the number of irrelevant PR cases.
- Increase the efficiency of PR decisions.
- Reduce the number of employees in IRCC.
- Reduce of non-relevant newcomers per province thus less self-serve expenses from Canada government.

## Core Idea

- Newcomer wants to estimate his chances to receive a PR twice: general score the best strategy.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="learnings"> 💡 Learnings </h2>

Understanding PR Chances: Many immigrants to Canada find it challenging to gauge their chances of obtaining permanent residency (PR) due to the complexity and variety of criteria and programs available.

Strategic Planning: Choosing the most effective strategy for obtaining PR requires a deep understanding of these criteria and the ability to prioritize efforts based on individual circumstances.

The Role of Data: Historical data on PR acceptance over the past decade can be instrumental in predicting a newcomer's likelihood of obtaining PR, highlighting the potential of data-driven decision-making.

Machine Learning Application: Applying machine learning to this data can provide personalized predictions about PR chances based on individual criteria, which could significantly assist newcomers in making informed decisions.

Personal Criteria Importance: The system considers various personal criteria such as age, country of origin, language level, and education, underscoring the multifaceted nature of PR applications.

Government Efficiency: By reducing irrelevant PR cases, the project aims to save government resources, streamline the PR decision-making process, and optimize the distribution of newcomers across provinces.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="conclusions"> 🎬 Conclusions </h2>

1. The course demystified data science for me throughout its duration.
2. Statistics is a powerful methodology that can be applied to almost any set of digital data.
3. Neural networks are highly useful for automating the process of finding weights and extracting valuable insights from vast amounts of data that humans cannot process or fully comprehend as a single entity.
4. Canada's immigration programs are complex and not very transparent. Despite claims from IRCC about data openness, it is often not the case.
5. The most challenging aspect is understanding and addressing survival bias, especially when data on rejections or other types of unsuccessful cases are scarce.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="next"> ⏭️ Next Steps </h2>

1. Continue to improve the data model.
2. Apply neural networks.
3. Make a new query to IRCC to gain data about refusals and the number of abandoned cases.
4. Add two datasets with country of birth and citizenship.
5. Improve the user interface, adding new fields.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<h2 id="license"> 📜 License </h2>

MIT License

Copyright (c) 2024 Roman Ihnatov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
