import pandas as pd
from matplotlib import pyplot

def convert_csv_to_data_frame(filePath):
    data = pd.read_csv("data.csv", skiprows=[0,2, 3,4,5,6,7])
    return data


obj = {
    "Strongly disagree": 0,
    "Somewhat disagree": 0.25,
    "Neither agree nor disagree": 0.5,
    "Somewhat agree": 0.75,
    "Strongly agree": 1,


    "Not familiar at all": 0,
    "Slightly familiar": 0.25,
    "Moderately familiar": 0.5,
    "Very familiar": 0.75,
    "Extremely familiar": 1,

    "Never": 0,
    "Rarely": 0.2,
    "Sometimes": 0.4,
    "About half the time": 0.6,
    "Most of the time": 0.8,
    "Always": 1,


    "Extremely unclear": 0,
    "Somewhat unclear": 0.25,
    "Neither clear nor unclear": 0.50,
    "Somewhat clear": 0.75,
    "Extremely clear": 1,

    "Yes": 1,
    "No": 0,
    "Not sure": 0.5,

    "Not at all confident": 0,
    "Slightly confident": 0.25,
    "Moderately confident": 0.5,
    "Very confident": 0.75,
    "Extremely confident": 1,

    "None at all": 0,
    "A little": 0.25,
    "A moderate amount": 0.5,
    "A lot": 0.75,
    "A great deal": 1,

    "No impact": 0,
    "Slightly reduces trust": 0.25,
    "Moderately reduces trust": 0.50,
    "Significantly reduces trust": 0.75,
    "Completely lose trust": 1,

    "Extremely unlikely": 0,
    "Somewhat unlikely": 0.25,
    "Neither likely nor unlikely": 0.5,
    "Somewhat likely": 0.75,
    "Extremely likely": 1,


    "less than 20k": 0,
    "20-30k": 0.25,
    "30-40k": 0.5,
    "40-50k": 0.75,
    "above 50k": 1,

    "High school or equivalent" : 0,
    "Diploma/Associate degree": 0.2,
    "Other (Please specify): _": 0.4,
    "Bachelor’s degree": 0.6,
    "Master’s degree": 0.8,
    "Doctorate": 1,


    "Daily": 0,
    "4-6 times a week": 0.25,
    "2-3 times a week": 0.5,
    "Once a week": 0.75,
    "Monthly": 1,


    "Always choose the cheaper product": 0,
    "Sometimes choose the cheaper product": 0.25,
    "Choose depending on the situation": 0.5,
    "Rarely choose the cheaper product": 0.75,
    "Always choose the eco-friendly product": 1,

    "Price is the most important factor": 0,
    "Price is somewhat important, but I prefer eco-friendly products": 0.5,
    "Price does not matter if the product is truly eco-friendly": 1,
}

def convert_column_to_numberic_value(data):
    result = []
    for index, value in enumerate(data):
        print(value, index)
        in_numeric = obj[value]
        result.append(in_numeric)
    return result

def convert_data_frame_to_numeric_value(data_frame):
    columns = data_frame.columns
    new_data_frame = pd.DataFrame()
    for index, column in enumerate(columns): 
        print(column)
        new_data_frame.insert(index, column, convert_column_to_numberic_value(data[column]))
    return new_data_frame
    

