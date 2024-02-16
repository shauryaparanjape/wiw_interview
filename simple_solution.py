import pandas as pd

import string

import logging


parent_url = "https://public.wiwdata.com/engineering-challenge/data/"

file_format = "csv"


"""

The logic of the this code is as follows

1. Load all the files into a single dataframe

2. Pivot the table to calculate aggregates on a per user_id basis

3. Save the result to a csv file

"""


def main():

    logging.basicConfig()

    logging.getLogger().setLevel(logging.INFO)

    char_list = list(string.ascii_lowercase)  # Generate list of alphabets a-z

    simple_df = pd.DataFrame()

    try:

        for letter in char_list:

            url = parent_url + letter + "." + file_format

            temp_df = pd.read_csv(url)  # Read csv file from url

            logging.info("File loaded from url: " + url)

            simple_df = pd.concat([simple_df, temp_df], axis=0, ignore_index=True)

        # Pivot table to calculate aggregates on a per user_id basis

        pvt_df = simple_df.pivot_table(
            index="user_id", columns="path", values="length", aggfunc="sum"
        ).reset_index()

        pvt_df.columns.name = None

        pvt_df.to_csv("result_simple.csv", index=False)

    except Exception as exp:

        logging.error(exp)


if __name__ == "__main__":

    main()
