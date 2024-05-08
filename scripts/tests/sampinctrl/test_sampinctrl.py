# Copyright (c) 2021 Teslabs Engineering S.L.
# Copyright (c) 2022 Gerson Fernando Budke
# SPDX-License-Identifier: Apache-2.0

from sampinctrl import main


def test_main(data, tmp_path):
    """
    Verifies that pinctrl headers are generated correctly by comparing the contents
    of reference files with the generated files in a temporary directory.

    Args:
        data (`object`.): directory containing the reference pinctrl headers that
            are used for comparison with the generated files.
            
            		- `data`: A dictionary containing the following keys:
            		+ `FILES`: A list of strings representing the file paths to be checked
            for correctness.
        tmp_path (str): directory where the generated pinctrl headers will be stored.

    """

    main(data, tmp_path)

    FILES = (
        "samad-pinctrl.h",
        "samae-pinctrl.h",
        "samaf-pinctrl.h",
        "sambe-pinctrl.h",
        "sambf-pinctrl.h",
        "samcf-pinctrl.h",
    )

    for file in FILES:
        ref_file = data / file
        gen_file = tmp_path / file

        assert gen_file.exists()

        with open(ref_file) as ref, open(gen_file) as gen:
            assert ref.read() == gen.read()