if __name__ == '__main__':
    data = convert_csv_to_data_frame(filePath='data.xlsx')
    
    # Hypothesis One
    print('----------------------------------------- Hypothesis-1 -------------------------------------------------------------------')
    hypothesis_name = "HP_1"
    columns = [
        'I understand the information presented on FMCG product labels and am satisfied with the clarity of these claims.',
        'How often do you read FMCG product labels to check for environmental claims (e.g., recyclable, sustainable, biodegradable)?',
        'Have you ever seen an FMCG product that made environmental claims on its label that you found to be exaggerated or false?',
        'How confident are you in identifying misleading or false environmental claims on FMCG product labels?',
    ]

    hypothesis_one_data_frame = data[columns]
    hypothesis_one_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_one_data_frame)
    hypothesis_one_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_one_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))


    print('------------------------------------------- Hypothesis-2 -----------------------------------------------------------------')
    hypothesis_name = "HP_2"
    hp_two_columns = [
        'I understand the information presented on FMCG product labels and am satisfied with the clarity of these claims.',
        'How clear and visible do you find environmental claims on FMCG product packaging?',
        'How much does the presence of environmental claims on FMCG products influence your purchasing decisions?',
        'Would you be willing to pay more for an FMCG product with verified and transparent environmental claims, even if the price is higher than misleading products?'
    ]

    hypothesis_two_data_frame = data[hp_two_columns]
    hypothesis_two_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_two_data_frame)
    hypothesis_two_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_one_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))


    print("-------------------------------------------- Hypothesis-3 -----------------------------------------------------------------")
    hypothesis_name = "HP_3"
    hp_three_columns = [
        'Have you ever seen an FMCG product that made environmental claims on its label that you found to be exaggerated or false?',
        'If you find that a brand’s environmental claims are misleading, how likely are you to stop purchasing their products?',
        'To what extent do misleading environmental claims affect your trust in a brand?',
        'How likely are you to continue purchasing instant cooking products even if their environmental claims are misleading or unclear?',
    ]

    hypothesis_three_data_frame = data[hp_three_columns]
    hypothesis_three_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_three_data_frame)
    hypothesis_three_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_three_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))


    print("-------------------------------------------- Hypothesis-4 -----------------------------------------------------------------")
    hypothesis_name = "HP_4"
    hp_four_columns = [
        'Are you aware that consuming instant or fast-cooking meals may have potential health risks despite being marketed as "natural" or "healthy"?',
        'If you are aware of the potential health risks of instant cooking items, do you still choose them due to convenience?',
        'Do you think FMCG brands intentionally use vague or misleading labels to make their products seem more environmentally friendly?',
        'Would you prefer if FMCG brands provided more detailed information about their ingredients and the environmental impact of their products?',
    ]

    hypothesis_four_data_frame = data[hp_four_columns]
    hypothesis_four_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_four_data_frame)
    hypothesis_four_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_four_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))


    print("-------------------------------------------- Hypothesis-5 -----------------------------------------------------------------")
    hypothesis_name = "HP_5"
    hp_five_columns = [
        'What is your highest level of education? - Selected Choice',
        'What is your household average monthy income',
        'How confident are you in identifying misleading or false environmental claims on FMCG product labels?',
        'How often do you read the ingredients list on FMCG product labels to verify the accuracy of environmental claims (e.g., "natural," "chemical-free")?',
        'Do you feel that FMCG brands provide sufficient transparency about the sourcing and processing of ingredients, particularly in products claiming to be "green" or "eco-friendly"?',
    ]

    hypothesis_five_data_frame = data[hp_five_columns]
    hypothesis_five_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_five_data_frame)
    hypothesis_five_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_five_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))

    print("---------------------------------------------- Hypothesis-6 ---------------------------------------------------------------")
    hypothesis_name = "HP_6"
    hp_six_columns = [
        'How often do you purchase Fast-Moving Consumer Goods (FMCG) such as food, beverages, household items, or personal care products?',
        'How much does the presence of environmental claims on FMCG products influence your purchasing decisions?',
        'If an FMCG product contains misleading environmental claims but is priced significantly lower than a truly eco-friendly product, which would you choose?',
        'To what extent does price influence your decision to purchase an FMCG product that makes environmental claims?',
    ]
    hypothesis_six_data_frame = data[hp_six_columns]
    hypothesis_six_data_frame_numeric = convert_data_frame_to_numeric_value(hypothesis_six_data_frame)
    hypothesis_six_data_frame_numeric.to_csv(f'{hypothesis_name}_numeric.csv', index=False)
    print(hypothesis_six_data_frame_numeric.corr('pearson').to_csv(f'{hypothesis_name}_corr.csv', index=False))



