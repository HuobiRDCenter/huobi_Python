#!/bin/bash

echo "UT test start ..."
python3 -m unittest test_api_signature.TestApi
echo "UT test end ..."