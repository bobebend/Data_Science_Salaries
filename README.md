# Data_Science_Salaries

This is my prefered dataset

# 1 Where your dataset can be found
    https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023

    (Data originally was sourced from aijobs.net.)

# 2 Potential dataset repository submission
    git@github.com:bobebend/Data_Science_Salaries.git

# 3 Dataset Shape
    (rows 3755, columns 11)

# 4 Describe the fields

    There are 11 columns:
        -work_year
        -experience_level
        -employment_type
        -job_title
        -salary
        -salary_currency
        -salary_in_usd
        -employee_residence
        -remote_ratio
        -company_location
        -company_size


    How many categorical fields? What do they represent?
        There are seven categorical fields. They generally represent experience level, employment type, job title,salary currency, employee residence, company location and size.

    How many quantitative? What do they represent?
        There are four quantitative fields. They are work year(all in this column from 2023 since this is a 2023 dataset), salary(in US, British or some other currency), salary in usd(salary column converted to usd if paid in other than usd), and remote ratio(overall work done remotely)

    Is there missing data or data that seems to be wrong somehow (e.g. age = -99)? 
        There was no missing data

    Has the data already been summarized, or are the observations raw and unprocessed?
        To my knowledge they are unprocessed, at least that is how I am treating them.  



# 5 Potential avenues of inquiry

    What types of questions does this dataset seem to support?

        1 What job titles are the most prevalant
        2 Salary for those job titles
        3 Experience level per job title
        4 Remote to Office work comparison 


# 6 Value proposition

        Providing a brief to Data Analysis students on potential career paths and possible salaries.

        My train of thought is to explore:
            1 What job titles there are
            2 What pay those job titles are receiving
            3 What level of experience the job titles generally have.

