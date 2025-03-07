import string
import random
import time
import asyncio
from models import CouponTable
from database import Database


def generate_coupons(num_coupons):
    return [
        CouponTable(
            code=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            discount=random.randint(1, 100)
        )
        for _ in range(num_coupons)
    ]


def seed_table(num_coupons):
    db = Database()
    db.connect_sync()
    session = db.get_session()

    start = time.time()

    session.add_all(generate_coupons(num_coupons))
    session.commit()
    session.close()

    print(f"{num_coupons} coupons have been added in {time.time() - start:.2f} seconds")


async def seed_table_async(num_coupons):
    db = Database(async_mode=True)
    await db.connect_async()
    session = db.get_session()

    start = time.time()

    session.add_all(generate_coupons(num_coupons))
    await session.commit()
    await db.close()

    print(f"{num_coupons} coupons have been added in {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    seed_table(1000)
    asyncio.run(seed_table_async(1000))
