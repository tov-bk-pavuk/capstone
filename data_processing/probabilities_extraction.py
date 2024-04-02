import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.compose import ColumnTransformer

from pprint import pprint

datasets = {
    "raw_data_age": pd.read_csv("../data/IRCC_AdhocSR_PR_0001_E.csv", index_col=0),
    # todo implement raw_data_census in further versions
    # "raw_data_census": pd.read_csv("../data/IRCC_AdhocSR_PR_0002_E.csv", encoding='ISO-8859-1', index_col=0),
    "raw_data_birth_country": pd.read_csv("../data/IRCC_AdhocSR_PR_0003_E.csv", index_col=0),
    "raw_data_citizenship": pd.read_csv("../data/IRCC_AdhocSR_PR_0004_E.csv", index_col=0),
    "raw_data_education": pd.read_csv("../data/IRCC_AdhocSR_PR_0005_E.csv", index_col=0),
    "raw_data_gender": pd.read_csv("../data/IRCC_AdhocSR_PR_0006_E.csv", index_col=0),
    "raw_data_legal_status": pd.read_csv("../data/IRCC_AdhocSR_PR_0007_E.csv", index_col=0),
    "raw_data_marital_status": pd.read_csv("../data/IRCC_AdhocSR_PR_0008_E.csv", index_col=0),
    "noc_2011": pd.read_csv(
        "../data/IRCC_AdhocSR_PR_0009_E.csv", encoding='ISO-8859-1', index_col=0
        ),
    "raw_data_preferred_language": pd.read_csv("../data/IRCC_AdhocSR_PR_0010_E.csv", index_col=0),
    "raw_data_province": pd.read_csv("../data/IRCC_AdhocSR_PR_0011_E.csv", index_col=0),
    "raw_data_skill_level_2": pd.read_csv("../data/IRCC_AdhocSR_PR_0012_E.csv", index_col=0),
    }

for dataset in datasets.values():
    dataset.reset_index(inplace=True)
    # Check and convert 'persons_count' if it exists
    if "persons_count" in dataset.columns:
        dataset["persons_count"] = pd.to_numeric(dataset["persons_count"], errors="coerce")

    # Alternatively, check and convert 'permit_holders' if it exists
    elif "permit_holders" in dataset.columns:
        dataset["permit_holders"] = pd.to_numeric(dataset["permit_holders"], errors="coerce")

    # Check and rename 'persons_count' if it exists
    if "persons_count" in dataset.columns:
        new_name = f"persons_count_{dataset.columns[2][:5]}"
        dataset.rename(columns={"persons_count": new_name}, inplace=True)

    # Check and rename 'permit_holders' if it exists
    if "permit_holders" in dataset.columns:
        new_name = f"permit_holders_{dataset.columns[2][:5]}"
        dataset.rename(columns={"permit_holders": new_name}, inplace=True)


def get_age_probabilities():
    age_dataset = datasets["raw_data_age"].drop(columns="landing_year")
    age_dataset = age_dataset[age_dataset.person_age_level1_eng_desc != "Not stated"]

    summed_by_age = pd.DataFrame(age_dataset.groupby("person_age_level1_eng_desc").sum()).reset_index()
    total_pr_receivers = age_dataset.groupby("person_age_level1_eng_desc").sum().sum()

    result_dict = {}
    for age, amount in zip(summed_by_age["person_age_level1_eng_desc"], summed_by_age["persons_count_perso"]):
        age_probability = amount / total_pr_receivers * 100
        result_dict[age] = round(age_probability.iloc[0], 4)
        print(f"{age} = {round(age_probability.iloc[0], 4)}")

    return result_dict


def get_birth_country():
    birth_country_dataset = datasets["raw_data_birth_country"].drop(columns="landing_year")
    birth_country_dataset.dropna(inplace=True)

    total_pr_receivers = birth_country_dataset.groupby("birth_country").sum().sum()

    summed_by_birth_country = pd.DataFrame(birth_country_dataset.groupby("birth_country").sum()).reset_index()

    birth_country_dict = {}
    for birth_country, amount in zip(
            summed_by_birth_country["birth_country"], summed_by_birth_country["permit_holders_birth"]
            ):
        a = amount / total_pr_receivers * 100
        birth_country_dict[birth_country] = round(a.iloc[0], 4)
        print(f"{birth_country} = {round(a.iloc[0], 4)}")

    return birth_country_dict


def get_citizenship():
    citizenship_dataset = datasets["raw_data_citizenship"].drop(columns="landing_year")
    citizenship_dataset.dropna(inplace=True)

    total_pr_receivers = citizenship_dataset.groupby("citizenship_country").sum().sum()

    summed_by_citizenship = pd.DataFrame(citizenship_dataset.groupby("citizenship_country").sum()).reset_index()

    citizenship_dict = {}
    for citizenship, amount in zip(
            summed_by_citizenship["citizenship_country"], summed_by_citizenship["permit_holders_citiz"]
            ):
        a = amount / total_pr_receivers * 100
        citizenship_dict[citizenship] = round(a.iloc[0], 4)
        print(f"{citizenship} = {round(a.iloc[0], 4)}")

    return citizenship_dict


