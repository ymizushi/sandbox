#!/usr/bin/env python3
import time
import asyncio

class Food:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return "<Food: {}>".format(self._name)

class Table:
    def __init__(self):
        self._foods = []

    async def eat(self):
        await asyncio.sleep(2)
        if len(self._foods) == 0:
            print("empty table")
            return None
        else:
            food = self._foods.pop()
            print(food)
            return food

    async def put(self, food):
        self._foods += [food]
        await asyncio.sleep(1)
        print("put food")

class Consumer:
    def __init__(self, table):
        self._table = table

    async def run(self):
        self._table.put(Food("Ikura"))
        self._table.put(Food("Sake"))
        self._table.put(Food("Maguro"))
        await self._table.put(Food("Tama"))

class Producer:
    def __init__(self, table):
        self._table = table

    async def run(self):
        self._table.eat()
        self._table.eat()
        self._table.eat()
        self._table.eat()
        await self._table.eat()

if __name__ == '__main__':
    table = Table()
    producer = Producer(table)
    consumer = Consumer(table)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(producer.run())
    loop.run_until_complete(consumer.run())
