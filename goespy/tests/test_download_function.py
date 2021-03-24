from faker import Faker
import datetime

faker = Faker()


def test_abi_downloader():

    initial_date = faker.date_time_ad(
        start_datetime=datetime.datetime(2019, 10, 1, 0, 0),
        end_datetime=datetime.datetime(2019, 10, 1, 23, 0),
    )
    final_date = faker.date_time_ad(
        start_datetime=datetime.datetime(2019, 10, 2, 0, 0),
        end_datetime=datetime.datetime(2019, 10, 2, 23, 0),
    )
    assert type(initial_date) == datetime.datetime
    assert type(final_date) == datetime.datetime
