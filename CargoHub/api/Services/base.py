from datetime import datetime

# schrijf alle onnodige extra functies in deze parent class
# Parent class
class Base:
    def __init__():
        pass

    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"