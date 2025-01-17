# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import sys
import re


def create_label_list(file_path="./img_and_label/imagenet1k_label_list.txt"):
    label_list = []
    with open(file_path) as f:
        line_text = f.readline().replace("\n", "")
        while line_text:
            split_line_list = line_text.split(" ")
            label = " "
            label = label.join(split_line_list[1:])
            label = label.split(",")[-1]
            label_list.append(label)
            line_text = f.readline().replace("\n", "")
    return label_list


if __name__ == "__main__":
    label_list = create_label_list(sys.argv[1])
    with open("./result.txt") as f:
        # Starting cls inference
        f.readline()

        # get index and score
        str_text = f.readline()

        # print detial info
        index_str, score_str = str_text.replace("\n", "").split(",")
        index = int(index_str)
        score = float(score_str)
        print(f"The label index is {index}, Max score is {score}, The classification result is {label_list[index]}")
