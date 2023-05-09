import pytest
from src.utils import load_data, get_filtered_data, dict_modification, date_formatted, masked_from, masked_to

@pytest.fixture
def test_data():
    return [{'id': 41428829, 'state': 'FAILED', 'date': '2019-07-03T18:35:29.512364',
                         'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                         'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
            {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                         'description': 'Перевод организации', 'to': 'Счет 11776614605963066702'},
            {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
                         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},]


def test_load_data(test_data):
    data = load_data(test_data)
    assert isinstance(data, list)

def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]


def test_dict_modification(test_data):
    assert dict_modification(test_data[1:3]) == [{'date': '2019-08-26', 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589', 'amount': '31957.58', 'currency': 'руб.'},
 {'date': '2018-06-30', 'description': 'Перевод организации', 'from': 'Not found', 'to': 'Счет 11776614605963066702', 'amount': '9824.07', 'currency': 'USD'}]


def test_date_formatted(test_data):
    n = [{'date': '2019-12-08', 'description': 'Открытие вклада', 'from': 'Not found', 'to': 'Счет 90424923579946435907', 'amount': '41096.24', 'currency': 'USD'}]
    assert date_formatted(n) == [{'date': '08.12.2019', 'description': 'Открытие вклада', 'from': 'Not found', 'to': 'Счет 90424923579946435907', 'amount': '41096.24', 'currency': 'USD'}]

def test_masked_from(test_data):
    assert masked_from('Visa Classic 2842878893689012') == "Visa Classic 2842 7** **** 9012 ->"

def test_masked_to(test_data):
    assert masked_to('Visa Classic 2842878893689012') == "Visa Classic 2842 7** **** 9012"