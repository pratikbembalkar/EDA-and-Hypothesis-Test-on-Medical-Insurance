# Medical Insurance Data Analysis

## Project Description
This project aims to analyze a medical insurance dataset to uncover factors influencing insurance charges. By performing exploratory data analysis (EDA) and hypothesis testing, we gain insights into the impact of variables like age, BMI, and smoking status on charges. The findings can guide insurance companies in understanding risk profiles and optimizing pricing strategies.


### 2. Exploratory Data Analysis (EDA)
- **Aim**: To explore the distribution and relationships between key variables, such as sex, region, smoker status, BMI, and age, in relation to medical insurance charges.

#### A. Patient Demographics Distribution
  - **Objective**: To understand the distribution of patients by sex, region, and smoker status.
  - **Steps**:
    - Used `sns.countplot()` to visualize counts of male and female patients.
    - Created a count plot to show the distribution of patients across different regions.
    - Plotted smoker versus non-smoker counts.
    - **Insight**: These visualizations provide an initial understanding of the composition of the dataset, identifying the proportions of smokers, regions, and genders represented.

#### B. Proportion Analysis of Categorical Variables
  - **Objective**: To calculate and compare proportions within categorical features.
  - **Steps**:
    - Calculated the proportion of each category within 'sex', 'smoker', and 'region' columns.
    - **Insight**: This helps understand the relative size of each subgroup within the dataset.

#### C. Insurance Charges Analysis
  - **Objective**: To assess the total and subgroup-specific insurance charges.
  - **Steps**:
    - Calculated total charges and displayed the value in millions.
    - Grouped by `sex`, `smoker`, and `region` to calculate mean and total charges, as well as each subgroup's percentage of total charges.
    - **Insight**: This highlights how charges are distributed among different demographics and smoking habits, showing which groups contribute most to total insurance costs.

#### D. BMI Analysis
  - **Objective**: To explore BMI distribution across different demographics.
  - **Steps**:
    - Calculated total BMI across the dataset.
    - Grouped by `sex` and `smoker` status to calculate mean and total BMI, including the percentage of total BMI contributed by each group.
    - **Insight**: This provides insight into BMI patterns, helping assess health-related risk factors by subgroup.

#### E. Regression and Pairwise Relationships
  - **Objective**: To examine relationships between age, BMI, and other variables.
  - **Steps**:
    - Created regression plots of age vs. BMI, highlighting `sex`, `region`, and `smoker` status to see trends between age and BMI by group.
    - Used a joint plot to observe the joint distribution and correlation between age and BMI.
    - Created a pair plot to visualize pairwise relationships between variables with respect to sex.
    - **Insight**: These visualizations uncover patterns in age, BMI, and insurance features, which could point toward key factors impacting charges.


### 3. Hypothesis Testing (Summarize->Details on the notebook)
- **Aim**: To statistically validate relationships and differences between categorical variables, BMI, and charges in the dataset. This helps determine if observed patterns are significant or due to random chance.

#### A. Chi-Square Test for Independence
  - **Objective**: To test if there is a significant association between categorical variables.
  - **Steps**:
    - Conducted chi-square tests between:
      - `sex` and `smoker` status.
      - `sex` and `region`.
      - `smoker` status and `region`.
    - **Insight**: These tests determine if being a smoker, region, or gender is independent of each other in the dataset.

#### B. Type II Error Assessment
  - **Objective**: To check the potential of incorrectly failing to reject a false null hypothesis by analyzing ratios in different regions.
  - **Steps**:
    - Calculated the ratio of male to female patients and non-smokers to smokers for each region.
    - **Insight**: Helps in understanding the distribution of these subgroups across different regions.

#### C. One-Sample T-Test
  - **Objective**: To determine if the BMI mean of specific subgroups differs significantly from the overall mean.
  - **Steps**:
    - Conducted one-sample t-tests for:
      - BMI by `sex` (female and male).
      - BMI by `smoker` status (yes and no).
      - BMI for each `region` (e.g., southwest, southeast).
    - **Insight**: Shows if the BMI for each group deviates significantly from the population mean.

#### D. Two-Sample T-Test
  - **Objective**: To compare the mean BMI between two independent groups.
  - **Steps**:
    - Compared BMI between:
      - Female and male patients.
      - Smokers and non-smokers.
    - **Insight**: Identifies if there are significant BMI differences between genders or smoking status.

#### E. Paired T-Test
  - **Objective**: To assess if there is a significant mean difference in `age` between pairs of groups.
  - **Steps**:
    - Conducted paired t-tests between:
      - Female and male patients.
      - Smokers and non-smokers.
    - **Insight**: Checks if age distribution varies significantly between these paired groups.

#### F. Normality Testing and Standardization
  - **Objective**: To confirm if the BMI distribution is normal and to standardize it.
  - **Steps**:
    - Normalized BMI data using Box-Cox transformation.
    - Verified normality with a Shapiro-Wilk test.
    - Calculated mean and standard deviation of the normalized BMI.
    - **Insight**: Ensures that the data meets assumptions for further tests and analysis.

#### G. Z-Tests
  - **Objective**: To compare the mean BMI or cost between two populations.
  - **Steps**:
    - Conducted one-sample z-tests for BMI of new samples against the original.
    - Conducted a two-sample z-test to compare costs between female and male patients.
    - **Insight**: Highlights significant differences between groups for specified measures.

#### H. ANOVA Test
  - **Objective**: To compare mean BMI across multiple groups to see if there is a significant difference.
  - **Steps**:
    - Performed one-way ANOVA for BMI by `sex`.
    - Conducted a two-way ANOVA to analyze BMI differences by `sex` and `region`.
    - **Insight**: Indicates if multiple groups have statistically different mean `BMI`s.