def get_education():
    education_dataset = datasets["raw_data_education"].drop(columns="landing_year")
    education_dataset.dropna(inplace=True)

    total_pr_receivers = education_dataset.groupby("education_qualification_eng_desc").sum().sum()

    summed_by_education = pd.DataFrame(
        education_dataset.groupby("education_qualification_eng_desc").sum()
        ).reset_index()

    education_dict = {}
    for education, amount in zip(
            summed_by_education["education_qualification_eng_desc"], summed_by_education["persons_count_educa"]
            ):
        a = amount / total_pr_receivers * 100
        education_dict[education] = round(a.iloc[0], 4)
        print(f"{education} = {round(a.iloc[0], 4)}")


def get_data_probabilities(dataset_name: str, numeric_column_name: str, categorical_column_name: str):
    probabilities = {}
    dataset_ = datasets[dataset_name].drop(columns="landing_year")
    dataset_ = dataset_[dataset_[categorical_column_name] != "Not stated"]
    dataset_.dropna(inplace=True)

    total_pr_receivers = dataset_.groupby(categorical_column_name).sum().sum()

    aggregation_by_category = pd.DataFrame(
        dataset_.groupby(categorical_column_name).sum()
        ).reset_index()

    for category, amount in zip(
            aggregation_by_category[categorical_column_name], aggregation_by_category[numeric_column_name]
            ):
        probability = amount / total_pr_receivers * 100
        probabilities[category] = round(probability.iloc[0], 4)
        print(f"{category} = {round(probability.iloc[0], 4)}")
    return probabilities


def get_data_probabilities_numerous_columns(dataset_name: str, numeric_column_name: str, categorical_column_name: str):
    probabilities = {}
    dataset_ = datasets[dataset_name].drop(columns="landing_year")
    dataset_ = dataset_[dataset_[categorical_column_name] != "Not stated"]
    dataset_.dropna(inplace=True)

    total_pr_receivers = dataset_.groupby(categorical_column_name).sum().sum()[0]

    aggregation_by_category = pd.DataFrame(
        dataset_.groupby(categorical_column_name).sum()
        ).reset_index()

    for category, amount in zip(
            aggregation_by_category[categorical_column_name], aggregation_by_category[numeric_column_name]
            ):
        probability = amount / total_pr_receivers * 100
        probabilities[category] = round(probability, 4)
        print(f"{category} = {round(probability, 4)}")
    return probabilities


def form_probabilities():
    probabilities = []

    return probabilities


if __name__ == '__main__':
    # age_probabilities = get_data_probabilities(
    #     "raw_data_age", "persons_count_perso", "person_age_level1_eng_desc")
    # birth_country_probabilities = get_data_probabilities(
    #     "raw_data_birth_country", "permit_holders_birth", "birth_country")
    # citizenship_probabilities = get_data_probabilities(
    #     "raw_data_citizenship", "permit_holders_citiz", "citizenship_country")
    education_probabilities = get_data_probabilities(
        "raw_data_education", "persons_count_educa", "education_qualification_eng_desc")
    # print(get_citizenship())
    # print(get_education())
    # education_probabilities = get_data_probabilities(
    #     "raw_data_education",
    #     "persons_count_educa",
    #     "education_qualification_eng_desc"
    #     )
    # gender_probabilities = get_data_probabilities(
    #     "raw_data_gender",
    #     "persons_count_gende",
    #     "gender_eng_desc"
    #     )
    # print(gender_probabilities)
    # legal_status_probabilities = get_data_probabilities_numerous_columns(
    #     "raw_data_legal_status",
    #     "persons_count_main_",
    #     "component_eng_description"
    #     )
    # print(legal_status_probabilities)
    # marital_status_probabilities = get_data_probabilities(
    #     "raw_data_marital_status",
    #     "persons_count_marit",
    #     "marital_status_eng_desc"
    #     )
    # print(marital_status_probabilities)
    # noc_probabilities = get_data_probabilities(  # todo later implementation of this dataset
    #     "noc_2011",
    #     "persons_count_noc_2",
    #     "noc_2011_level4_eng_desc"
    #     )
    # print(noc_probabilities)
    # preferred_language_probabilities = get_data_probabilities(
    #     "raw_data_preferred_language",
    #     "persons_count_prefe",
    #     "preferred_language_eng_desc"
    #     )
    # print(preferred_language_probabilities)
    # province_probabilities = get_data_probabilities(
    #     "raw_data_province",
    #     "persons_count_provi",
    #     "province_long_eng_desc"
    #     )
    # print(province_probabilities)
    # skill_level_1_probabilities = get_data_probabilities_numerous_columns(  # todo later implementation of this
    #  dataset
    #     "raw_data_skill_level_2",
    #     "persons_count_skill",
    #     "skill_level1_eng_desc"
    #     )
    # print(skill_level_1_probabilities)
    # skill_level_2_probabilities = get_data_probabilities_numerous_columns(  # todo later implementation of this
    #  dataset
    #     "raw_data_skill_level_2",
    #     "persons_count_skill",
    #     "skill_level2_eng_desc"
    #     )
    # print(skill_level_2_probabilities)
