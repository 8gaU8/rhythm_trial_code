class DummySerial:
    in_waiting = 1

    def __init__(self, *args, **kwargs) -> None:
        pass

    def write(self, arg):
        if arg != [0]:
            print(f"write {arg}")
        return arg

    def read(self, arg):
        return bin(0x01)

    def close(self):
        ...
