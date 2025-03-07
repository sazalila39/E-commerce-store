import string
import random
import time
from database import Database
from models import CouponTable


def seed_table(num_coupons):
    db = Database()
    db.connect()
    session = db.get_session()
    start = time.time()

    session.bulk_save_objects([
        CouponTable(
            code=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            discount=random.randint(1, 100)
        )
        for _ in range(num_coupons)
    ])

    session.commit()
    session.close()

    print(f"{num_coupons} coupons have been added in {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    seed_table(1000)
