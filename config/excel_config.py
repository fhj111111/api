import json


class title_id:
    id = 0
    case_name = 1
    url = 2
    method = 3
    yilai_id = 4
    yilai_ziduan=5
    yilai_data = 6
    header = 7
    data = 8
    asserts = 9
    asserts_suss = 10

def get_yilai_id():
    return title_id.yilai_id


def get_yilai_ziduan():
    return title_id.yilai_ziduan

def get_yilai_data():
    return title_id.yilai_data

def get_id():
    return title_id.id

def get_case_name():
    return title_id.case_name

def get_url():
    return title_id.url

def get_method():
    return title_id.method

def get_header():
    if title_id.header == '':
        return None
    return title_id.header


def get_data():
    if title_id.data == '':
        return None
    return title_id.data


def get_asserts():
    return title_id.asserts

def get_ass_suss():
    return title_id.asserts_suss