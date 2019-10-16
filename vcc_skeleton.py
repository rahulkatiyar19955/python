# DO NOT EDIT THIS FILE
import unittest
import json
from multiprocessing import Process, Manager
from time import clock
import os
import requests

from Question1 import question01
from Question2 import question02
from Question3 import question03
from Question4 import question04
from Question5 import question05
from Question6 import question06


class Test(unittest.TestCase):

    def test_runq1_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        print(travis_uuid)
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/1/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/1/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q1input = test["input"]
                p = Process(target=runq1, args=(q1input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 1 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 1,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 1,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)

        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/1',
                          data=jsonresponse, headers=headers)

    def test_runq2_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/2/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/2/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q2input = test["input"]
                p = Process(target=runq2, args=(q2input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 2 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 2,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 2,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)
        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/2',
                          data=jsonresponse, headers=headers)

    def test_runq3_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/3/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/3/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q3input = test["input"]
                p = Process(target=runq3, args=(q3input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 3 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 3,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 3,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)
        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/3',
                          data=jsonresponse, headers=headers)

    def test_runq4_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/4/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/4/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q4input = test["input"]
                p = Process(target=runq4, args=(q4input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 4 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 4,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 4,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)
        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            print(jsonresponse)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/4',
                          data=jsonresponse, headers=headers)

    def test_runq5_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/5/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/5/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q6input = test["input"]
                p = Process(target=runq5, args=(q6input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 5 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 5,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 5,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)
        print(json.dumps(response))
        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/5',
                          data=jsonresponse, headers=headers)

    def test_runq6_main(self):
        travis_uuid = os.environ.get('travistestidentifier', '')
        if travis_uuid != '' or None:
            url = "https://cscc-gl.herokuapp.com/tests/run/6/" + travis_uuid
        else:
            url = "https://cscc-gl.herokuapp.com/tests/run/6/"
        tests = requests.get(url=url).json()
        response = []
        for testnumber in range(0, len(tests)):
            try:
                return_dict = Manager().dict()
                test = tests[testnumber]
                q6input = test["input"]
                p = Process(target=runq6, args=(q6input, return_dict))
                p.start()

                # Wait for 1 seconds or until process finishes
                p.join(1)

                # If thread is still active
                if p.is_alive():
                    # Terminate
                    print(
                        "A question 6 test has timed out. Each individual test has a maximum of one second to run.")
                    response.append({
                        "questionNumber": 6,
                        "testNumber": testnumber,
                        "correct": "TIMED_OUT",
                        "speed": -1
                    })
                    p.terminate()
                    p.join()
                else:
                    correct = "CORRECT"
                    if return_dict['output'] != test["output"]:
                        correct = "INCORRECT"
                    response.append({
                        "questionNumber": 6,
                        "testNumber": testnumber,
                        "correct": correct,
                        "speed": return_dict['diff'] * 100000000
                    })
            except Exception as e:
                print(e)
        for item in response:
            print(item)
        if travis_uuid != '' or None:
            jsonresponse = json.dumps(response)
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('https://cscc-gl.herokuapp.com/answer/contestant/' + travis_uuid + '/6',
                          data=jsonresponse, headers=headers)


# DO NOT CHANGE THIS FUNCTION EITHER
def runq1(q1input, return_dict):
    start = clock()
    i = json.loads(q1input.replace(" ", ""))
    output = question01(i['initialLevelOfDebt'], i['interestPercentage'], i['repaymentPercentage'])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# DO NOT CHANGE THIS FUNCTION EITHER
def runq2(q2input, return_dict):
    start = clock()
    i = json.loads(q2input.replace(" ", ""))
    output = question02(i['risk'], i['bonus'], i['trader'])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# DO NOT CHANGE THIS FUNCTION EITHER
def runq3(q3input, return_dict):
    start = clock()
    i = json.loads(q3input.replace(" ", ""))
    output = question03(i['scores'], i['alice'])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# DO NOT CHANGE THIS FUNCTION EITHER
def runq4(q4input, return_dict):
    start = clock()
    i = json.loads(q4input.replace(" ", ""))
    output = question04(i['v'], i['c'], i['mc'])
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# DO NOT CHANGE THIS FUNCTION EITHER
def runq5(q5input, return_dict):
    start = clock()
    i = json.loads(q5input.replace(" ", ""))
    output = question05(i)
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


# DO NOT CHANGE THIS FUNCTION EITHER
def runq6(q6input, return_dict):
    start = clock()
    # i = json.loads(q6input)
    output = question06(q6input)
    end = clock()
    diff = end - start
    return_dict['output'] = output
    return_dict['diff'] = diff


if __name__ == '__main__':
    unittest.main()
