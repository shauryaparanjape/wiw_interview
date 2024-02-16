import pandas as pd

import string

import logging


parent_url = "https://public.wiwdata.com/engineering-challenge/data/"

file_format = "csv"


"""

This logic implements an incremental approach to aggregating the data

Outline of the logic is as follows

1. Load a single file

2. Upload and aggregate the dataframe to its dictionary components

3. Loop through the rest of the files

"""


def main():

    logging.basicConfig()

    logging.getLogger().setLevel(logging.INFO)

    incremental_dict = {}  # This is the empty aggregation dictionary

    char_list = list(string.ascii_lowercase)  # Generate list of alphabets a-z

    try:

        for letter in char_list:

            url = parent_url + letter + "." + file_format

            temp_df = pd.read_csv(url)

            logging.info("File loaded from url: " + url)

            # incremental data load logic into dictionary

            for row in temp_df[["user_id", "path", "length"]].iterrows():

                # check if user id already exists in the dictionary

                if incremental_dict.get(row[1]["user_id"]) is None:

                    incremental_dict[row[1]["user_id"]] = {"user_id": row[1]["user_id"]}

                # only load values if the length is a number

                if isinstance(row[1]["length"], int) or isinstance(
                    row[1]["length"], float
                ):

                    current_length = int(row[1]["length"])

                else:

                    current_length = 0

                next_length = incremental_dict[row[1]["user_id"]].get(row[1]["path"], 0)

                incremental_dict[row[1]["user_id"]][row[1]["path"]] = (
                    current_length + next_length
                )

        concat_df = pd.DataFrame()

        # For loop flattens the dictionary into a pandas dataframe

        for k in incremental_dict.keys():

            interim_df = pd.DataFrame(incremental_dict[k], index=[0])

            concat_df = pd.concat([concat_df, interim_df], axis=0, ignore_index=True)

        concat_df.sort_values("user_id").to_csv("result_incremental.csv", index=False)

    except Exception as exp:

        logging.error(exp)


if __name__ == "__main__":

    main()
