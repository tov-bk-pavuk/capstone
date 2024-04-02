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


def get_data_probabilities(dataset_name: str, numeric_column_name: str, categorical_column_name: str):
    probabilities_ = {}
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
        probabilities_[category] = round(probability.iloc[0], 4)
        # print(f"{category} = {round(probability.iloc[0], 4)}")
    # total = [i for i in probabilities_.values()]
    # pprint(round(sum(total)))
    return probabilities_


def get_data_probabilities_numerous_columns(dataset_name: str, numeric_column_name: str, categorical_column_name: str):
    probabilities_ = {}
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
        probabilities_[category] = round(probability, 4)
        # print(f"{category} = {round(probability, 4)}")
    # total = [i for i in probabilities_.values()]
    # pprint(round(sum(total)))
    return probabilities_


def form_probabilities():
    return {
        "age": get_data_probabilities(
            "raw_data_age",
            "persons_count_perso",
            "person_age_level1_eng_desc"
            ),
        # todo later implementation of this dataset because of heavy UI
        # "birth_country": get_data_probabilities(
        #     "raw_data_birth_country",
        #     "permit_holders_birth",
        #     "birth_country"
        #     ),
        # todo later implementation of this dataset because of heavy UI
        # "citizenship": get_data_probabilities(
        #     "raw_data_citizenship",
        #     "permit_holders_citiz",
        #     "citizenship_country"
        #     ),
        "education": get_data_probabilities(
            "raw_data_education",
            "persons_count_educa",
            "education_qualification_eng_desc"
            ),
        "gender": get_data_probabilities(
            "raw_data_gender",
            "persons_count_gende",
            "gender_eng_desc"
            ),
        "legal_status": get_data_probabilities_numerous_columns(
            "raw_data_legal_status",
            "persons_count_main_",
            "component_eng_description"
            ),
        "marital_status": get_data_probabilities(
            "raw_data_marital_status",
            "persons_count_marit",
            "marital_status_eng_desc"
            ),
        "preferred_language": get_data_probabilities(
            "raw_data_preferred_language",
            "persons_count_prefe",
            "preferred_language_eng_desc"
            ),
        "province": get_data_probabilities(
            "raw_data_province",
            "persons_count_provi",
            "province_long_eng_desc"
            ),
        # todo later implementation of this dataset
        # "noc_probabilities": get_data_probabilities(
        #     "noc_2011",
        #     "persons_count_noc_2",
        #     "noc_2011_level4_eng_desc"
        #     ),
        # # todo later implementation of this dataset
        # "skill_level_1_probabilities": get_data_probabilities_numerous_columns(
        #
        #     "raw_data_skill_level_2",
        #     "persons_count_skill",
        #     "skill_level1_eng_desc"
        #     ),
        # # todo later implementation of this dataset
        # "skill_level_2_probabilities": get_data_probabilities_numerous_columns(
        #     "raw_data_skill_level_2",
        #     "persons_count_skill",
        #     "skill_level2_eng_desc"
        #     ),
        }


if __name__ == '__main__':
    probabilities = form_probabilities()
    pprint(probabilities)

